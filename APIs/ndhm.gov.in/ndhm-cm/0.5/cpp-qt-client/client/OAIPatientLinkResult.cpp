/**
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPatientLinkResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientLinkResult::OAIPatientLinkResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientLinkResult::OAIPatientLinkResult() {
    this->initializeModel();
}

OAIPatientLinkResult::~OAIPatientLinkResult() {}

void OAIPatientLinkResult::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_resp_isSet = false;
    m_resp_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIPatientLinkResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientLinkResult::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_resp_isValid = ::OpenAPI::fromJsonValue(m_resp, json[QString("resp")]);
    m_resp_isSet = !json[QString("resp")].isNull() && m_resp_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIPatientLinkResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientLinkResult::asJsonObject() const {
    QJsonObject obj;
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_patient.isSet()) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
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

OAIError OAIPatientLinkResult::getError() const {
    return m_error;
}
void OAIPatientLinkResult::setError(const OAIError &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIPatientLinkResult::is_error_Set() const{
    return m_error_isSet;
}

bool OAIPatientLinkResult::is_error_Valid() const{
    return m_error_isValid;
}

OAIPatientLinkResult_patient OAIPatientLinkResult::getPatient() const {
    return m_patient;
}
void OAIPatientLinkResult::setPatient(const OAIPatientLinkResult_patient &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIPatientLinkResult::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIPatientLinkResult::is_patient_Valid() const{
    return m_patient_isValid;
}

QString OAIPatientLinkResult::getRequestId() const {
    return m_request_id;
}
void OAIPatientLinkResult::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIPatientLinkResult::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIPatientLinkResult::is_request_id_Valid() const{
    return m_request_id_isValid;
}

OAIRequestReference OAIPatientLinkResult::getResp() const {
    return m_resp;
}
void OAIPatientLinkResult::setResp(const OAIRequestReference &resp) {
    m_resp = resp;
    m_resp_isSet = true;
}

bool OAIPatientLinkResult::is_resp_Set() const{
    return m_resp_isSet;
}

bool OAIPatientLinkResult::is_resp_Valid() const{
    return m_resp_isValid;
}

QDateTime OAIPatientLinkResult::getTimestamp() const {
    return m_timestamp;
}
void OAIPatientLinkResult::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIPatientLinkResult::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIPatientLinkResult::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIPatientLinkResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient.isSet()) {
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

bool OAIPatientLinkResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_request_id_isValid && m_resp_isValid && m_timestamp_isValid && true;
}

} // namespace OpenAPI
