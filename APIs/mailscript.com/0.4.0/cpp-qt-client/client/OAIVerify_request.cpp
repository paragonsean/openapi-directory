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

#include "OAIVerify_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVerify_request::OAIVerify_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVerify_request::OAIVerify_request() {
    this->initializeModel();
}

OAIVerify_request::~OAIVerify_request() {}

void OAIVerify_request::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_sms_isSet = false;
    m_sms_isValid = false;
}

void OAIVerify_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVerify_request::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_sms_isValid = ::OpenAPI::fromJsonValue(m_sms, json[QString("sms")]);
    m_sms_isSet = !json[QString("sms")].isNull() && m_sms_isValid;
}

QString OAIVerify_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVerify_request::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_sms_isSet) {
        obj.insert(QString("sms"), ::OpenAPI::toJsonValue(m_sms));
    }
    return obj;
}

QString OAIVerify_request::getCode() const {
    return m_code;
}
void OAIVerify_request::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIVerify_request::is_code_Set() const{
    return m_code_isSet;
}

bool OAIVerify_request::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIVerify_request::getEmail() const {
    return m_email;
}
void OAIVerify_request::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIVerify_request::is_email_Set() const{
    return m_email_isSet;
}

bool OAIVerify_request::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIVerify_request::getSms() const {
    return m_sms;
}
void OAIVerify_request::setSms(const QString &sms) {
    m_sms = sms;
    m_sms_isSet = true;
}

bool OAIVerify_request::is_sms_Set() const{
    return m_sms_isSet;
}

bool OAIVerify_request::is_sms_Valid() const{
    return m_sms_isValid;
}

bool OAIVerify_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
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

bool OAIVerify_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_code_isValid && m_email_isValid && m_sms_isValid && true;
}

} // namespace OpenAPI
