/**
 * RecoveryServicesBackupClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAzureIaaSVMJob.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAzureIaaSVMJob::OAIAzureIaaSVMJob(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAzureIaaSVMJob::OAIAzureIaaSVMJob() {
    this->initializeModel();
}

OAIAzureIaaSVMJob::~OAIAzureIaaSVMJob() {}

void OAIAzureIaaSVMJob::initializeModel() {

    m_actions_info_isSet = false;
    m_actions_info_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_error_details_isSet = false;
    m_error_details_isValid = false;

    m_extended_info_isSet = false;
    m_extended_info_isValid = false;

    m_virtual_machine_version_isSet = false;
    m_virtual_machine_version_isValid = false;

    m_activity_id_isSet = false;
    m_activity_id_isValid = false;

    m_backup_management_type_isSet = false;
    m_backup_management_type_isValid = false;

    m_end_time_isSet = false;
    m_end_time_isValid = false;

    m_entity_friendly_name_isSet = false;
    m_entity_friendly_name_isValid = false;

    m_job_type_isSet = false;
    m_job_type_isValid = false;

    m_operation_isSet = false;
    m_operation_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIAzureIaaSVMJob::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAzureIaaSVMJob::fromJsonObject(QJsonObject json) {

    m_actions_info_isValid = ::OpenAPI::fromJsonValue(m_actions_info, json[QString("actionsInfo")]);
    m_actions_info_isSet = !json[QString("actionsInfo")].isNull() && m_actions_info_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_error_details_isValid = ::OpenAPI::fromJsonValue(m_error_details, json[QString("errorDetails")]);
    m_error_details_isSet = !json[QString("errorDetails")].isNull() && m_error_details_isValid;

    m_extended_info_isValid = ::OpenAPI::fromJsonValue(m_extended_info, json[QString("extendedInfo")]);
    m_extended_info_isSet = !json[QString("extendedInfo")].isNull() && m_extended_info_isValid;

    m_virtual_machine_version_isValid = ::OpenAPI::fromJsonValue(m_virtual_machine_version, json[QString("virtualMachineVersion")]);
    m_virtual_machine_version_isSet = !json[QString("virtualMachineVersion")].isNull() && m_virtual_machine_version_isValid;

    m_activity_id_isValid = ::OpenAPI::fromJsonValue(m_activity_id, json[QString("activityId")]);
    m_activity_id_isSet = !json[QString("activityId")].isNull() && m_activity_id_isValid;

    m_backup_management_type_isValid = ::OpenAPI::fromJsonValue(m_backup_management_type, json[QString("backupManagementType")]);
    m_backup_management_type_isSet = !json[QString("backupManagementType")].isNull() && m_backup_management_type_isValid;

    m_end_time_isValid = ::OpenAPI::fromJsonValue(m_end_time, json[QString("endTime")]);
    m_end_time_isSet = !json[QString("endTime")].isNull() && m_end_time_isValid;

    m_entity_friendly_name_isValid = ::OpenAPI::fromJsonValue(m_entity_friendly_name, json[QString("entityFriendlyName")]);
    m_entity_friendly_name_isSet = !json[QString("entityFriendlyName")].isNull() && m_entity_friendly_name_isValid;

    m_job_type_isValid = ::OpenAPI::fromJsonValue(m_job_type, json[QString("jobType")]);
    m_job_type_isSet = !json[QString("jobType")].isNull() && m_job_type_isValid;

    m_operation_isValid = ::OpenAPI::fromJsonValue(m_operation, json[QString("operation")]);
    m_operation_isSet = !json[QString("operation")].isNull() && m_operation_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("startTime")]);
    m_start_time_isSet = !json[QString("startTime")].isNull() && m_start_time_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIAzureIaaSVMJob::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAzureIaaSVMJob::asJsonObject() const {
    QJsonObject obj;
    if (m_actions_info.size() > 0) {
        obj.insert(QString("actionsInfo"), ::OpenAPI::toJsonValue(m_actions_info));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_error_details.size() > 0) {
        obj.insert(QString("errorDetails"), ::OpenAPI::toJsonValue(m_error_details));
    }
    if (m_extended_info.isSet()) {
        obj.insert(QString("extendedInfo"), ::OpenAPI::toJsonValue(m_extended_info));
    }
    if (m_virtual_machine_version_isSet) {
        obj.insert(QString("virtualMachineVersion"), ::OpenAPI::toJsonValue(m_virtual_machine_version));
    }
    if (m_activity_id_isSet) {
        obj.insert(QString("activityId"), ::OpenAPI::toJsonValue(m_activity_id));
    }
    if (m_backup_management_type_isSet) {
        obj.insert(QString("backupManagementType"), ::OpenAPI::toJsonValue(m_backup_management_type));
    }
    if (m_end_time_isSet) {
        obj.insert(QString("endTime"), ::OpenAPI::toJsonValue(m_end_time));
    }
    if (m_entity_friendly_name_isSet) {
        obj.insert(QString("entityFriendlyName"), ::OpenAPI::toJsonValue(m_entity_friendly_name));
    }
    if (m_job_type_isSet) {
        obj.insert(QString("jobType"), ::OpenAPI::toJsonValue(m_job_type));
    }
    if (m_operation_isSet) {
        obj.insert(QString("operation"), ::OpenAPI::toJsonValue(m_operation));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("startTime"), ::OpenAPI::toJsonValue(m_start_time));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QList<QString> OAIAzureIaaSVMJob::getActionsInfo() const {
    return m_actions_info;
}
void OAIAzureIaaSVMJob::setActionsInfo(const QList<QString> &actions_info) {
    m_actions_info = actions_info;
    m_actions_info_isSet = true;
}

bool OAIAzureIaaSVMJob::is_actions_info_Set() const{
    return m_actions_info_isSet;
}

bool OAIAzureIaaSVMJob::is_actions_info_Valid() const{
    return m_actions_info_isValid;
}

QString OAIAzureIaaSVMJob::getDuration() const {
    return m_duration;
}
void OAIAzureIaaSVMJob::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIAzureIaaSVMJob::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIAzureIaaSVMJob::is_duration_Valid() const{
    return m_duration_isValid;
}

QList<OAIAzureIaaSVMErrorInfo> OAIAzureIaaSVMJob::getErrorDetails() const {
    return m_error_details;
}
void OAIAzureIaaSVMJob::setErrorDetails(const QList<OAIAzureIaaSVMErrorInfo> &error_details) {
    m_error_details = error_details;
    m_error_details_isSet = true;
}

bool OAIAzureIaaSVMJob::is_error_details_Set() const{
    return m_error_details_isSet;
}

bool OAIAzureIaaSVMJob::is_error_details_Valid() const{
    return m_error_details_isValid;
}

OAIAzureIaaSVMJobExtendedInfo OAIAzureIaaSVMJob::getExtendedInfo() const {
    return m_extended_info;
}
void OAIAzureIaaSVMJob::setExtendedInfo(const OAIAzureIaaSVMJobExtendedInfo &extended_info) {
    m_extended_info = extended_info;
    m_extended_info_isSet = true;
}

bool OAIAzureIaaSVMJob::is_extended_info_Set() const{
    return m_extended_info_isSet;
}

bool OAIAzureIaaSVMJob::is_extended_info_Valid() const{
    return m_extended_info_isValid;
}

QString OAIAzureIaaSVMJob::getVirtualMachineVersion() const {
    return m_virtual_machine_version;
}
void OAIAzureIaaSVMJob::setVirtualMachineVersion(const QString &virtual_machine_version) {
    m_virtual_machine_version = virtual_machine_version;
    m_virtual_machine_version_isSet = true;
}

bool OAIAzureIaaSVMJob::is_virtual_machine_version_Set() const{
    return m_virtual_machine_version_isSet;
}

bool OAIAzureIaaSVMJob::is_virtual_machine_version_Valid() const{
    return m_virtual_machine_version_isValid;
}

QString OAIAzureIaaSVMJob::getActivityId() const {
    return m_activity_id;
}
void OAIAzureIaaSVMJob::setActivityId(const QString &activity_id) {
    m_activity_id = activity_id;
    m_activity_id_isSet = true;
}

bool OAIAzureIaaSVMJob::is_activity_id_Set() const{
    return m_activity_id_isSet;
}

bool OAIAzureIaaSVMJob::is_activity_id_Valid() const{
    return m_activity_id_isValid;
}

QString OAIAzureIaaSVMJob::getBackupManagementType() const {
    return m_backup_management_type;
}
void OAIAzureIaaSVMJob::setBackupManagementType(const QString &backup_management_type) {
    m_backup_management_type = backup_management_type;
    m_backup_management_type_isSet = true;
}

bool OAIAzureIaaSVMJob::is_backup_management_type_Set() const{
    return m_backup_management_type_isSet;
}

bool OAIAzureIaaSVMJob::is_backup_management_type_Valid() const{
    return m_backup_management_type_isValid;
}

QDateTime OAIAzureIaaSVMJob::getEndTime() const {
    return m_end_time;
}
void OAIAzureIaaSVMJob::setEndTime(const QDateTime &end_time) {
    m_end_time = end_time;
    m_end_time_isSet = true;
}

bool OAIAzureIaaSVMJob::is_end_time_Set() const{
    return m_end_time_isSet;
}

bool OAIAzureIaaSVMJob::is_end_time_Valid() const{
    return m_end_time_isValid;
}

QString OAIAzureIaaSVMJob::getEntityFriendlyName() const {
    return m_entity_friendly_name;
}
void OAIAzureIaaSVMJob::setEntityFriendlyName(const QString &entity_friendly_name) {
    m_entity_friendly_name = entity_friendly_name;
    m_entity_friendly_name_isSet = true;
}

bool OAIAzureIaaSVMJob::is_entity_friendly_name_Set() const{
    return m_entity_friendly_name_isSet;
}

bool OAIAzureIaaSVMJob::is_entity_friendly_name_Valid() const{
    return m_entity_friendly_name_isValid;
}

QString OAIAzureIaaSVMJob::getJobType() const {
    return m_job_type;
}
void OAIAzureIaaSVMJob::setJobType(const QString &job_type) {
    m_job_type = job_type;
    m_job_type_isSet = true;
}

bool OAIAzureIaaSVMJob::is_job_type_Set() const{
    return m_job_type_isSet;
}

bool OAIAzureIaaSVMJob::is_job_type_Valid() const{
    return m_job_type_isValid;
}

QString OAIAzureIaaSVMJob::getOperation() const {
    return m_operation;
}
void OAIAzureIaaSVMJob::setOperation(const QString &operation) {
    m_operation = operation;
    m_operation_isSet = true;
}

bool OAIAzureIaaSVMJob::is_operation_Set() const{
    return m_operation_isSet;
}

bool OAIAzureIaaSVMJob::is_operation_Valid() const{
    return m_operation_isValid;
}

QDateTime OAIAzureIaaSVMJob::getStartTime() const {
    return m_start_time;
}
void OAIAzureIaaSVMJob::setStartTime(const QDateTime &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAIAzureIaaSVMJob::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAIAzureIaaSVMJob::is_start_time_Valid() const{
    return m_start_time_isValid;
}

QString OAIAzureIaaSVMJob::getStatus() const {
    return m_status;
}
void OAIAzureIaaSVMJob::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIAzureIaaSVMJob::is_status_Set() const{
    return m_status_isSet;
}

bool OAIAzureIaaSVMJob::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIAzureIaaSVMJob::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_actions_info.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_details.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_extended_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_virtual_machine_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_activity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_backup_management_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_friendly_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
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

bool OAIAzureIaaSVMJob::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_job_type_isValid && true;
}

} // namespace OpenAPI
