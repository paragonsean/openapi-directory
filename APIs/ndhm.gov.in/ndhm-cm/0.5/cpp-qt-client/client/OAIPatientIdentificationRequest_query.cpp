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

#include "OAIPatientIdentificationRequest_query.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientIdentificationRequest_query::OAIPatientIdentificationRequest_query(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientIdentificationRequest_query::OAIPatientIdentificationRequest_query() {
    this->initializeModel();
}

OAIPatientIdentificationRequest_query::~OAIPatientIdentificationRequest_query() {}

void OAIPatientIdentificationRequest_query::initializeModel() {

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_requester_isSet = false;
    m_requester_isValid = false;
}

void OAIPatientIdentificationRequest_query::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientIdentificationRequest_query::fromJsonObject(QJsonObject json) {

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_requester_isValid = ::OpenAPI::fromJsonValue(m_requester, json[QString("requester")]);
    m_requester_isSet = !json[QString("requester")].isNull() && m_requester_isValid;
}

QString OAIPatientIdentificationRequest_query::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientIdentificationRequest_query::asJsonObject() const {
    QJsonObject obj;
    if (m_patient.isSet()) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
    }
    if (m_requester.isSet()) {
        obj.insert(QString("requester"), ::OpenAPI::toJsonValue(m_requester));
    }
    return obj;
}

OAIPatientIdentificationRequest_query_patient OAIPatientIdentificationRequest_query::getPatient() const {
    return m_patient;
}
void OAIPatientIdentificationRequest_query::setPatient(const OAIPatientIdentificationRequest_query_patient &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIPatientIdentificationRequest_query::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIPatientIdentificationRequest_query::is_patient_Valid() const{
    return m_patient_isValid;
}

OAIHealthInformationNotification_notification_notifier OAIPatientIdentificationRequest_query::getRequester() const {
    return m_requester;
}
void OAIPatientIdentificationRequest_query::setRequester(const OAIHealthInformationNotification_notification_notifier &requester) {
    m_requester = requester;
    m_requester_isSet = true;
}

bool OAIPatientIdentificationRequest_query::is_requester_Set() const{
    return m_requester_isSet;
}

bool OAIPatientIdentificationRequest_query::is_requester_Valid() const{
    return m_requester_isValid;
}

bool OAIPatientIdentificationRequest_query::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_patient.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_requester.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientIdentificationRequest_query::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_patient_isValid && m_requester_isValid && true;
}

} // namespace OpenAPI
