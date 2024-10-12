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

#include "OAIAddVerification_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddVerification_request::OAIAddVerification_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddVerification_request::OAIAddVerification_request() {
    this->initializeModel();
}

OAIAddVerification_request::~OAIAddVerification_request() {}

void OAIAddVerification_request::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_sms_isSet = false;
    m_sms_isValid = false;
}

void OAIAddVerification_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddVerification_request::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_sms_isValid = ::OpenAPI::fromJsonValue(m_sms, json[QString("sms")]);
    m_sms_isSet = !json[QString("sms")].isNull() && m_sms_isValid;
}

QString OAIAddVerification_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddVerification_request::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_sms_isSet) {
        obj.insert(QString("sms"), ::OpenAPI::toJsonValue(m_sms));
    }
    return obj;
}

QString OAIAddVerification_request::getEmail() const {
    return m_email;
}
void OAIAddVerification_request::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIAddVerification_request::is_email_Set() const{
    return m_email_isSet;
}

bool OAIAddVerification_request::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIAddVerification_request::getType() const {
    return m_type;
}
void OAIAddVerification_request::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAddVerification_request::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAddVerification_request::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIAddVerification_request::getSms() const {
    return m_sms;
}
void OAIAddVerification_request::setSms(const QString &sms) {
    m_sms = sms;
    m_sms_isSet = true;
}

bool OAIAddVerification_request::is_sms_Set() const{
    return m_sms_isSet;
}

bool OAIAddVerification_request::is_sms_Valid() const{
    return m_sms_isValid;
}

bool OAIAddVerification_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
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

bool OAIAddVerification_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_email_isValid && m_type_isValid && m_sms_isValid && true;
}

} // namespace OpenAPI
