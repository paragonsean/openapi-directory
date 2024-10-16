/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITaskDetailVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITaskDetailVO::OAITaskDetailVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITaskDetailVO::OAITaskDetailVO() {
    this->initializeModel();
}

OAITaskDetailVO::~OAITaskDetailVO() {}

void OAITaskDetailVO::initializeModel() {

    m_actual_duration_isSet = false;
    m_actual_duration_isValid = false;

    m_actual_end_isSet = false;
    m_actual_end_isValid = false;

    m_actual_hours_isSet = false;
    m_actual_hours_isValid = false;

    m_actual_start_isSet = false;
    m_actual_start_isValid = false;

    m_assign_to_isSet = false;
    m_assign_to_isValid = false;

    m_baseline_duration_isSet = false;
    m_baseline_duration_isValid = false;

    m_baseline_end_date_isSet = false;
    m_baseline_end_date_isValid = false;

    m_baseline_start_date_isSet = false;
    m_baseline_start_date_isValid = false;

    m_comments_isSet = false;
    m_comments_isValid = false;

    m_create_date_isSet = false;
    m_create_date_isValid = false;

    m_creator_workgroup_name_isSet = false;
    m_creator_workgroup_name_isValid = false;

    m_current_duration_isSet = false;
    m_current_duration_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_is_milestone_isSet = false;
    m_is_milestone_isValid = false;

    m_last_updated_by_isSet = false;
    m_last_updated_by_isValid = false;

    m_mod_date_isSet = false;
    m_mod_date_isValid = false;

    m_percent_complete_isSet = false;
    m_percent_complete_isValid = false;

    m_plan_duration_isSet = false;
    m_plan_duration_isValid = false;

    m_plan_end_isSet = false;
    m_plan_end_isValid = false;

    m_plan_start_isSet = false;
    m_plan_start_isValid = false;

    m_priority_isSet = false;
    m_priority_isValid = false;

    m_requested_by_isSet = false;
    m_requested_by_isValid = false;

    m_schedule_code_isSet = false;
    m_schedule_code_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_task_id_isSet = false;
    m_task_id_isValid = false;

    m_task_name_isSet = false;
    m_task_name_isValid = false;

    m_task_type_isSet = false;
    m_task_type_isValid = false;
}

void OAITaskDetailVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITaskDetailVO::fromJsonObject(QJsonObject json) {

    m_actual_duration_isValid = ::OpenAPI::fromJsonValue(m_actual_duration, json[QString("actual_duration")]);
    m_actual_duration_isSet = !json[QString("actual_duration")].isNull() && m_actual_duration_isValid;

    m_actual_end_isValid = ::OpenAPI::fromJsonValue(m_actual_end, json[QString("actual_end")]);
    m_actual_end_isSet = !json[QString("actual_end")].isNull() && m_actual_end_isValid;

    m_actual_hours_isValid = ::OpenAPI::fromJsonValue(m_actual_hours, json[QString("actual_hours")]);
    m_actual_hours_isSet = !json[QString("actual_hours")].isNull() && m_actual_hours_isValid;

    m_actual_start_isValid = ::OpenAPI::fromJsonValue(m_actual_start, json[QString("actual_start")]);
    m_actual_start_isSet = !json[QString("actual_start")].isNull() && m_actual_start_isValid;

    m_assign_to_isValid = ::OpenAPI::fromJsonValue(m_assign_to, json[QString("assign_to")]);
    m_assign_to_isSet = !json[QString("assign_to")].isNull() && m_assign_to_isValid;

    m_baseline_duration_isValid = ::OpenAPI::fromJsonValue(m_baseline_duration, json[QString("baseline_duration")]);
    m_baseline_duration_isSet = !json[QString("baseline_duration")].isNull() && m_baseline_duration_isValid;

    m_baseline_end_date_isValid = ::OpenAPI::fromJsonValue(m_baseline_end_date, json[QString("baseline_end_date")]);
    m_baseline_end_date_isSet = !json[QString("baseline_end_date")].isNull() && m_baseline_end_date_isValid;

    m_baseline_start_date_isValid = ::OpenAPI::fromJsonValue(m_baseline_start_date, json[QString("baseline_start_date")]);
    m_baseline_start_date_isSet = !json[QString("baseline_start_date")].isNull() && m_baseline_start_date_isValid;

    m_comments_isValid = ::OpenAPI::fromJsonValue(m_comments, json[QString("comments")]);
    m_comments_isSet = !json[QString("comments")].isNull() && m_comments_isValid;

    m_create_date_isValid = ::OpenAPI::fromJsonValue(m_create_date, json[QString("create_date")]);
    m_create_date_isSet = !json[QString("create_date")].isNull() && m_create_date_isValid;

    m_creator_workgroup_name_isValid = ::OpenAPI::fromJsonValue(m_creator_workgroup_name, json[QString("creator_workgroup_name")]);
    m_creator_workgroup_name_isSet = !json[QString("creator_workgroup_name")].isNull() && m_creator_workgroup_name_isValid;

    m_current_duration_isValid = ::OpenAPI::fromJsonValue(m_current_duration, json[QString("current_duration")]);
    m_current_duration_isSet = !json[QString("current_duration")].isNull() && m_current_duration_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_is_milestone_isValid = ::OpenAPI::fromJsonValue(m_is_milestone, json[QString("is_milestone")]);
    m_is_milestone_isSet = !json[QString("is_milestone")].isNull() && m_is_milestone_isValid;

    m_last_updated_by_isValid = ::OpenAPI::fromJsonValue(m_last_updated_by, json[QString("last_updated_by")]);
    m_last_updated_by_isSet = !json[QString("last_updated_by")].isNull() && m_last_updated_by_isValid;

    m_mod_date_isValid = ::OpenAPI::fromJsonValue(m_mod_date, json[QString("mod_date")]);
    m_mod_date_isSet = !json[QString("mod_date")].isNull() && m_mod_date_isValid;

    m_percent_complete_isValid = ::OpenAPI::fromJsonValue(m_percent_complete, json[QString("percent_complete")]);
    m_percent_complete_isSet = !json[QString("percent_complete")].isNull() && m_percent_complete_isValid;

    m_plan_duration_isValid = ::OpenAPI::fromJsonValue(m_plan_duration, json[QString("plan_duration")]);
    m_plan_duration_isSet = !json[QString("plan_duration")].isNull() && m_plan_duration_isValid;

    m_plan_end_isValid = ::OpenAPI::fromJsonValue(m_plan_end, json[QString("plan_end")]);
    m_plan_end_isSet = !json[QString("plan_end")].isNull() && m_plan_end_isValid;

    m_plan_start_isValid = ::OpenAPI::fromJsonValue(m_plan_start, json[QString("plan_start")]);
    m_plan_start_isSet = !json[QString("plan_start")].isNull() && m_plan_start_isValid;

    m_priority_isValid = ::OpenAPI::fromJsonValue(m_priority, json[QString("priority")]);
    m_priority_isSet = !json[QString("priority")].isNull() && m_priority_isValid;

    m_requested_by_isValid = ::OpenAPI::fromJsonValue(m_requested_by, json[QString("requested_by")]);
    m_requested_by_isSet = !json[QString("requested_by")].isNull() && m_requested_by_isValid;

    m_schedule_code_isValid = ::OpenAPI::fromJsonValue(m_schedule_code, json[QString("schedule_code")]);
    m_schedule_code_isSet = !json[QString("schedule_code")].isNull() && m_schedule_code_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_task_id_isValid = ::OpenAPI::fromJsonValue(m_task_id, json[QString("task_id")]);
    m_task_id_isSet = !json[QString("task_id")].isNull() && m_task_id_isValid;

    m_task_name_isValid = ::OpenAPI::fromJsonValue(m_task_name, json[QString("task_name")]);
    m_task_name_isSet = !json[QString("task_name")].isNull() && m_task_name_isValid;

    m_task_type_isValid = ::OpenAPI::fromJsonValue(m_task_type, json[QString("task_type")]);
    m_task_type_isSet = !json[QString("task_type")].isNull() && m_task_type_isValid;
}

QString OAITaskDetailVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITaskDetailVO::asJsonObject() const {
    QJsonObject obj;
    if (m_actual_duration_isSet) {
        obj.insert(QString("actual_duration"), ::OpenAPI::toJsonValue(m_actual_duration));
    }
    if (m_actual_end_isSet) {
        obj.insert(QString("actual_end"), ::OpenAPI::toJsonValue(m_actual_end));
    }
    if (m_actual_hours_isSet) {
        obj.insert(QString("actual_hours"), ::OpenAPI::toJsonValue(m_actual_hours));
    }
    if (m_actual_start_isSet) {
        obj.insert(QString("actual_start"), ::OpenAPI::toJsonValue(m_actual_start));
    }
    if (m_assign_to.isSet()) {
        obj.insert(QString("assign_to"), ::OpenAPI::toJsonValue(m_assign_to));
    }
    if (m_baseline_duration_isSet) {
        obj.insert(QString("baseline_duration"), ::OpenAPI::toJsonValue(m_baseline_duration));
    }
    if (m_baseline_end_date_isSet) {
        obj.insert(QString("baseline_end_date"), ::OpenAPI::toJsonValue(m_baseline_end_date));
    }
    if (m_baseline_start_date_isSet) {
        obj.insert(QString("baseline_start_date"), ::OpenAPI::toJsonValue(m_baseline_start_date));
    }
    if (m_comments_isSet) {
        obj.insert(QString("comments"), ::OpenAPI::toJsonValue(m_comments));
    }
    if (m_create_date_isSet) {
        obj.insert(QString("create_date"), ::OpenAPI::toJsonValue(m_create_date));
    }
    if (m_creator_workgroup_name_isSet) {
        obj.insert(QString("creator_workgroup_name"), ::OpenAPI::toJsonValue(m_creator_workgroup_name));
    }
    if (m_current_duration_isSet) {
        obj.insert(QString("current_duration"), ::OpenAPI::toJsonValue(m_current_duration));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_is_milestone_isSet) {
        obj.insert(QString("is_milestone"), ::OpenAPI::toJsonValue(m_is_milestone));
    }
    if (m_last_updated_by.isSet()) {
        obj.insert(QString("last_updated_by"), ::OpenAPI::toJsonValue(m_last_updated_by));
    }
    if (m_mod_date_isSet) {
        obj.insert(QString("mod_date"), ::OpenAPI::toJsonValue(m_mod_date));
    }
    if (m_percent_complete_isSet) {
        obj.insert(QString("percent_complete"), ::OpenAPI::toJsonValue(m_percent_complete));
    }
    if (m_plan_duration_isSet) {
        obj.insert(QString("plan_duration"), ::OpenAPI::toJsonValue(m_plan_duration));
    }
    if (m_plan_end_isSet) {
        obj.insert(QString("plan_end"), ::OpenAPI::toJsonValue(m_plan_end));
    }
    if (m_plan_start_isSet) {
        obj.insert(QString("plan_start"), ::OpenAPI::toJsonValue(m_plan_start));
    }
    if (m_priority_isSet) {
        obj.insert(QString("priority"), ::OpenAPI::toJsonValue(m_priority));
    }
    if (m_requested_by.isSet()) {
        obj.insert(QString("requested_by"), ::OpenAPI::toJsonValue(m_requested_by));
    }
    if (m_schedule_code_isSet) {
        obj.insert(QString("schedule_code"), ::OpenAPI::toJsonValue(m_schedule_code));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_task_id_isSet) {
        obj.insert(QString("task_id"), ::OpenAPI::toJsonValue(m_task_id));
    }
    if (m_task_name_isSet) {
        obj.insert(QString("task_name"), ::OpenAPI::toJsonValue(m_task_name));
    }
    if (m_task_type_isSet) {
        obj.insert(QString("task_type"), ::OpenAPI::toJsonValue(m_task_type));
    }
    return obj;
}

QJsonValue OAITaskDetailVO::getActualDuration() const {
    return m_actual_duration;
}
void OAITaskDetailVO::setActualDuration(const QJsonValue &actual_duration) {
    m_actual_duration = actual_duration;
    m_actual_duration_isSet = true;
}

bool OAITaskDetailVO::is_actual_duration_Set() const{
    return m_actual_duration_isSet;
}

bool OAITaskDetailVO::is_actual_duration_Valid() const{
    return m_actual_duration_isValid;
}

QDate OAITaskDetailVO::getActualEnd() const {
    return m_actual_end;
}
void OAITaskDetailVO::setActualEnd(const QDate &actual_end) {
    m_actual_end = actual_end;
    m_actual_end_isSet = true;
}

bool OAITaskDetailVO::is_actual_end_Set() const{
    return m_actual_end_isSet;
}

bool OAITaskDetailVO::is_actual_end_Valid() const{
    return m_actual_end_isValid;
}

QJsonValue OAITaskDetailVO::getActualHours() const {
    return m_actual_hours;
}
void OAITaskDetailVO::setActualHours(const QJsonValue &actual_hours) {
    m_actual_hours = actual_hours;
    m_actual_hours_isSet = true;
}

bool OAITaskDetailVO::is_actual_hours_Set() const{
    return m_actual_hours_isSet;
}

bool OAITaskDetailVO::is_actual_hours_Valid() const{
    return m_actual_hours_isValid;
}

QDate OAITaskDetailVO::getActualStart() const {
    return m_actual_start;
}
void OAITaskDetailVO::setActualStart(const QDate &actual_start) {
    m_actual_start = actual_start;
    m_actual_start_isSet = true;
}

bool OAITaskDetailVO::is_actual_start_Set() const{
    return m_actual_start_isSet;
}

bool OAITaskDetailVO::is_actual_start_Valid() const{
    return m_actual_start_isValid;
}

OAIPersonVO OAITaskDetailVO::getAssignTo() const {
    return m_assign_to;
}
void OAITaskDetailVO::setAssignTo(const OAIPersonVO &assign_to) {
    m_assign_to = assign_to;
    m_assign_to_isSet = true;
}

bool OAITaskDetailVO::is_assign_to_Set() const{
    return m_assign_to_isSet;
}

bool OAITaskDetailVO::is_assign_to_Valid() const{
    return m_assign_to_isValid;
}

QJsonValue OAITaskDetailVO::getBaselineDuration() const {
    return m_baseline_duration;
}
void OAITaskDetailVO::setBaselineDuration(const QJsonValue &baseline_duration) {
    m_baseline_duration = baseline_duration;
    m_baseline_duration_isSet = true;
}

bool OAITaskDetailVO::is_baseline_duration_Set() const{
    return m_baseline_duration_isSet;
}

bool OAITaskDetailVO::is_baseline_duration_Valid() const{
    return m_baseline_duration_isValid;
}

QDate OAITaskDetailVO::getBaselineEndDate() const {
    return m_baseline_end_date;
}
void OAITaskDetailVO::setBaselineEndDate(const QDate &baseline_end_date) {
    m_baseline_end_date = baseline_end_date;
    m_baseline_end_date_isSet = true;
}

bool OAITaskDetailVO::is_baseline_end_date_Set() const{
    return m_baseline_end_date_isSet;
}

bool OAITaskDetailVO::is_baseline_end_date_Valid() const{
    return m_baseline_end_date_isValid;
}

QDate OAITaskDetailVO::getBaselineStartDate() const {
    return m_baseline_start_date;
}
void OAITaskDetailVO::setBaselineStartDate(const QDate &baseline_start_date) {
    m_baseline_start_date = baseline_start_date;
    m_baseline_start_date_isSet = true;
}

bool OAITaskDetailVO::is_baseline_start_date_Set() const{
    return m_baseline_start_date_isSet;
}

bool OAITaskDetailVO::is_baseline_start_date_Valid() const{
    return m_baseline_start_date_isValid;
}

QString OAITaskDetailVO::getComments() const {
    return m_comments;
}
void OAITaskDetailVO::setComments(const QString &comments) {
    m_comments = comments;
    m_comments_isSet = true;
}

bool OAITaskDetailVO::is_comments_Set() const{
    return m_comments_isSet;
}

bool OAITaskDetailVO::is_comments_Valid() const{
    return m_comments_isValid;
}

QDate OAITaskDetailVO::getCreateDate() const {
    return m_create_date;
}
void OAITaskDetailVO::setCreateDate(const QDate &create_date) {
    m_create_date = create_date;
    m_create_date_isSet = true;
}

bool OAITaskDetailVO::is_create_date_Set() const{
    return m_create_date_isSet;
}

bool OAITaskDetailVO::is_create_date_Valid() const{
    return m_create_date_isValid;
}

QString OAITaskDetailVO::getCreatorWorkgroupName() const {
    return m_creator_workgroup_name;
}
void OAITaskDetailVO::setCreatorWorkgroupName(const QString &creator_workgroup_name) {
    m_creator_workgroup_name = creator_workgroup_name;
    m_creator_workgroup_name_isSet = true;
}

bool OAITaskDetailVO::is_creator_workgroup_name_Set() const{
    return m_creator_workgroup_name_isSet;
}

bool OAITaskDetailVO::is_creator_workgroup_name_Valid() const{
    return m_creator_workgroup_name_isValid;
}

QJsonValue OAITaskDetailVO::getCurrentDuration() const {
    return m_current_duration;
}
void OAITaskDetailVO::setCurrentDuration(const QJsonValue &current_duration) {
    m_current_duration = current_duration;
    m_current_duration_isSet = true;
}

bool OAITaskDetailVO::is_current_duration_Set() const{
    return m_current_duration_isSet;
}

bool OAITaskDetailVO::is_current_duration_Valid() const{
    return m_current_duration_isValid;
}

QString OAITaskDetailVO::getDescription() const {
    return m_description;
}
void OAITaskDetailVO::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAITaskDetailVO::is_description_Set() const{
    return m_description_isSet;
}

bool OAITaskDetailVO::is_description_Valid() const{
    return m_description_isValid;
}

bool OAITaskDetailVO::isIsMilestone() const {
    return m_is_milestone;
}
void OAITaskDetailVO::setIsMilestone(const bool &is_milestone) {
    m_is_milestone = is_milestone;
    m_is_milestone_isSet = true;
}

bool OAITaskDetailVO::is_is_milestone_Set() const{
    return m_is_milestone_isSet;
}

bool OAITaskDetailVO::is_is_milestone_Valid() const{
    return m_is_milestone_isValid;
}

OAIPersonVO OAITaskDetailVO::getLastUpdatedBy() const {
    return m_last_updated_by;
}
void OAITaskDetailVO::setLastUpdatedBy(const OAIPersonVO &last_updated_by) {
    m_last_updated_by = last_updated_by;
    m_last_updated_by_isSet = true;
}

bool OAITaskDetailVO::is_last_updated_by_Set() const{
    return m_last_updated_by_isSet;
}

bool OAITaskDetailVO::is_last_updated_by_Valid() const{
    return m_last_updated_by_isValid;
}

QDate OAITaskDetailVO::getModDate() const {
    return m_mod_date;
}
void OAITaskDetailVO::setModDate(const QDate &mod_date) {
    m_mod_date = mod_date;
    m_mod_date_isSet = true;
}

bool OAITaskDetailVO::is_mod_date_Set() const{
    return m_mod_date_isSet;
}

bool OAITaskDetailVO::is_mod_date_Valid() const{
    return m_mod_date_isValid;
}

qint32 OAITaskDetailVO::getPercentComplete() const {
    return m_percent_complete;
}
void OAITaskDetailVO::setPercentComplete(const qint32 &percent_complete) {
    m_percent_complete = percent_complete;
    m_percent_complete_isSet = true;
}

bool OAITaskDetailVO::is_percent_complete_Set() const{
    return m_percent_complete_isSet;
}

bool OAITaskDetailVO::is_percent_complete_Valid() const{
    return m_percent_complete_isValid;
}

QJsonValue OAITaskDetailVO::getPlanDuration() const {
    return m_plan_duration;
}
void OAITaskDetailVO::setPlanDuration(const QJsonValue &plan_duration) {
    m_plan_duration = plan_duration;
    m_plan_duration_isSet = true;
}

bool OAITaskDetailVO::is_plan_duration_Set() const{
    return m_plan_duration_isSet;
}

bool OAITaskDetailVO::is_plan_duration_Valid() const{
    return m_plan_duration_isValid;
}

QDate OAITaskDetailVO::getPlanEnd() const {
    return m_plan_end;
}
void OAITaskDetailVO::setPlanEnd(const QDate &plan_end) {
    m_plan_end = plan_end;
    m_plan_end_isSet = true;
}

bool OAITaskDetailVO::is_plan_end_Set() const{
    return m_plan_end_isSet;
}

bool OAITaskDetailVO::is_plan_end_Valid() const{
    return m_plan_end_isValid;
}

QDate OAITaskDetailVO::getPlanStart() const {
    return m_plan_start;
}
void OAITaskDetailVO::setPlanStart(const QDate &plan_start) {
    m_plan_start = plan_start;
    m_plan_start_isSet = true;
}

bool OAITaskDetailVO::is_plan_start_Set() const{
    return m_plan_start_isSet;
}

bool OAITaskDetailVO::is_plan_start_Valid() const{
    return m_plan_start_isValid;
}

QString OAITaskDetailVO::getPriority() const {
    return m_priority;
}
void OAITaskDetailVO::setPriority(const QString &priority) {
    m_priority = priority;
    m_priority_isSet = true;
}

bool OAITaskDetailVO::is_priority_Set() const{
    return m_priority_isSet;
}

bool OAITaskDetailVO::is_priority_Valid() const{
    return m_priority_isValid;
}

OAIPersonVO OAITaskDetailVO::getRequestedBy() const {
    return m_requested_by;
}
void OAITaskDetailVO::setRequestedBy(const OAIPersonVO &requested_by) {
    m_requested_by = requested_by;
    m_requested_by_isSet = true;
}

bool OAITaskDetailVO::is_requested_by_Set() const{
    return m_requested_by_isSet;
}

bool OAITaskDetailVO::is_requested_by_Valid() const{
    return m_requested_by_isValid;
}

QString OAITaskDetailVO::getScheduleCode() const {
    return m_schedule_code;
}
void OAITaskDetailVO::setScheduleCode(const QString &schedule_code) {
    m_schedule_code = schedule_code;
    m_schedule_code_isSet = true;
}

bool OAITaskDetailVO::is_schedule_code_Set() const{
    return m_schedule_code_isSet;
}

bool OAITaskDetailVO::is_schedule_code_Valid() const{
    return m_schedule_code_isValid;
}

QString OAITaskDetailVO::getStatus() const {
    return m_status;
}
void OAITaskDetailVO::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAITaskDetailVO::is_status_Set() const{
    return m_status_isSet;
}

bool OAITaskDetailVO::is_status_Valid() const{
    return m_status_isValid;
}

qint64 OAITaskDetailVO::getTaskId() const {
    return m_task_id;
}
void OAITaskDetailVO::setTaskId(const qint64 &task_id) {
    m_task_id = task_id;
    m_task_id_isSet = true;
}

bool OAITaskDetailVO::is_task_id_Set() const{
    return m_task_id_isSet;
}

bool OAITaskDetailVO::is_task_id_Valid() const{
    return m_task_id_isValid;
}

QString OAITaskDetailVO::getTaskName() const {
    return m_task_name;
}
void OAITaskDetailVO::setTaskName(const QString &task_name) {
    m_task_name = task_name;
    m_task_name_isSet = true;
}

bool OAITaskDetailVO::is_task_name_Set() const{
    return m_task_name_isSet;
}

bool OAITaskDetailVO::is_task_name_Valid() const{
    return m_task_name_isValid;
}

QString OAITaskDetailVO::getTaskType() const {
    return m_task_type;
}
void OAITaskDetailVO::setTaskType(const QString &task_type) {
    m_task_type = task_type;
    m_task_type_isSet = true;
}

bool OAITaskDetailVO::is_task_type_Set() const{
    return m_task_type_isSet;
}

bool OAITaskDetailVO::is_task_type_Valid() const{
    return m_task_type_isValid;
}

bool OAITaskDetailVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_actual_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_actual_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_actual_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_actual_start_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_assign_to.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_baseline_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_baseline_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_baseline_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_create_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creator_workgroup_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_current_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_milestone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_updated_by.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mod_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_percent_complete_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_plan_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_plan_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_plan_start_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_priority_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_requested_by.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITaskDetailVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
