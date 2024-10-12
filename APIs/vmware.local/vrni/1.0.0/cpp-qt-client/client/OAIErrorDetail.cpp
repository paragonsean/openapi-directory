/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIErrorDetail.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIErrorDetail::OAIErrorDetail(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIErrorDetail::OAIErrorDetail() {
    this->initializeModel();
}

OAIErrorDetail::~OAIErrorDetail() {}

void OAIErrorDetail::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;
}

void OAIErrorDetail::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIErrorDetail::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;
}

QString OAIErrorDetail::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIErrorDetail::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_target.size() > 0) {
        obj.insert(QString("target"), ::OpenAPI::toJsonValue(m_target));
    }
    return obj;
}

qint32 OAIErrorDetail::getCode() const {
    return m_code;
}
void OAIErrorDetail::setCode(const qint32 &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIErrorDetail::is_code_Set() const{
    return m_code_isSet;
}

bool OAIErrorDetail::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIErrorDetail::getMessage() const {
    return m_message;
}
void OAIErrorDetail::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIErrorDetail::is_message_Set() const{
    return m_message_isSet;
}

bool OAIErrorDetail::is_message_Valid() const{
    return m_message_isValid;
}

QList<QString> OAIErrorDetail::getTarget() const {
    return m_target;
}
void OAIErrorDetail::setTarget(const QList<QString> &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIErrorDetail::is_target_Set() const{
    return m_target_isSet;
}

bool OAIErrorDetail::is_target_Valid() const{
    return m_target_isValid;
}

bool OAIErrorDetail::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIErrorDetail::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
