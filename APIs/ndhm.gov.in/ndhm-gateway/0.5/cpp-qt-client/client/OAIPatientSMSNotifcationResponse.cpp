/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPatientSMSNotifcationResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientSMSNotifcationResponse::OAIPatientSMSNotifcationResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientSMSNotifcationResponse::OAIPatientSMSNotifcationResponse() {
    this->initializeModel();
}

OAIPatientSMSNotifcationResponse::~OAIPatientSMSNotifcationResponse() {}

void OAIPatientSMSNotifcationResponse::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_resp_isSet = false;
    m_resp_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIPatientSMSNotifcationResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientSMSNotifcationResponse::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_resp_isValid = ::OpenAPI::fromJsonValue(m_resp, json[QString("resp")]);
    m_resp_isSet = !json[QString("resp")].isNull() && m_resp_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIPatientSMSNotifcationResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientSMSNotifcationResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_resp.isSet()) {
        obj.insert(QString("resp"), ::OpenAPI::toJsonValue(m_resp));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

OAIError OAIPatientSMSNotifcationResponse::getError() const {
    return m_error;
}
void OAIPatientSMSNotifcationResponse::setError(const OAIError &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIPatientSMSNotifcationResponse::is_error_Set() const{
    return m_error_isSet;
}

bool OAIPatientSMSNotifcationResponse::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIPatientSMSNotifcationResponse::getRequestId() const {
    return m_request_id;
}
void OAIPatientSMSNotifcationResponse::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIPatientSMSNotifcationResponse::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIPatientSMSNotifcationResponse::is_request_id_Valid() const{
    return m_request_id_isValid;
}

OAIRequestReference OAIPatientSMSNotifcationResponse::getResp() const {
    return m_resp;
}
void OAIPatientSMSNotifcationResponse::setResp(const OAIRequestReference &resp) {
    m_resp = resp;
    m_resp_isSet = true;
}

bool OAIPatientSMSNotifcationResponse::is_resp_Set() const{
    return m_resp_isSet;
}

bool OAIPatientSMSNotifcationResponse::is_resp_Valid() const{
    return m_resp_isValid;
}

QString OAIPatientSMSNotifcationResponse::getStatus() const {
    return m_status;
}
void OAIPatientSMSNotifcationResponse::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPatientSMSNotifcationResponse::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPatientSMSNotifcationResponse::is_status_Valid() const{
    return m_status_isValid;
}

QDateTime OAIPatientSMSNotifcationResponse::getTimestamp() const {
    return m_timestamp;
}
void OAIPatientSMSNotifcationResponse::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIPatientSMSNotifcationResponse::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIPatientSMSNotifcationResponse::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIPatientSMSNotifcationResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resp.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientSMSNotifcationResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_request_id_isValid && m_resp_isValid && m_timestamp_isValid && true;
}

} // namespace OpenAPI
