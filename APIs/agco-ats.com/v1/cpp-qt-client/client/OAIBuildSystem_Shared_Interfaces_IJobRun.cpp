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

#include "OAIBuildSystem_Shared_Interfaces_IJobRun.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuildSystem_Shared_Interfaces_IJobRun::OAIBuildSystem_Shared_Interfaces_IJobRun(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuildSystem_Shared_Interfaces_IJobRun::OAIBuildSystem_Shared_Interfaces_IJobRun() {
    this->initializeModel();
}

OAIBuildSystem_Shared_Interfaces_IJobRun::~OAIBuildSystem_Shared_Interfaces_IJobRun() {}

void OAIBuildSystem_Shared_Interfaces_IJobRun::initializeModel() {

    m_activity_runs_isSet = false;
    m_activity_runs_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_job_id_isSet = false;
    m_job_id_isValid = false;

    m_job_run_id_isSet = false;
    m_job_run_id_isValid = false;

    m_parameters_isSet = false;
    m_parameters_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIBuildSystem_Shared_Interfaces_IJobRun::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuildSystem_Shared_Interfaces_IJobRun::fromJsonObject(QJsonObject json) {

    m_activity_runs_isValid = ::OpenAPI::fromJsonValue(m_activity_runs, json[QString("ActivityRuns")]);
    m_activity_runs_isSet = !json[QString("ActivityRuns")].isNull() && m_activity_runs_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("EndDate")]);
    m_end_date_isSet = !json[QString("EndDate")].isNull() && m_end_date_isValid;

    m_job_id_isValid = ::OpenAPI::fromJsonValue(m_job_id, json[QString("JobID")]);
    m_job_id_isSet = !json[QString("JobID")].isNull() && m_job_id_isValid;

    m_job_run_id_isValid = ::OpenAPI::fromJsonValue(m_job_run_id, json[QString("JobRunID")]);
    m_job_run_id_isSet = !json[QString("JobRunID")].isNull() && m_job_run_id_isValid;

    m_parameters_isValid = ::OpenAPI::fromJsonValue(m_parameters, json[QString("Parameters")]);
    m_parameters_isSet = !json[QString("Parameters")].isNull() && m_parameters_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("StartDate")]);
    m_start_date_isSet = !json[QString("StartDate")].isNull() && m_start_date_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;
}

QString OAIBuildSystem_Shared_Interfaces_IJobRun::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuildSystem_Shared_Interfaces_IJobRun::asJsonObject() const {
    QJsonObject obj;
    if (m_activity_runs.size() > 0) {
        obj.insert(QString("ActivityRuns"), ::OpenAPI::toJsonValue(m_activity_runs));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("EndDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_job_id_isSet) {
        obj.insert(QString("JobID"), ::OpenAPI::toJsonValue(m_job_id));
    }
    if (m_job_run_id_isSet) {
        obj.insert(QString("JobRunID"), ::OpenAPI::toJsonValue(m_job_run_id));
    }
    if (m_parameters.size() > 0) {
        obj.insert(QString("Parameters"), ::OpenAPI::toJsonValue(m_parameters));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("StartDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QList<OAIBuildSystem_Shared_Interfaces_IActivityRun> OAIBuildSystem_Shared_Interfaces_IJobRun::getActivityRuns() const {
    return m_activity_runs;
}
void OAIBuildSystem_Shared_Interfaces_IJobRun::setActivityRuns(const QList<OAIBuildSystem_Shared_Interfaces_IActivityRun> &activity_runs) {
    m_activity_runs = activity_runs;
    m_activity_runs_isSet = true;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_activity_runs_Set() const{
    return m_activity_runs_isSet;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_activity_runs_Valid() const{
    return m_activity_runs_isValid;
}

QDateTime OAIBuildSystem_Shared_Interfaces_IJobRun::getEndDate() const {
    return m_end_date;
}
void OAIBuildSystem_Shared_Interfaces_IJobRun::setEndDate(const QDateTime &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_end_date_Valid() const{
    return m_end_date_isValid;
}

qint32 OAIBuildSystem_Shared_Interfaces_IJobRun::getJobId() const {
    return m_job_id;
}
void OAIBuildSystem_Shared_Interfaces_IJobRun::setJobId(const qint32 &job_id) {
    m_job_id = job_id;
    m_job_id_isSet = true;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_job_id_Set() const{
    return m_job_id_isSet;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_job_id_Valid() const{
    return m_job_id_isValid;
}

qint32 OAIBuildSystem_Shared_Interfaces_IJobRun::getJobRunId() const {
    return m_job_run_id;
}
void OAIBuildSystem_Shared_Interfaces_IJobRun::setJobRunId(const qint32 &job_run_id) {
    m_job_run_id = job_run_id;
    m_job_run_id_isSet = true;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_job_run_id_Set() const{
    return m_job_run_id_isSet;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_job_run_id_Valid() const{
    return m_job_run_id_isValid;
}

QList<OAIBuildSystem_Shared_Interfaces_IParameterValue> OAIBuildSystem_Shared_Interfaces_IJobRun::getParameters() const {
    return m_parameters;
}
void OAIBuildSystem_Shared_Interfaces_IJobRun::setParameters(const QList<OAIBuildSystem_Shared_Interfaces_IParameterValue> &parameters) {
    m_parameters = parameters;
    m_parameters_isSet = true;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_parameters_Set() const{
    return m_parameters_isSet;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_parameters_Valid() const{
    return m_parameters_isValid;
}

QDateTime OAIBuildSystem_Shared_Interfaces_IJobRun::getStartDate() const {
    return m_start_date;
}
void OAIBuildSystem_Shared_Interfaces_IJobRun::setStartDate(const QDateTime &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_start_date_Valid() const{
    return m_start_date_isValid;
}

QString OAIBuildSystem_Shared_Interfaces_IJobRun::getStatus() const {
    return m_status;
}
void OAIBuildSystem_Shared_Interfaces_IJobRun::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_status_Set() const{
    return m_status_isSet;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIBuildSystem_Shared_Interfaces_IJobRun::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_activity_runs.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_run_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parameters.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
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

bool OAIBuildSystem_Shared_Interfaces_IJobRun::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
