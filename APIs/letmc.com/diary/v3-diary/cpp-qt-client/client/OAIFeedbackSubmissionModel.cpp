/**
 * agentOS API V3, Diary Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-diary
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFeedbackSubmissionModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFeedbackSubmissionModel::OAIFeedbackSubmissionModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFeedbackSubmissionModel::OAIFeedbackSubmissionModel() {
    this->initializeModel();
}

OAIFeedbackSubmissionModel::~OAIFeedbackSubmissionModel() {}

void OAIFeedbackSubmissionModel::initializeModel() {

    m_appointment_id_isSet = false;
    m_appointment_id_isValid = false;

    m_feedback_isSet = false;
    m_feedback_isValid = false;

    m_property_id_isSet = false;
    m_property_id_isValid = false;
}

void OAIFeedbackSubmissionModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFeedbackSubmissionModel::fromJsonObject(QJsonObject json) {

    m_appointment_id_isValid = ::OpenAPI::fromJsonValue(m_appointment_id, json[QString("AppointmentID")]);
    m_appointment_id_isSet = !json[QString("AppointmentID")].isNull() && m_appointment_id_isValid;

    m_feedback_isValid = ::OpenAPI::fromJsonValue(m_feedback, json[QString("Feedback")]);
    m_feedback_isSet = !json[QString("Feedback")].isNull() && m_feedback_isValid;

    m_property_id_isValid = ::OpenAPI::fromJsonValue(m_property_id, json[QString("PropertyID")]);
    m_property_id_isSet = !json[QString("PropertyID")].isNull() && m_property_id_isValid;
}

QString OAIFeedbackSubmissionModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFeedbackSubmissionModel::asJsonObject() const {
    QJsonObject obj;
    if (m_appointment_id_isSet) {
        obj.insert(QString("AppointmentID"), ::OpenAPI::toJsonValue(m_appointment_id));
    }
    if (m_feedback_isSet) {
        obj.insert(QString("Feedback"), ::OpenAPI::toJsonValue(m_feedback));
    }
    if (m_property_id_isSet) {
        obj.insert(QString("PropertyID"), ::OpenAPI::toJsonValue(m_property_id));
    }
    return obj;
}

QString OAIFeedbackSubmissionModel::getAppointmentId() const {
    return m_appointment_id;
}
void OAIFeedbackSubmissionModel::setAppointmentId(const QString &appointment_id) {
    m_appointment_id = appointment_id;
    m_appointment_id_isSet = true;
}

bool OAIFeedbackSubmissionModel::is_appointment_id_Set() const{
    return m_appointment_id_isSet;
}

bool OAIFeedbackSubmissionModel::is_appointment_id_Valid() const{
    return m_appointment_id_isValid;
}

QString OAIFeedbackSubmissionModel::getFeedback() const {
    return m_feedback;
}
void OAIFeedbackSubmissionModel::setFeedback(const QString &feedback) {
    m_feedback = feedback;
    m_feedback_isSet = true;
}

bool OAIFeedbackSubmissionModel::is_feedback_Set() const{
    return m_feedback_isSet;
}

bool OAIFeedbackSubmissionModel::is_feedback_Valid() const{
    return m_feedback_isValid;
}

QString OAIFeedbackSubmissionModel::getPropertyId() const {
    return m_property_id;
}
void OAIFeedbackSubmissionModel::setPropertyId(const QString &property_id) {
    m_property_id = property_id;
    m_property_id_isSet = true;
}

bool OAIFeedbackSubmissionModel::is_property_id_Set() const{
    return m_property_id_isSet;
}

bool OAIFeedbackSubmissionModel::is_property_id_Valid() const{
    return m_property_id_isValid;
}

bool OAIFeedbackSubmissionModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_appointment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_feedback_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_property_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFeedbackSubmissionModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
