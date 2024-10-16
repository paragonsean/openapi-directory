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

#include "OAIDataSubjectRightUpdateStatusOperation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDataSubjectRightUpdateStatusOperation::OAIDataSubjectRightUpdateStatusOperation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDataSubjectRightUpdateStatusOperation::OAIDataSubjectRightUpdateStatusOperation() {
    this->initializeModel();
}

OAIDataSubjectRightUpdateStatusOperation::~OAIDataSubjectRightUpdateStatusOperation() {}

void OAIDataSubjectRightUpdateStatusOperation::initializeModel() {

    m_participant_data_isSet = false;
    m_participant_data_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIDataSubjectRightUpdateStatusOperation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDataSubjectRightUpdateStatusOperation::fromJsonObject(QJsonObject json) {

    m_participant_data_isValid = ::OpenAPI::fromJsonValue(m_participant_data, json[QString("participantData")]);
    m_participant_data_isSet = !json[QString("participantData")].isNull() && m_participant_data_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIDataSubjectRightUpdateStatusOperation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDataSubjectRightUpdateStatusOperation::asJsonObject() const {
    QJsonObject obj;
    if (m_participant_data_isSet) {
        obj.insert(QString("participantData"), ::OpenAPI::toJsonValue(m_participant_data));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIDataSubjectRightUpdateStatusOperation::getParticipantData() const {
    return m_participant_data;
}
void OAIDataSubjectRightUpdateStatusOperation::setParticipantData(const QString &participant_data) {
    m_participant_data = participant_data;
    m_participant_data_isSet = true;
}

bool OAIDataSubjectRightUpdateStatusOperation::is_participant_data_Set() const{
    return m_participant_data_isSet;
}

bool OAIDataSubjectRightUpdateStatusOperation::is_participant_data_Valid() const{
    return m_participant_data_isValid;
}

QString OAIDataSubjectRightUpdateStatusOperation::getRequestId() const {
    return m_request_id;
}
void OAIDataSubjectRightUpdateStatusOperation::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIDataSubjectRightUpdateStatusOperation::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIDataSubjectRightUpdateStatusOperation::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QString OAIDataSubjectRightUpdateStatusOperation::getStatus() const {
    return m_status;
}
void OAIDataSubjectRightUpdateStatusOperation::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIDataSubjectRightUpdateStatusOperation::is_status_Set() const{
    return m_status_isSet;
}

bool OAIDataSubjectRightUpdateStatusOperation::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIDataSubjectRightUpdateStatusOperation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_participant_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
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

bool OAIDataSubjectRightUpdateStatusOperation::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_request_id_isValid && m_status_isValid && true;
}

} // namespace OpenAPI
