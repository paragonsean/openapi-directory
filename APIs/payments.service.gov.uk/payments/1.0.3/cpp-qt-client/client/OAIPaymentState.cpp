/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPaymentState.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaymentState::OAIPaymentState(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaymentState::OAIPaymentState() {
    this->initializeModel();
}

OAIPaymentState::~OAIPaymentState() {}

void OAIPaymentState::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_finished_isSet = false;
    m_finished_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIPaymentState::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPaymentState::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_finished_isValid = ::OpenAPI::fromJsonValue(m_finished, json[QString("finished")]);
    m_finished_isSet = !json[QString("finished")].isNull() && m_finished_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIPaymentState::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPaymentState::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_finished_isSet) {
        obj.insert(QString("finished"), ::OpenAPI::toJsonValue(m_finished));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIPaymentState::getCode() const {
    return m_code;
}
void OAIPaymentState::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIPaymentState::is_code_Set() const{
    return m_code_isSet;
}

bool OAIPaymentState::is_code_Valid() const{
    return m_code_isValid;
}

bool OAIPaymentState::isFinished() const {
    return m_finished;
}
void OAIPaymentState::setFinished(const bool &finished) {
    m_finished = finished;
    m_finished_isSet = true;
}

bool OAIPaymentState::is_finished_Set() const{
    return m_finished_isSet;
}

bool OAIPaymentState::is_finished_Valid() const{
    return m_finished_isValid;
}

QString OAIPaymentState::getMessage() const {
    return m_message;
}
void OAIPaymentState::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIPaymentState::is_message_Set() const{
    return m_message_isSet;
}

bool OAIPaymentState::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIPaymentState::getStatus() const {
    return m_status;
}
void OAIPaymentState::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPaymentState::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPaymentState::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIPaymentState::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_finished_isSet) {
            isObjectUpdated = true;
            break;
        }

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

bool OAIPaymentState::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
