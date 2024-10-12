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

#include "OAIPatientAuthNotificationAcknowledgement.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientAuthNotificationAcknowledgement::OAIPatientAuthNotificationAcknowledgement(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientAuthNotificationAcknowledgement::OAIPatientAuthNotificationAcknowledgement() {
    this->initializeModel();
}

OAIPatientAuthNotificationAcknowledgement::~OAIPatientAuthNotificationAcknowledgement() {}

void OAIPatientAuthNotificationAcknowledgement::initializeModel() {

    m_acknowledgement_isSet = false;
    m_acknowledgement_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_resp_isSet = false;
    m_resp_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIPatientAuthNotificationAcknowledgement::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientAuthNotificationAcknowledgement::fromJsonObject(QJsonObject json) {

    m_acknowledgement_isValid = ::OpenAPI::fromJsonValue(m_acknowledgement, json[QString("acknowledgement")]);
    m_acknowledgement_isSet = !json[QString("acknowledgement")].isNull() && m_acknowledgement_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_resp_isValid = ::OpenAPI::fromJsonValue(m_resp, json[QString("resp")]);
    m_resp_isSet = !json[QString("resp")].isNull() && m_resp_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIPatientAuthNotificationAcknowledgement::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientAuthNotificationAcknowledgement::asJsonObject() const {
    QJsonObject obj;
    if (m_acknowledgement.isSet()) {
        obj.insert(QString("acknowledgement"), ::OpenAPI::toJsonValue(m_acknowledgement));
    }
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_resp.isSet()) {
        obj.insert(QString("resp"), ::OpenAPI::toJsonValue(m_resp));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

OAIPatientAuthNotificationAcknowledgement_acknowledgement OAIPatientAuthNotificationAcknowledgement::getAcknowledgement() const {
    return m_acknowledgement;
}
void OAIPatientAuthNotificationAcknowledgement::setAcknowledgement(const OAIPatientAuthNotificationAcknowledgement_acknowledgement &acknowledgement) {
    m_acknowledgement = acknowledgement;
    m_acknowledgement_isSet = true;
}

bool OAIPatientAuthNotificationAcknowledgement::is_acknowledgement_Set() const{
    return m_acknowledgement_isSet;
}

bool OAIPatientAuthNotificationAcknowledgement::is_acknowledgement_Valid() const{
    return m_acknowledgement_isValid;
}

OAIError OAIPatientAuthNotificationAcknowledgement::getError() const {
    return m_error;
}
void OAIPatientAuthNotificationAcknowledgement::setError(const OAIError &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIPatientAuthNotificationAcknowledgement::is_error_Set() const{
    return m_error_isSet;
}

bool OAIPatientAuthNotificationAcknowledgement::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIPatientAuthNotificationAcknowledgement::getRequestId() const {
    return m_request_id;
}
void OAIPatientAuthNotificationAcknowledgement::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIPatientAuthNotificationAcknowledgement::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIPatientAuthNotificationAcknowledgement::is_request_id_Valid() const{
    return m_request_id_isValid;
}

OAIRequestReference OAIPatientAuthNotificationAcknowledgement::getResp() const {
    return m_resp;
}
void OAIPatientAuthNotificationAcknowledgement::setResp(const OAIRequestReference &resp) {
    m_resp = resp;
    m_resp_isSet = true;
}

bool OAIPatientAuthNotificationAcknowledgement::is_resp_Set() const{
    return m_resp_isSet;
}

bool OAIPatientAuthNotificationAcknowledgement::is_resp_Valid() const{
    return m_resp_isValid;
}

QDateTime OAIPatientAuthNotificationAcknowledgement::getTimestamp() const {
    return m_timestamp;
}
void OAIPatientAuthNotificationAcknowledgement::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIPatientAuthNotificationAcknowledgement::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIPatientAuthNotificationAcknowledgement::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIPatientAuthNotificationAcknowledgement::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_acknowledgement.isSet()) {
            isObjectUpdated = true;
            break;
        }

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

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientAuthNotificationAcknowledgement::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_request_id_isValid && m_resp_isValid && m_timestamp_isValid && true;
}

} // namespace OpenAPI
