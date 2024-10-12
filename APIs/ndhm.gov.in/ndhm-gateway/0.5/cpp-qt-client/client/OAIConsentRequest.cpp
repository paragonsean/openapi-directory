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

#include "OAIConsentRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConsentRequest::OAIConsentRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConsentRequest::OAIConsentRequest() {
    this->initializeModel();
}

OAIConsentRequest::~OAIConsentRequest() {}

void OAIConsentRequest::initializeModel() {

    m_consent_isSet = false;
    m_consent_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIConsentRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConsentRequest::fromJsonObject(QJsonObject json) {

    m_consent_isValid = ::OpenAPI::fromJsonValue(m_consent, json[QString("consent")]);
    m_consent_isSet = !json[QString("consent")].isNull() && m_consent_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIConsentRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConsentRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_consent.isSet()) {
        obj.insert(QString("consent"), ::OpenAPI::toJsonValue(m_consent));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

OAIConsentRequest_consent OAIConsentRequest::getConsent() const {
    return m_consent;
}
void OAIConsentRequest::setConsent(const OAIConsentRequest_consent &consent) {
    m_consent = consent;
    m_consent_isSet = true;
}

bool OAIConsentRequest::is_consent_Set() const{
    return m_consent_isSet;
}

bool OAIConsentRequest::is_consent_Valid() const{
    return m_consent_isValid;
}

QString OAIConsentRequest::getRequestId() const {
    return m_request_id;
}
void OAIConsentRequest::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIConsentRequest::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIConsentRequest::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QDateTime OAIConsentRequest::getTimestamp() const {
    return m_timestamp;
}
void OAIConsentRequest::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIConsentRequest::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIConsentRequest::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIConsentRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_consent.isSet()) {
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

bool OAIConsentRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_consent_isValid && m_request_id_isValid && m_timestamp_isValid && true;
}

} // namespace OpenAPI
