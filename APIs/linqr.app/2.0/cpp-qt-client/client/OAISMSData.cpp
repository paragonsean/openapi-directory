/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISMSData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISMSData::OAISMSData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISMSData::OAISMSData() {
    this->initializeModel();
}

OAISMSData::~OAISMSData() {}

void OAISMSData::initializeModel() {

    m_message_isSet = false;
    m_message_isValid = false;

    m_to_isSet = false;
    m_to_isValid = false;
}

void OAISMSData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISMSData::fromJsonObject(QJsonObject json) {

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_to_isValid = ::OpenAPI::fromJsonValue(m_to, json[QString("to")]);
    m_to_isSet = !json[QString("to")].isNull() && m_to_isValid;
}

QString OAISMSData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISMSData::asJsonObject() const {
    QJsonObject obj;
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_to.isSet()) {
        obj.insert(QString("to"), ::OpenAPI::toJsonValue(m_to));
    }
    return obj;
}

QString OAISMSData::getMessage() const {
    return m_message;
}
void OAISMSData::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAISMSData::is_message_Set() const{
    return m_message_isSet;
}

bool OAISMSData::is_message_Valid() const{
    return m_message_isValid;
}

OAITo_1 OAISMSData::getTo() const {
    return m_to;
}
void OAISMSData::setTo(const OAITo_1 &to) {
    m_to = to;
    m_to_isSet = true;
}

bool OAISMSData::is_to_Set() const{
    return m_to_isSet;
}

bool OAISMSData::is_to_Valid() const{
    return m_to_isValid;
}

bool OAISMSData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_to.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISMSData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_to_isValid && true;
}

} // namespace OpenAPI
