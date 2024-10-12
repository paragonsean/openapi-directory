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

#include "OAIPatientAuthModeQueryRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientAuthModeQueryRequest::OAIPatientAuthModeQueryRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientAuthModeQueryRequest::OAIPatientAuthModeQueryRequest() {
    this->initializeModel();
}

OAIPatientAuthModeQueryRequest::~OAIPatientAuthModeQueryRequest() {}

void OAIPatientAuthModeQueryRequest::initializeModel() {

    m_query_isSet = false;
    m_query_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIPatientAuthModeQueryRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientAuthModeQueryRequest::fromJsonObject(QJsonObject json) {

    m_query_isValid = ::OpenAPI::fromJsonValue(m_query, json[QString("query")]);
    m_query_isSet = !json[QString("query")].isNull() && m_query_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIPatientAuthModeQueryRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientAuthModeQueryRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_query.isSet()) {
        obj.insert(QString("query"), ::OpenAPI::toJsonValue(m_query));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

OAIPatientAuthModeQueryRequest_query OAIPatientAuthModeQueryRequest::getQuery() const {
    return m_query;
}
void OAIPatientAuthModeQueryRequest::setQuery(const OAIPatientAuthModeQueryRequest_query &query) {
    m_query = query;
    m_query_isSet = true;
}

bool OAIPatientAuthModeQueryRequest::is_query_Set() const{
    return m_query_isSet;
}

bool OAIPatientAuthModeQueryRequest::is_query_Valid() const{
    return m_query_isValid;
}

QString OAIPatientAuthModeQueryRequest::getRequestId() const {
    return m_request_id;
}
void OAIPatientAuthModeQueryRequest::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIPatientAuthModeQueryRequest::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIPatientAuthModeQueryRequest::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QDateTime OAIPatientAuthModeQueryRequest::getTimestamp() const {
    return m_timestamp;
}
void OAIPatientAuthModeQueryRequest::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIPatientAuthModeQueryRequest::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIPatientAuthModeQueryRequest::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIPatientAuthModeQueryRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_query.isSet()) {
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

bool OAIPatientAuthModeQueryRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_query_isValid && m_request_id_isValid && m_timestamp_isValid && true;
}

} // namespace OpenAPI
