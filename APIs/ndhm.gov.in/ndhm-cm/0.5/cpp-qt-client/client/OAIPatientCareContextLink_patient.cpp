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

#include "OAIPatientCareContextLink_patient.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientCareContextLink_patient::OAIPatientCareContextLink_patient(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientCareContextLink_patient::OAIPatientCareContextLink_patient() {
    this->initializeModel();
}

OAIPatientCareContextLink_patient::~OAIPatientCareContextLink_patient() {}

void OAIPatientCareContextLink_patient::initializeModel() {

    m_care_contexts_isSet = false;
    m_care_contexts_isValid = false;

    m_display_isSet = false;
    m_display_isValid = false;

    m_reference_number_isSet = false;
    m_reference_number_isValid = false;
}

void OAIPatientCareContextLink_patient::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientCareContextLink_patient::fromJsonObject(QJsonObject json) {

    m_care_contexts_isValid = ::OpenAPI::fromJsonValue(m_care_contexts, json[QString("careContexts")]);
    m_care_contexts_isSet = !json[QString("careContexts")].isNull() && m_care_contexts_isValid;

    m_display_isValid = ::OpenAPI::fromJsonValue(m_display, json[QString("display")]);
    m_display_isSet = !json[QString("display")].isNull() && m_display_isValid;

    m_reference_number_isValid = ::OpenAPI::fromJsonValue(m_reference_number, json[QString("referenceNumber")]);
    m_reference_number_isSet = !json[QString("referenceNumber")].isNull() && m_reference_number_isValid;
}

QString OAIPatientCareContextLink_patient::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientCareContextLink_patient::asJsonObject() const {
    QJsonObject obj;
    if (m_care_contexts.size() > 0) {
        obj.insert(QString("careContexts"), ::OpenAPI::toJsonValue(m_care_contexts));
    }
    if (m_display_isSet) {
        obj.insert(QString("display"), ::OpenAPI::toJsonValue(m_display));
    }
    if (m_reference_number_isSet) {
        obj.insert(QString("referenceNumber"), ::OpenAPI::toJsonValue(m_reference_number));
    }
    return obj;
}

QList<OAICareContextRepresentation> OAIPatientCareContextLink_patient::getCareContexts() const {
    return m_care_contexts;
}
void OAIPatientCareContextLink_patient::setCareContexts(const QList<OAICareContextRepresentation> &care_contexts) {
    m_care_contexts = care_contexts;
    m_care_contexts_isSet = true;
}

bool OAIPatientCareContextLink_patient::is_care_contexts_Set() const{
    return m_care_contexts_isSet;
}

bool OAIPatientCareContextLink_patient::is_care_contexts_Valid() const{
    return m_care_contexts_isValid;
}

QString OAIPatientCareContextLink_patient::getDisplay() const {
    return m_display;
}
void OAIPatientCareContextLink_patient::setDisplay(const QString &display) {
    m_display = display;
    m_display_isSet = true;
}

bool OAIPatientCareContextLink_patient::is_display_Set() const{
    return m_display_isSet;
}

bool OAIPatientCareContextLink_patient::is_display_Valid() const{
    return m_display_isValid;
}

QString OAIPatientCareContextLink_patient::getReferenceNumber() const {
    return m_reference_number;
}
void OAIPatientCareContextLink_patient::setReferenceNumber(const QString &reference_number) {
    m_reference_number = reference_number;
    m_reference_number_isSet = true;
}

bool OAIPatientCareContextLink_patient::is_reference_number_Set() const{
    return m_reference_number_isSet;
}

bool OAIPatientCareContextLink_patient::is_reference_number_Valid() const{
    return m_reference_number_isValid;
}

bool OAIPatientCareContextLink_patient::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_care_contexts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_number_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientCareContextLink_patient::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_care_contexts_isValid && m_display_isValid && m_reference_number_isValid && true;
}

} // namespace OpenAPI
