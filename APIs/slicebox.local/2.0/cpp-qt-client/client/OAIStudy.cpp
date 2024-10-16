/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStudy.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStudy::OAIStudy(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStudy::OAIStudy() {
    this->initializeModel();
}

OAIStudy::~OAIStudy() {}

void OAIStudy::initializeModel() {

    m_accession_number_isSet = false;
    m_accession_number_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_patient_age_isSet = false;
    m_patient_age_isValid = false;

    m_patient_id_isSet = false;
    m_patient_id_isValid = false;

    m_study_date_isSet = false;
    m_study_date_isValid = false;

    m_study_description_isSet = false;
    m_study_description_isValid = false;

    m_study_id_isSet = false;
    m_study_id_isValid = false;

    m_study_instance_uid_isSet = false;
    m_study_instance_uid_isValid = false;
}

void OAIStudy::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStudy::fromJsonObject(QJsonObject json) {

    m_accession_number_isValid = ::OpenAPI::fromJsonValue(m_accession_number, json[QString("accessionNumber")]);
    m_accession_number_isSet = !json[QString("accessionNumber")].isNull() && m_accession_number_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_patient_age_isValid = ::OpenAPI::fromJsonValue(m_patient_age, json[QString("patientAge")]);
    m_patient_age_isSet = !json[QString("patientAge")].isNull() && m_patient_age_isValid;

    m_patient_id_isValid = ::OpenAPI::fromJsonValue(m_patient_id, json[QString("patientId")]);
    m_patient_id_isSet = !json[QString("patientId")].isNull() && m_patient_id_isValid;

    m_study_date_isValid = ::OpenAPI::fromJsonValue(m_study_date, json[QString("studyDate")]);
    m_study_date_isSet = !json[QString("studyDate")].isNull() && m_study_date_isValid;

    m_study_description_isValid = ::OpenAPI::fromJsonValue(m_study_description, json[QString("studyDescription")]);
    m_study_description_isSet = !json[QString("studyDescription")].isNull() && m_study_description_isValid;

    m_study_id_isValid = ::OpenAPI::fromJsonValue(m_study_id, json[QString("studyID")]);
    m_study_id_isSet = !json[QString("studyID")].isNull() && m_study_id_isValid;

    m_study_instance_uid_isValid = ::OpenAPI::fromJsonValue(m_study_instance_uid, json[QString("studyInstanceUID")]);
    m_study_instance_uid_isSet = !json[QString("studyInstanceUID")].isNull() && m_study_instance_uid_isValid;
}

QString OAIStudy::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStudy::asJsonObject() const {
    QJsonObject obj;
    if (m_accession_number.isSet()) {
        obj.insert(QString("accessionNumber"), ::OpenAPI::toJsonValue(m_accession_number));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_patient_age.isSet()) {
        obj.insert(QString("patientAge"), ::OpenAPI::toJsonValue(m_patient_age));
    }
    if (m_patient_id_isSet) {
        obj.insert(QString("patientId"), ::OpenAPI::toJsonValue(m_patient_id));
    }
    if (m_study_date.isSet()) {
        obj.insert(QString("studyDate"), ::OpenAPI::toJsonValue(m_study_date));
    }
    if (m_study_description.isSet()) {
        obj.insert(QString("studyDescription"), ::OpenAPI::toJsonValue(m_study_description));
    }
    if (m_study_id.isSet()) {
        obj.insert(QString("studyID"), ::OpenAPI::toJsonValue(m_study_id));
    }
    if (m_study_instance_uid.isSet()) {
        obj.insert(QString("studyInstanceUID"), ::OpenAPI::toJsonValue(m_study_instance_uid));
    }
    return obj;
}

OAIDicomPropertyValue OAIStudy::getAccessionNumber() const {
    return m_accession_number;
}
void OAIStudy::setAccessionNumber(const OAIDicomPropertyValue &accession_number) {
    m_accession_number = accession_number;
    m_accession_number_isSet = true;
}

bool OAIStudy::is_accession_number_Set() const{
    return m_accession_number_isSet;
}

bool OAIStudy::is_accession_number_Valid() const{
    return m_accession_number_isValid;
}

qint64 OAIStudy::getId() const {
    return m_id;
}
void OAIStudy::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIStudy::is_id_Set() const{
    return m_id_isSet;
}

bool OAIStudy::is_id_Valid() const{
    return m_id_isValid;
}

OAIDicomPropertyValue OAIStudy::getPatientAge() const {
    return m_patient_age;
}
void OAIStudy::setPatientAge(const OAIDicomPropertyValue &patient_age) {
    m_patient_age = patient_age;
    m_patient_age_isSet = true;
}

bool OAIStudy::is_patient_age_Set() const{
    return m_patient_age_isSet;
}

bool OAIStudy::is_patient_age_Valid() const{
    return m_patient_age_isValid;
}

qint64 OAIStudy::getPatientId() const {
    return m_patient_id;
}
void OAIStudy::setPatientId(const qint64 &patient_id) {
    m_patient_id = patient_id;
    m_patient_id_isSet = true;
}

bool OAIStudy::is_patient_id_Set() const{
    return m_patient_id_isSet;
}

bool OAIStudy::is_patient_id_Valid() const{
    return m_patient_id_isValid;
}

OAIDicomPropertyValue OAIStudy::getStudyDate() const {
    return m_study_date;
}
void OAIStudy::setStudyDate(const OAIDicomPropertyValue &study_date) {
    m_study_date = study_date;
    m_study_date_isSet = true;
}

bool OAIStudy::is_study_date_Set() const{
    return m_study_date_isSet;
}

bool OAIStudy::is_study_date_Valid() const{
    return m_study_date_isValid;
}

OAIDicomPropertyValue OAIStudy::getStudyDescription() const {
    return m_study_description;
}
void OAIStudy::setStudyDescription(const OAIDicomPropertyValue &study_description) {
    m_study_description = study_description;
    m_study_description_isSet = true;
}

bool OAIStudy::is_study_description_Set() const{
    return m_study_description_isSet;
}

bool OAIStudy::is_study_description_Valid() const{
    return m_study_description_isValid;
}

OAIDicomPropertyValue OAIStudy::getStudyId() const {
    return m_study_id;
}
void OAIStudy::setStudyId(const OAIDicomPropertyValue &study_id) {
    m_study_id = study_id;
    m_study_id_isSet = true;
}

bool OAIStudy::is_study_id_Set() const{
    return m_study_id_isSet;
}

bool OAIStudy::is_study_id_Valid() const{
    return m_study_id_isValid;
}

OAIDicomPropertyValue OAIStudy::getStudyInstanceUid() const {
    return m_study_instance_uid;
}
void OAIStudy::setStudyInstanceUid(const OAIDicomPropertyValue &study_instance_uid) {
    m_study_instance_uid = study_instance_uid;
    m_study_instance_uid_isSet = true;
}

bool OAIStudy::is_study_instance_uid_Set() const{
    return m_study_instance_uid_isSet;
}

bool OAIStudy::is_study_instance_uid_Valid() const{
    return m_study_instance_uid_isValid;
}

bool OAIStudy::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_accession_number.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_age.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_study_date.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_study_description.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_study_id.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_study_instance_uid.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStudy::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
