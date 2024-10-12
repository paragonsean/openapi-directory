/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVerifySmsRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVerifySmsRequest::OAIVerifySmsRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVerifySmsRequest::OAIVerifySmsRequest() {
    this->initializeModel();
}

OAIVerifySmsRequest::~OAIVerifySmsRequest() {}

void OAIVerifySmsRequest::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_sms_isSet = false;
    m_sms_isValid = false;
}

void OAIVerifySmsRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVerifySmsRequest::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_sms_isValid = ::OpenAPI::fromJsonValue(m_sms, json[QString("sms")]);
    m_sms_isSet = !json[QString("sms")].isNull() && m_sms_isValid;
}

QString OAIVerifySmsRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVerifySmsRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_sms_isSet) {
        obj.insert(QString("sms"), ::OpenAPI::toJsonValue(m_sms));
    }
    return obj;
}

QString OAIVerifySmsRequest::getCode() const {
    return m_code;
}
void OAIVerifySmsRequest::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIVerifySmsRequest::is_code_Set() const{
    return m_code_isSet;
}

bool OAIVerifySmsRequest::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIVerifySmsRequest::getSms() const {
    return m_sms;
}
void OAIVerifySmsRequest::setSms(const QString &sms) {
    m_sms = sms;
    m_sms_isSet = true;
}

bool OAIVerifySmsRequest::is_sms_Set() const{
    return m_sms_isSet;
}

bool OAIVerifySmsRequest::is_sms_Valid() const{
    return m_sms_isValid;
}

bool OAIVerifySmsRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sms_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVerifySmsRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_code_isValid && m_sms_isValid && true;
}

} // namespace OpenAPI
