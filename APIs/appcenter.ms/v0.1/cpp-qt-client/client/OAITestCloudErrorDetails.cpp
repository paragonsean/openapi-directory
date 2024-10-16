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

#include "OAITestCloudErrorDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITestCloudErrorDetails::OAITestCloudErrorDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITestCloudErrorDetails::OAITestCloudErrorDetails() {
    this->initializeModel();
}

OAITestCloudErrorDetails::~OAITestCloudErrorDetails() {}

void OAITestCloudErrorDetails::initializeModel() {

    m_message_isSet = false;
    m_message_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAITestCloudErrorDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITestCloudErrorDetails::fromJsonObject(QJsonObject json) {

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAITestCloudErrorDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITestCloudErrorDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAITestCloudErrorDetails::getMessage() const {
    return m_message;
}
void OAITestCloudErrorDetails::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAITestCloudErrorDetails::is_message_Set() const{
    return m_message_isSet;
}

bool OAITestCloudErrorDetails::is_message_Valid() const{
    return m_message_isValid;
}

QString OAITestCloudErrorDetails::getStatus() const {
    return m_status;
}
void OAITestCloudErrorDetails::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAITestCloudErrorDetails::is_status_Set() const{
    return m_status_isSet;
}

bool OAITestCloudErrorDetails::is_status_Valid() const{
    return m_status_isValid;
}

bool OAITestCloudErrorDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_message_isSet) {
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

bool OAITestCloudErrorDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_message_isValid && m_status_isValid && true;
}

} // namespace OpenAPI
