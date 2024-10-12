/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDisplayNameDisapprovalReason.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDisplayNameDisapprovalReason::OAIDisplayNameDisapprovalReason(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDisplayNameDisapprovalReason::OAIDisplayNameDisapprovalReason() {
    this->initializeModel();
}

OAIDisplayNameDisapprovalReason::~OAIDisplayNameDisapprovalReason() {}

void OAIDisplayNameDisapprovalReason::initializeModel() {

    m_disapproval_reason_isSet = false;
    m_disapproval_reason_isValid = false;

    m_language_code_isSet = false;
    m_language_code_isValid = false;
}

void OAIDisplayNameDisapprovalReason::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDisplayNameDisapprovalReason::fromJsonObject(QJsonObject json) {

    m_disapproval_reason_isValid = ::OpenAPI::fromJsonValue(m_disapproval_reason, json[QString("disapprovalReason")]);
    m_disapproval_reason_isSet = !json[QString("disapprovalReason")].isNull() && m_disapproval_reason_isValid;

    m_language_code_isValid = ::OpenAPI::fromJsonValue(m_language_code, json[QString("languageCode")]);
    m_language_code_isSet = !json[QString("languageCode")].isNull() && m_language_code_isValid;
}

QString OAIDisplayNameDisapprovalReason::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDisplayNameDisapprovalReason::asJsonObject() const {
    QJsonObject obj;
    if (m_disapproval_reason_isSet) {
        obj.insert(QString("disapprovalReason"), ::OpenAPI::toJsonValue(m_disapproval_reason));
    }
    if (m_language_code_isSet) {
        obj.insert(QString("languageCode"), ::OpenAPI::toJsonValue(m_language_code));
    }
    return obj;
}

QString OAIDisplayNameDisapprovalReason::getDisapprovalReason() const {
    return m_disapproval_reason;
}
void OAIDisplayNameDisapprovalReason::setDisapprovalReason(const QString &disapproval_reason) {
    m_disapproval_reason = disapproval_reason;
    m_disapproval_reason_isSet = true;
}

bool OAIDisplayNameDisapprovalReason::is_disapproval_reason_Set() const{
    return m_disapproval_reason_isSet;
}

bool OAIDisplayNameDisapprovalReason::is_disapproval_reason_Valid() const{
    return m_disapproval_reason_isValid;
}

QString OAIDisplayNameDisapprovalReason::getLanguageCode() const {
    return m_language_code;
}
void OAIDisplayNameDisapprovalReason::setLanguageCode(const QString &language_code) {
    m_language_code = language_code;
    m_language_code_isSet = true;
}

bool OAIDisplayNameDisapprovalReason::is_language_code_Set() const{
    return m_language_code_isSet;
}

bool OAIDisplayNameDisapprovalReason::is_language_code_Valid() const{
    return m_language_code_isValid;
}

bool OAIDisplayNameDisapprovalReason::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_disapproval_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDisplayNameDisapprovalReason::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
