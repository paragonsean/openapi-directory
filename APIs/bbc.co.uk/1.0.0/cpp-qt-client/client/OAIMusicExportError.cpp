/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMusicExportError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMusicExportError::OAIMusicExportError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMusicExportError::OAIMusicExportError() {
    this->initializeModel();
}

OAIMusicExportError::~OAIMusicExportError() {}

void OAIMusicExportError::initializeModel() {

    m_message_isSet = false;
    m_message_isValid = false;

    m_replied_at_isSet = false;
    m_replied_at_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIMusicExportError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMusicExportError::fromJsonObject(QJsonObject json) {

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_replied_at_isValid = ::OpenAPI::fromJsonValue(m_replied_at, json[QString("replied_at")]);
    m_replied_at_isSet = !json[QString("replied_at")].isNull() && m_replied_at_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIMusicExportError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMusicExportError::asJsonObject() const {
    QJsonObject obj;
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_replied_at_isSet) {
        obj.insert(QString("replied_at"), ::OpenAPI::toJsonValue(m_replied_at));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIMusicExportError::getMessage() const {
    return m_message;
}
void OAIMusicExportError::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIMusicExportError::is_message_Set() const{
    return m_message_isSet;
}

bool OAIMusicExportError::is_message_Valid() const{
    return m_message_isValid;
}

qint32 OAIMusicExportError::getRepliedAt() const {
    return m_replied_at;
}
void OAIMusicExportError::setRepliedAt(const qint32 &replied_at) {
    m_replied_at = replied_at;
    m_replied_at_isSet = true;
}

bool OAIMusicExportError::is_replied_at_Set() const{
    return m_replied_at_isSet;
}

bool OAIMusicExportError::is_replied_at_Valid() const{
    return m_replied_at_isValid;
}

qint32 OAIMusicExportError::getStatus() const {
    return m_status;
}
void OAIMusicExportError::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIMusicExportError::is_status_Set() const{
    return m_status_isSet;
}

bool OAIMusicExportError::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIMusicExportError::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_replied_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMusicExportError::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_message_isValid && m_replied_at_isValid && m_status_isValid && true;
}

} // namespace OpenAPI
