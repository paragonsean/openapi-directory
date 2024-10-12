/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRunFilter.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRunFilter::OAIRunFilter(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRunFilter::OAIRunFilter() {
    this->initializeModel();
}

OAIRunFilter::~OAIRunFilter() {}

void OAIRunFilter::initializeModel() {

    m_create_time_isSet = false;
    m_create_time_isValid = false;

    m_finish_time_isSet = false;
    m_finish_time_isValid = false;

    m_is_archive_enabled_isSet = false;
    m_is_archive_enabled_isValid = false;

    m_output_image_manifests_isSet = false;
    m_output_image_manifests_isValid = false;

    m_run_id_isSet = false;
    m_run_id_isValid = false;

    m_run_type_isSet = false;
    m_run_type_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_task_name_isSet = false;
    m_task_name_isValid = false;
}

void OAIRunFilter::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRunFilter::fromJsonObject(QJsonObject json) {

    m_create_time_isValid = ::OpenAPI::fromJsonValue(m_create_time, json[QString("createTime")]);
    m_create_time_isSet = !json[QString("createTime")].isNull() && m_create_time_isValid;

    m_finish_time_isValid = ::OpenAPI::fromJsonValue(m_finish_time, json[QString("finishTime")]);
    m_finish_time_isSet = !json[QString("finishTime")].isNull() && m_finish_time_isValid;

    m_is_archive_enabled_isValid = ::OpenAPI::fromJsonValue(m_is_archive_enabled, json[QString("isArchiveEnabled")]);
    m_is_archive_enabled_isSet = !json[QString("isArchiveEnabled")].isNull() && m_is_archive_enabled_isValid;

    m_output_image_manifests_isValid = ::OpenAPI::fromJsonValue(m_output_image_manifests, json[QString("outputImageManifests")]);
    m_output_image_manifests_isSet = !json[QString("outputImageManifests")].isNull() && m_output_image_manifests_isValid;

    m_run_id_isValid = ::OpenAPI::fromJsonValue(m_run_id, json[QString("runId")]);
    m_run_id_isSet = !json[QString("runId")].isNull() && m_run_id_isValid;

    m_run_type_isValid = ::OpenAPI::fromJsonValue(m_run_type, json[QString("runType")]);
    m_run_type_isSet = !json[QString("runType")].isNull() && m_run_type_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_task_name_isValid = ::OpenAPI::fromJsonValue(m_task_name, json[QString("taskName")]);
    m_task_name_isSet = !json[QString("taskName")].isNull() && m_task_name_isValid;
}

QString OAIRunFilter::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRunFilter::asJsonObject() const {
    QJsonObject obj;
    if (m_create_time_isSet) {
        obj.insert(QString("createTime"), ::OpenAPI::toJsonValue(m_create_time));
    }
    if (m_finish_time_isSet) {
        obj.insert(QString("finishTime"), ::OpenAPI::toJsonValue(m_finish_time));
    }
    if (m_is_archive_enabled_isSet) {
        obj.insert(QString("isArchiveEnabled"), ::OpenAPI::toJsonValue(m_is_archive_enabled));
    }
    if (m_output_image_manifests_isSet) {
        obj.insert(QString("outputImageManifests"), ::OpenAPI::toJsonValue(m_output_image_manifests));
    }
    if (m_run_id_isSet) {
        obj.insert(QString("runId"), ::OpenAPI::toJsonValue(m_run_id));
    }
    if (m_run_type_isSet) {
        obj.insert(QString("runType"), ::OpenAPI::toJsonValue(m_run_type));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_task_name_isSet) {
        obj.insert(QString("taskName"), ::OpenAPI::toJsonValue(m_task_name));
    }
    return obj;
}

QDateTime OAIRunFilter::getCreateTime() const {
    return m_create_time;
}
void OAIRunFilter::setCreateTime(const QDateTime &create_time) {
    m_create_time = create_time;
    m_create_time_isSet = true;
}

bool OAIRunFilter::is_create_time_Set() const{
    return m_create_time_isSet;
}

bool OAIRunFilter::is_create_time_Valid() const{
    return m_create_time_isValid;
}

QDateTime OAIRunFilter::getFinishTime() const {
    return m_finish_time;
}
void OAIRunFilter::setFinishTime(const QDateTime &finish_time) {
    m_finish_time = finish_time;
    m_finish_time_isSet = true;
}

bool OAIRunFilter::is_finish_time_Set() const{
    return m_finish_time_isSet;
}

bool OAIRunFilter::is_finish_time_Valid() const{
    return m_finish_time_isValid;
}

bool OAIRunFilter::isIsArchiveEnabled() const {
    return m_is_archive_enabled;
}
void OAIRunFilter::setIsArchiveEnabled(const bool &is_archive_enabled) {
    m_is_archive_enabled = is_archive_enabled;
    m_is_archive_enabled_isSet = true;
}

bool OAIRunFilter::is_is_archive_enabled_Set() const{
    return m_is_archive_enabled_isSet;
}

bool OAIRunFilter::is_is_archive_enabled_Valid() const{
    return m_is_archive_enabled_isValid;
}

QString OAIRunFilter::getOutputImageManifests() const {
    return m_output_image_manifests;
}
void OAIRunFilter::setOutputImageManifests(const QString &output_image_manifests) {
    m_output_image_manifests = output_image_manifests;
    m_output_image_manifests_isSet = true;
}

bool OAIRunFilter::is_output_image_manifests_Set() const{
    return m_output_image_manifests_isSet;
}

bool OAIRunFilter::is_output_image_manifests_Valid() const{
    return m_output_image_manifests_isValid;
}

QString OAIRunFilter::getRunId() const {
    return m_run_id;
}
void OAIRunFilter::setRunId(const QString &run_id) {
    m_run_id = run_id;
    m_run_id_isSet = true;
}

bool OAIRunFilter::is_run_id_Set() const{
    return m_run_id_isSet;
}

bool OAIRunFilter::is_run_id_Valid() const{
    return m_run_id_isValid;
}

QString OAIRunFilter::getRunType() const {
    return m_run_type;
}
void OAIRunFilter::setRunType(const QString &run_type) {
    m_run_type = run_type;
    m_run_type_isSet = true;
}

bool OAIRunFilter::is_run_type_Set() const{
    return m_run_type_isSet;
}

bool OAIRunFilter::is_run_type_Valid() const{
    return m_run_type_isValid;
}

QString OAIRunFilter::getStatus() const {
    return m_status;
}
void OAIRunFilter::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIRunFilter::is_status_Set() const{
    return m_status_isSet;
}

bool OAIRunFilter::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIRunFilter::getTaskName() const {
    return m_task_name;
}
void OAIRunFilter::setTaskName(const QString &task_name) {
    m_task_name = task_name;
    m_task_name_isSet = true;
}

bool OAIRunFilter::is_task_name_Set() const{
    return m_task_name_isSet;
}

bool OAIRunFilter::is_task_name_Valid() const{
    return m_task_name_isValid;
}

bool OAIRunFilter::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_create_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_finish_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_archive_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_output_image_manifests_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_run_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_run_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRunFilter::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
