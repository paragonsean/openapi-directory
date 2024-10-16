/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBuildSystem_Shared_DTO_ActivityRunStatus.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuildSystem_Shared_DTO_ActivityRunStatus::OAIBuildSystem_Shared_DTO_ActivityRunStatus(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuildSystem_Shared_DTO_ActivityRunStatus::OAIBuildSystem_Shared_DTO_ActivityRunStatus() {
    this->initializeModel();
}

OAIBuildSystem_Shared_DTO_ActivityRunStatus::~OAIBuildSystem_Shared_DTO_ActivityRunStatus() {}

void OAIBuildSystem_Shared_DTO_ActivityRunStatus::initializeModel() {

    m_current_step_isSet = false;
    m_current_step_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_step_progress_isSet = false;
    m_step_progress_isValid = false;

    m_step_status_isSet = false;
    m_step_status_isValid = false;
}

void OAIBuildSystem_Shared_DTO_ActivityRunStatus::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuildSystem_Shared_DTO_ActivityRunStatus::fromJsonObject(QJsonObject json) {

    m_current_step_isValid = ::OpenAPI::fromJsonValue(m_current_step, json[QString("CurrentStep")]);
    m_current_step_isSet = !json[QString("CurrentStep")].isNull() && m_current_step_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;

    m_step_progress_isValid = ::OpenAPI::fromJsonValue(m_step_progress, json[QString("StepProgress")]);
    m_step_progress_isSet = !json[QString("StepProgress")].isNull() && m_step_progress_isValid;

    m_step_status_isValid = ::OpenAPI::fromJsonValue(m_step_status, json[QString("StepStatus")]);
    m_step_status_isSet = !json[QString("StepStatus")].isNull() && m_step_status_isValid;
}

QString OAIBuildSystem_Shared_DTO_ActivityRunStatus::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuildSystem_Shared_DTO_ActivityRunStatus::asJsonObject() const {
    QJsonObject obj;
    if (m_current_step_isSet) {
        obj.insert(QString("CurrentStep"), ::OpenAPI::toJsonValue(m_current_step));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_step_progress_isSet) {
        obj.insert(QString("StepProgress"), ::OpenAPI::toJsonValue(m_step_progress));
    }
    if (m_step_status_isSet) {
        obj.insert(QString("StepStatus"), ::OpenAPI::toJsonValue(m_step_status));
    }
    return obj;
}

qint32 OAIBuildSystem_Shared_DTO_ActivityRunStatus::getCurrentStep() const {
    return m_current_step;
}
void OAIBuildSystem_Shared_DTO_ActivityRunStatus::setCurrentStep(const qint32 &current_step) {
    m_current_step = current_step;
    m_current_step_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::is_current_step_Set() const{
    return m_current_step_isSet;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::is_current_step_Valid() const{
    return m_current_step_isValid;
}

QString OAIBuildSystem_Shared_DTO_ActivityRunStatus::getStatus() const {
    return m_status;
}
void OAIBuildSystem_Shared_DTO_ActivityRunStatus::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::is_status_Set() const{
    return m_status_isSet;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::is_status_Valid() const{
    return m_status_isValid;
}

qint32 OAIBuildSystem_Shared_DTO_ActivityRunStatus::getStepProgress() const {
    return m_step_progress;
}
void OAIBuildSystem_Shared_DTO_ActivityRunStatus::setStepProgress(const qint32 &step_progress) {
    m_step_progress = step_progress;
    m_step_progress_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::is_step_progress_Set() const{
    return m_step_progress_isSet;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::is_step_progress_Valid() const{
    return m_step_progress_isValid;
}

QString OAIBuildSystem_Shared_DTO_ActivityRunStatus::getStepStatus() const {
    return m_step_status;
}
void OAIBuildSystem_Shared_DTO_ActivityRunStatus::setStepStatus(const QString &step_status) {
    m_step_status = step_status;
    m_step_status_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::is_step_status_Set() const{
    return m_step_status_isSet;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::is_step_status_Valid() const{
    return m_step_status_isValid;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_current_step_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_step_progress_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_step_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBuildSystem_Shared_DTO_ActivityRunStatus::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
