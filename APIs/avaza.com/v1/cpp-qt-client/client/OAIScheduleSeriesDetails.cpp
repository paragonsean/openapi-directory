/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIScheduleSeriesDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIScheduleSeriesDetails::OAIScheduleSeriesDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIScheduleSeriesDetails::OAIScheduleSeriesDetails() {
    this->initializeModel();
}

OAIScheduleSeriesDetails::~OAIScheduleSeriesDetails() {}

void OAIScheduleSeriesDetails::initializeModel() {

    m_account_idfk_isSet = false;
    m_account_idfk_isValid = false;

    m_company_idfk_isSet = false;
    m_company_idfk_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_updated_isSet = false;
    m_date_updated_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_firstname_isSet = false;
    m_firstname_isValid = false;

    m_hours_per_day_isSet = false;
    m_hours_per_day_isValid = false;

    m_lastname_isSet = false;
    m_lastname_isValid = false;

    m_leave_type_idfk_isSet = false;
    m_leave_type_idfk_isValid = false;

    m_leave_type_name_isSet = false;
    m_leave_type_name_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_project_idfk_isSet = false;
    m_project_idfk_isValid = false;

    m_project_title_isSet = false;
    m_project_title_isValid = false;

    m_schedule_on_days_off_isSet = false;
    m_schedule_on_days_off_isValid = false;

    m_schedule_series_id_isSet = false;
    m_schedule_series_id_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_task_idfk_isSet = false;
    m_task_idfk_isValid = false;

    m_task_title_isSet = false;
    m_task_title_isValid = false;

    m_time_sheet_category_idfk_isSet = false;
    m_time_sheet_category_idfk_isValid = false;

    m_time_sheet_category_name_isSet = false;
    m_time_sheet_category_name_isValid = false;

    m_total_duration_isSet = false;
    m_total_duration_isValid = false;

    m_updated_by_user_idfk_isSet = false;
    m_updated_by_user_idfk_isValid = false;

    m_user_idfk_isSet = false;
    m_user_idfk_isValid = false;
}

void OAIScheduleSeriesDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIScheduleSeriesDetails::fromJsonObject(QJsonObject json) {

    m_account_idfk_isValid = ::OpenAPI::fromJsonValue(m_account_idfk, json[QString("AccountIDFK")]);
    m_account_idfk_isSet = !json[QString("AccountIDFK")].isNull() && m_account_idfk_isValid;

    m_company_idfk_isValid = ::OpenAPI::fromJsonValue(m_company_idfk, json[QString("CompanyIDFK")]);
    m_company_idfk_isSet = !json[QString("CompanyIDFK")].isNull() && m_company_idfk_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("CompanyName")]);
    m_company_name_isSet = !json[QString("CompanyName")].isNull() && m_company_name_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("DateCreated")]);
    m_date_created_isSet = !json[QString("DateCreated")].isNull() && m_date_created_isValid;

    m_date_updated_isValid = ::OpenAPI::fromJsonValue(m_date_updated, json[QString("DateUpdated")]);
    m_date_updated_isSet = !json[QString("DateUpdated")].isNull() && m_date_updated_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("EndDate")]);
    m_end_date_isSet = !json[QString("EndDate")].isNull() && m_end_date_isValid;

    m_firstname_isValid = ::OpenAPI::fromJsonValue(m_firstname, json[QString("Firstname")]);
    m_firstname_isSet = !json[QString("Firstname")].isNull() && m_firstname_isValid;

    m_hours_per_day_isValid = ::OpenAPI::fromJsonValue(m_hours_per_day, json[QString("HoursPerDay")]);
    m_hours_per_day_isSet = !json[QString("HoursPerDay")].isNull() && m_hours_per_day_isValid;

    m_lastname_isValid = ::OpenAPI::fromJsonValue(m_lastname, json[QString("Lastname")]);
    m_lastname_isSet = !json[QString("Lastname")].isNull() && m_lastname_isValid;

    m_leave_type_idfk_isValid = ::OpenAPI::fromJsonValue(m_leave_type_idfk, json[QString("LeaveTypeIDFK")]);
    m_leave_type_idfk_isSet = !json[QString("LeaveTypeIDFK")].isNull() && m_leave_type_idfk_isValid;

    m_leave_type_name_isValid = ::OpenAPI::fromJsonValue(m_leave_type_name, json[QString("LeaveTypeName")]);
    m_leave_type_name_isSet = !json[QString("LeaveTypeName")].isNull() && m_leave_type_name_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("Notes")]);
    m_notes_isSet = !json[QString("Notes")].isNull() && m_notes_isValid;

    m_project_idfk_isValid = ::OpenAPI::fromJsonValue(m_project_idfk, json[QString("ProjectIDFK")]);
    m_project_idfk_isSet = !json[QString("ProjectIDFK")].isNull() && m_project_idfk_isValid;

    m_project_title_isValid = ::OpenAPI::fromJsonValue(m_project_title, json[QString("ProjectTitle")]);
    m_project_title_isSet = !json[QString("ProjectTitle")].isNull() && m_project_title_isValid;

    m_schedule_on_days_off_isValid = ::OpenAPI::fromJsonValue(m_schedule_on_days_off, json[QString("ScheduleOnDaysOff")]);
    m_schedule_on_days_off_isSet = !json[QString("ScheduleOnDaysOff")].isNull() && m_schedule_on_days_off_isValid;

    m_schedule_series_id_isValid = ::OpenAPI::fromJsonValue(m_schedule_series_id, json[QString("ScheduleSeriesID")]);
    m_schedule_series_id_isSet = !json[QString("ScheduleSeriesID")].isNull() && m_schedule_series_id_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("StartDate")]);
    m_start_date_isSet = !json[QString("StartDate")].isNull() && m_start_date_isValid;

    m_task_idfk_isValid = ::OpenAPI::fromJsonValue(m_task_idfk, json[QString("TaskIDFK")]);
    m_task_idfk_isSet = !json[QString("TaskIDFK")].isNull() && m_task_idfk_isValid;

    m_task_title_isValid = ::OpenAPI::fromJsonValue(m_task_title, json[QString("TaskTitle")]);
    m_task_title_isSet = !json[QString("TaskTitle")].isNull() && m_task_title_isValid;

    m_time_sheet_category_idfk_isValid = ::OpenAPI::fromJsonValue(m_time_sheet_category_idfk, json[QString("TimeSheetCategoryIDFK")]);
    m_time_sheet_category_idfk_isSet = !json[QString("TimeSheetCategoryIDFK")].isNull() && m_time_sheet_category_idfk_isValid;

    m_time_sheet_category_name_isValid = ::OpenAPI::fromJsonValue(m_time_sheet_category_name, json[QString("TimeSheetCategoryName")]);
    m_time_sheet_category_name_isSet = !json[QString("TimeSheetCategoryName")].isNull() && m_time_sheet_category_name_isValid;

    m_total_duration_isValid = ::OpenAPI::fromJsonValue(m_total_duration, json[QString("TotalDuration")]);
    m_total_duration_isSet = !json[QString("TotalDuration")].isNull() && m_total_duration_isValid;

    m_updated_by_user_idfk_isValid = ::OpenAPI::fromJsonValue(m_updated_by_user_idfk, json[QString("UpdatedByUserIDFK")]);
    m_updated_by_user_idfk_isSet = !json[QString("UpdatedByUserIDFK")].isNull() && m_updated_by_user_idfk_isValid;

    m_user_idfk_isValid = ::OpenAPI::fromJsonValue(m_user_idfk, json[QString("UserIDFK")]);
    m_user_idfk_isSet = !json[QString("UserIDFK")].isNull() && m_user_idfk_isValid;
}

QString OAIScheduleSeriesDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIScheduleSeriesDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_account_idfk_isSet) {
        obj.insert(QString("AccountIDFK"), ::OpenAPI::toJsonValue(m_account_idfk));
    }
    if (m_company_idfk_isSet) {
        obj.insert(QString("CompanyIDFK"), ::OpenAPI::toJsonValue(m_company_idfk));
    }
    if (m_company_name_isSet) {
        obj.insert(QString("CompanyName"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_date_created_isSet) {
        obj.insert(QString("DateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_date_updated_isSet) {
        obj.insert(QString("DateUpdated"), ::OpenAPI::toJsonValue(m_date_updated));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("EndDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_firstname_isSet) {
        obj.insert(QString("Firstname"), ::OpenAPI::toJsonValue(m_firstname));
    }
    if (m_hours_per_day_isSet) {
        obj.insert(QString("HoursPerDay"), ::OpenAPI::toJsonValue(m_hours_per_day));
    }
    if (m_lastname_isSet) {
        obj.insert(QString("Lastname"), ::OpenAPI::toJsonValue(m_lastname));
    }
    if (m_leave_type_idfk_isSet) {
        obj.insert(QString("LeaveTypeIDFK"), ::OpenAPI::toJsonValue(m_leave_type_idfk));
    }
    if (m_leave_type_name_isSet) {
        obj.insert(QString("LeaveTypeName"), ::OpenAPI::toJsonValue(m_leave_type_name));
    }
    if (m_notes_isSet) {
        obj.insert(QString("Notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_project_idfk_isSet) {
        obj.insert(QString("ProjectIDFK"), ::OpenAPI::toJsonValue(m_project_idfk));
    }
    if (m_project_title_isSet) {
        obj.insert(QString("ProjectTitle"), ::OpenAPI::toJsonValue(m_project_title));
    }
    if (m_schedule_on_days_off_isSet) {
        obj.insert(QString("ScheduleOnDaysOff"), ::OpenAPI::toJsonValue(m_schedule_on_days_off));
    }
    if (m_schedule_series_id_isSet) {
        obj.insert(QString("ScheduleSeriesID"), ::OpenAPI::toJsonValue(m_schedule_series_id));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("StartDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_task_idfk_isSet) {
        obj.insert(QString("TaskIDFK"), ::OpenAPI::toJsonValue(m_task_idfk));
    }
    if (m_task_title_isSet) {
        obj.insert(QString("TaskTitle"), ::OpenAPI::toJsonValue(m_task_title));
    }
    if (m_time_sheet_category_idfk_isSet) {
        obj.insert(QString("TimeSheetCategoryIDFK"), ::OpenAPI::toJsonValue(m_time_sheet_category_idfk));
    }
    if (m_time_sheet_category_name_isSet) {
        obj.insert(QString("TimeSheetCategoryName"), ::OpenAPI::toJsonValue(m_time_sheet_category_name));
    }
    if (m_total_duration_isSet) {
        obj.insert(QString("TotalDuration"), ::OpenAPI::toJsonValue(m_total_duration));
    }
    if (m_updated_by_user_idfk_isSet) {
        obj.insert(QString("UpdatedByUserIDFK"), ::OpenAPI::toJsonValue(m_updated_by_user_idfk));
    }
    if (m_user_idfk_isSet) {
        obj.insert(QString("UserIDFK"), ::OpenAPI::toJsonValue(m_user_idfk));
    }
    return obj;
}

qint32 OAIScheduleSeriesDetails::getAccountIdfk() const {
    return m_account_idfk;
}
void OAIScheduleSeriesDetails::setAccountIdfk(const qint32 &account_idfk) {
    m_account_idfk = account_idfk;
    m_account_idfk_isSet = true;
}

bool OAIScheduleSeriesDetails::is_account_idfk_Set() const{
    return m_account_idfk_isSet;
}

bool OAIScheduleSeriesDetails::is_account_idfk_Valid() const{
    return m_account_idfk_isValid;
}

qint32 OAIScheduleSeriesDetails::getCompanyIdfk() const {
    return m_company_idfk;
}
void OAIScheduleSeriesDetails::setCompanyIdfk(const qint32 &company_idfk) {
    m_company_idfk = company_idfk;
    m_company_idfk_isSet = true;
}

bool OAIScheduleSeriesDetails::is_company_idfk_Set() const{
    return m_company_idfk_isSet;
}

bool OAIScheduleSeriesDetails::is_company_idfk_Valid() const{
    return m_company_idfk_isValid;
}

QString OAIScheduleSeriesDetails::getCompanyName() const {
    return m_company_name;
}
void OAIScheduleSeriesDetails::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAIScheduleSeriesDetails::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAIScheduleSeriesDetails::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QDateTime OAIScheduleSeriesDetails::getDateCreated() const {
    return m_date_created;
}
void OAIScheduleSeriesDetails::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAIScheduleSeriesDetails::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAIScheduleSeriesDetails::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAIScheduleSeriesDetails::getDateUpdated() const {
    return m_date_updated;
}
void OAIScheduleSeriesDetails::setDateUpdated(const QDateTime &date_updated) {
    m_date_updated = date_updated;
    m_date_updated_isSet = true;
}

bool OAIScheduleSeriesDetails::is_date_updated_Set() const{
    return m_date_updated_isSet;
}

bool OAIScheduleSeriesDetails::is_date_updated_Valid() const{
    return m_date_updated_isValid;
}

QDateTime OAIScheduleSeriesDetails::getEndDate() const {
    return m_end_date;
}
void OAIScheduleSeriesDetails::setEndDate(const QDateTime &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIScheduleSeriesDetails::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIScheduleSeriesDetails::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QString OAIScheduleSeriesDetails::getFirstname() const {
    return m_firstname;
}
void OAIScheduleSeriesDetails::setFirstname(const QString &firstname) {
    m_firstname = firstname;
    m_firstname_isSet = true;
}

bool OAIScheduleSeriesDetails::is_firstname_Set() const{
    return m_firstname_isSet;
}

bool OAIScheduleSeriesDetails::is_firstname_Valid() const{
    return m_firstname_isValid;
}

double OAIScheduleSeriesDetails::getHoursPerDay() const {
    return m_hours_per_day;
}
void OAIScheduleSeriesDetails::setHoursPerDay(const double &hours_per_day) {
    m_hours_per_day = hours_per_day;
    m_hours_per_day_isSet = true;
}

bool OAIScheduleSeriesDetails::is_hours_per_day_Set() const{
    return m_hours_per_day_isSet;
}

bool OAIScheduleSeriesDetails::is_hours_per_day_Valid() const{
    return m_hours_per_day_isValid;
}

QString OAIScheduleSeriesDetails::getLastname() const {
    return m_lastname;
}
void OAIScheduleSeriesDetails::setLastname(const QString &lastname) {
    m_lastname = lastname;
    m_lastname_isSet = true;
}

bool OAIScheduleSeriesDetails::is_lastname_Set() const{
    return m_lastname_isSet;
}

bool OAIScheduleSeriesDetails::is_lastname_Valid() const{
    return m_lastname_isValid;
}

qint32 OAIScheduleSeriesDetails::getLeaveTypeIdfk() const {
    return m_leave_type_idfk;
}
void OAIScheduleSeriesDetails::setLeaveTypeIdfk(const qint32 &leave_type_idfk) {
    m_leave_type_idfk = leave_type_idfk;
    m_leave_type_idfk_isSet = true;
}

bool OAIScheduleSeriesDetails::is_leave_type_idfk_Set() const{
    return m_leave_type_idfk_isSet;
}

bool OAIScheduleSeriesDetails::is_leave_type_idfk_Valid() const{
    return m_leave_type_idfk_isValid;
}

QString OAIScheduleSeriesDetails::getLeaveTypeName() const {
    return m_leave_type_name;
}
void OAIScheduleSeriesDetails::setLeaveTypeName(const QString &leave_type_name) {
    m_leave_type_name = leave_type_name;
    m_leave_type_name_isSet = true;
}

bool OAIScheduleSeriesDetails::is_leave_type_name_Set() const{
    return m_leave_type_name_isSet;
}

bool OAIScheduleSeriesDetails::is_leave_type_name_Valid() const{
    return m_leave_type_name_isValid;
}

QString OAIScheduleSeriesDetails::getNotes() const {
    return m_notes;
}
void OAIScheduleSeriesDetails::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIScheduleSeriesDetails::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIScheduleSeriesDetails::is_notes_Valid() const{
    return m_notes_isValid;
}

qint32 OAIScheduleSeriesDetails::getProjectIdfk() const {
    return m_project_idfk;
}
void OAIScheduleSeriesDetails::setProjectIdfk(const qint32 &project_idfk) {
    m_project_idfk = project_idfk;
    m_project_idfk_isSet = true;
}

bool OAIScheduleSeriesDetails::is_project_idfk_Set() const{
    return m_project_idfk_isSet;
}

bool OAIScheduleSeriesDetails::is_project_idfk_Valid() const{
    return m_project_idfk_isValid;
}

QString OAIScheduleSeriesDetails::getProjectTitle() const {
    return m_project_title;
}
void OAIScheduleSeriesDetails::setProjectTitle(const QString &project_title) {
    m_project_title = project_title;
    m_project_title_isSet = true;
}

bool OAIScheduleSeriesDetails::is_project_title_Set() const{
    return m_project_title_isSet;
}

bool OAIScheduleSeriesDetails::is_project_title_Valid() const{
    return m_project_title_isValid;
}

bool OAIScheduleSeriesDetails::isScheduleOnDaysOff() const {
    return m_schedule_on_days_off;
}
void OAIScheduleSeriesDetails::setScheduleOnDaysOff(const bool &schedule_on_days_off) {
    m_schedule_on_days_off = schedule_on_days_off;
    m_schedule_on_days_off_isSet = true;
}

bool OAIScheduleSeriesDetails::is_schedule_on_days_off_Set() const{
    return m_schedule_on_days_off_isSet;
}

bool OAIScheduleSeriesDetails::is_schedule_on_days_off_Valid() const{
    return m_schedule_on_days_off_isValid;
}

qint64 OAIScheduleSeriesDetails::getScheduleSeriesId() const {
    return m_schedule_series_id;
}
void OAIScheduleSeriesDetails::setScheduleSeriesId(const qint64 &schedule_series_id) {
    m_schedule_series_id = schedule_series_id;
    m_schedule_series_id_isSet = true;
}

bool OAIScheduleSeriesDetails::is_schedule_series_id_Set() const{
    return m_schedule_series_id_isSet;
}

bool OAIScheduleSeriesDetails::is_schedule_series_id_Valid() const{
    return m_schedule_series_id_isValid;
}

QDateTime OAIScheduleSeriesDetails::getStartDate() const {
    return m_start_date;
}
void OAIScheduleSeriesDetails::setStartDate(const QDateTime &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIScheduleSeriesDetails::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIScheduleSeriesDetails::is_start_date_Valid() const{
    return m_start_date_isValid;
}

qint32 OAIScheduleSeriesDetails::getTaskIdfk() const {
    return m_task_idfk;
}
void OAIScheduleSeriesDetails::setTaskIdfk(const qint32 &task_idfk) {
    m_task_idfk = task_idfk;
    m_task_idfk_isSet = true;
}

bool OAIScheduleSeriesDetails::is_task_idfk_Set() const{
    return m_task_idfk_isSet;
}

bool OAIScheduleSeriesDetails::is_task_idfk_Valid() const{
    return m_task_idfk_isValid;
}

QString OAIScheduleSeriesDetails::getTaskTitle() const {
    return m_task_title;
}
void OAIScheduleSeriesDetails::setTaskTitle(const QString &task_title) {
    m_task_title = task_title;
    m_task_title_isSet = true;
}

bool OAIScheduleSeriesDetails::is_task_title_Set() const{
    return m_task_title_isSet;
}

bool OAIScheduleSeriesDetails::is_task_title_Valid() const{
    return m_task_title_isValid;
}

qint32 OAIScheduleSeriesDetails::getTimeSheetCategoryIdfk() const {
    return m_time_sheet_category_idfk;
}
void OAIScheduleSeriesDetails::setTimeSheetCategoryIdfk(const qint32 &time_sheet_category_idfk) {
    m_time_sheet_category_idfk = time_sheet_category_idfk;
    m_time_sheet_category_idfk_isSet = true;
}

bool OAIScheduleSeriesDetails::is_time_sheet_category_idfk_Set() const{
    return m_time_sheet_category_idfk_isSet;
}

bool OAIScheduleSeriesDetails::is_time_sheet_category_idfk_Valid() const{
    return m_time_sheet_category_idfk_isValid;
}

QString OAIScheduleSeriesDetails::getTimeSheetCategoryName() const {
    return m_time_sheet_category_name;
}
void OAIScheduleSeriesDetails::setTimeSheetCategoryName(const QString &time_sheet_category_name) {
    m_time_sheet_category_name = time_sheet_category_name;
    m_time_sheet_category_name_isSet = true;
}

bool OAIScheduleSeriesDetails::is_time_sheet_category_name_Set() const{
    return m_time_sheet_category_name_isSet;
}

bool OAIScheduleSeriesDetails::is_time_sheet_category_name_Valid() const{
    return m_time_sheet_category_name_isValid;
}

double OAIScheduleSeriesDetails::getTotalDuration() const {
    return m_total_duration;
}
void OAIScheduleSeriesDetails::setTotalDuration(const double &total_duration) {
    m_total_duration = total_duration;
    m_total_duration_isSet = true;
}

bool OAIScheduleSeriesDetails::is_total_duration_Set() const{
    return m_total_duration_isSet;
}

bool OAIScheduleSeriesDetails::is_total_duration_Valid() const{
    return m_total_duration_isValid;
}

qint32 OAIScheduleSeriesDetails::getUpdatedByUserIdfk() const {
    return m_updated_by_user_idfk;
}
void OAIScheduleSeriesDetails::setUpdatedByUserIdfk(const qint32 &updated_by_user_idfk) {
    m_updated_by_user_idfk = updated_by_user_idfk;
    m_updated_by_user_idfk_isSet = true;
}

bool OAIScheduleSeriesDetails::is_updated_by_user_idfk_Set() const{
    return m_updated_by_user_idfk_isSet;
}

bool OAIScheduleSeriesDetails::is_updated_by_user_idfk_Valid() const{
    return m_updated_by_user_idfk_isValid;
}

qint32 OAIScheduleSeriesDetails::getUserIdfk() const {
    return m_user_idfk;
}
void OAIScheduleSeriesDetails::setUserIdfk(const qint32 &user_idfk) {
    m_user_idfk = user_idfk;
    m_user_idfk_isSet = true;
}

bool OAIScheduleSeriesDetails::is_user_idfk_Set() const{
    return m_user_idfk_isSet;
}

bool OAIScheduleSeriesDetails::is_user_idfk_Valid() const{
    return m_user_idfk_isValid;
}

bool OAIScheduleSeriesDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_firstname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hours_per_day_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lastname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_leave_type_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_leave_type_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_on_days_off_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_series_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_sheet_category_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_sheet_category_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_by_user_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIScheduleSeriesDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
