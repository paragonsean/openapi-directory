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

#include "OAIHIUSubscriptionNotification.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHIUSubscriptionNotification::OAIHIUSubscriptionNotification(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHIUSubscriptionNotification::OAIHIUSubscriptionNotification() {
    this->initializeModel();
}

OAIHIUSubscriptionNotification::~OAIHIUSubscriptionNotification() {}

void OAIHIUSubscriptionNotification::initializeModel() {

    m_event_isSet = false;
    m_event_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIHIUSubscriptionNotification::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHIUSubscriptionNotification::fromJsonObject(QJsonObject json) {

    m_event_isValid = ::OpenAPI::fromJsonValue(m_event, json[QString("event")]);
    m_event_isSet = !json[QString("event")].isNull() && m_event_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIHIUSubscriptionNotification::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHIUSubscriptionNotification::asJsonObject() const {
    QJsonObject obj;
    if (m_event.isSet()) {
        obj.insert(QString("event"), ::OpenAPI::toJsonValue(m_event));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

OAIHIUSubscriptionNotification_event OAIHIUSubscriptionNotification::getEvent() const {
    return m_event;
}
void OAIHIUSubscriptionNotification::setEvent(const OAIHIUSubscriptionNotification_event &event) {
    m_event = event;
    m_event_isSet = true;
}

bool OAIHIUSubscriptionNotification::is_event_Set() const{
    return m_event_isSet;
}

bool OAIHIUSubscriptionNotification::is_event_Valid() const{
    return m_event_isValid;
}

QString OAIHIUSubscriptionNotification::getRequestId() const {
    return m_request_id;
}
void OAIHIUSubscriptionNotification::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIHIUSubscriptionNotification::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIHIUSubscriptionNotification::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QDateTime OAIHIUSubscriptionNotification::getTimestamp() const {
    return m_timestamp;
}
void OAIHIUSubscriptionNotification::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIHIUSubscriptionNotification::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIHIUSubscriptionNotification::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIHIUSubscriptionNotification::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_event.isSet()) {
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

bool OAIHIUSubscriptionNotification::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_event_isValid && m_request_id_isValid && m_timestamp_isValid && true;
}

} // namespace OpenAPI
