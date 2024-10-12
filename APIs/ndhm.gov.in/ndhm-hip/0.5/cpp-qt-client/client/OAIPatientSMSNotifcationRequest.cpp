/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPatientSMSNotifcationRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientSMSNotifcationRequest::OAIPatientSMSNotifcationRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientSMSNotifcationRequest::OAIPatientSMSNotifcationRequest() {
    this->initializeModel();
}

OAIPatientSMSNotifcationRequest::~OAIPatientSMSNotifcationRequest() {}

void OAIPatientSMSNotifcationRequest::initializeModel() {

    m_notification_isSet = false;
    m_notification_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIPatientSMSNotifcationRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientSMSNotifcationRequest::fromJsonObject(QJsonObject json) {

    m_notification_isValid = ::OpenAPI::fromJsonValue(m_notification, json[QString("notification")]);
    m_notification_isSet = !json[QString("notification")].isNull() && m_notification_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIPatientSMSNotifcationRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientSMSNotifcationRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_notification.isSet()) {
        obj.insert(QString("notification"), ::OpenAPI::toJsonValue(m_notification));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

OAIPatientSMSNotifcationRequest_notification OAIPatientSMSNotifcationRequest::getNotification() const {
    return m_notification;
}
void OAIPatientSMSNotifcationRequest::setNotification(const OAIPatientSMSNotifcationRequest_notification &notification) {
    m_notification = notification;
    m_notification_isSet = true;
}

bool OAIPatientSMSNotifcationRequest::is_notification_Set() const{
    return m_notification_isSet;
}

bool OAIPatientSMSNotifcationRequest::is_notification_Valid() const{
    return m_notification_isValid;
}

QString OAIPatientSMSNotifcationRequest::getRequestId() const {
    return m_request_id;
}
void OAIPatientSMSNotifcationRequest::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIPatientSMSNotifcationRequest::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIPatientSMSNotifcationRequest::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QDateTime OAIPatientSMSNotifcationRequest::getTimestamp() const {
    return m_timestamp;
}
void OAIPatientSMSNotifcationRequest::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIPatientSMSNotifcationRequest::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIPatientSMSNotifcationRequest::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIPatientSMSNotifcationRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_notification.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
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

bool OAIPatientSMSNotifcationRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_notification_isValid && m_request_id_isValid && m_timestamp_isValid && true;
}

} // namespace OpenAPI
