/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAsyncOperationStatus.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAsyncOperationStatus::OAIAsyncOperationStatus(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAsyncOperationStatus::OAIAsyncOperationStatus() {
    this->initializeModel();
}

OAIAsyncOperationStatus::~OAIAsyncOperationStatus() {}

void OAIAsyncOperationStatus::initializeModel() {

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_end_time_isSet = false;
    m_end_time_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_operation_details_isSet = false;
    m_operation_details_isValid = false;

    m_operation_log_isSet = false;
    m_operation_log_isValid = false;

    m_operation_type_isSet = false;
    m_operation_type_isValid = false;

    m_parent_request_id_isSet = false;
    m_parent_request_id_isValid = false;

    m_resource_location_isSet = false;
    m_resource_location_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;
}

void OAIAsyncOperationStatus::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAsyncOperationStatus::fromJsonObject(QJsonObject json) {

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_end_time_isValid = ::OpenAPI::fromJsonValue(m_end_time, json[QString("endTime")]);
    m_end_time_isSet = !json[QString("endTime")].isNull() && m_end_time_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_operation_details_isValid = ::OpenAPI::fromJsonValue(m_operation_details, json[QString("operationDetails")]);
    m_operation_details_isSet = !json[QString("operationDetails")].isNull() && m_operation_details_isValid;

    m_operation_log_isValid = ::OpenAPI::fromJsonValue(m_operation_log, json[QString("operationLog")]);
    m_operation_log_isSet = !json[QString("operationLog")].isNull() && m_operation_log_isValid;

    m_operation_type_isValid = ::OpenAPI::fromJsonValue(m_operation_type, json[QString("operationType")]);
    m_operation_type_isSet = !json[QString("operationType")].isNull() && m_operation_type_isValid;

    m_parent_request_id_isValid = ::OpenAPI::fromJsonValue(m_parent_request_id, json[QString("parentRequestId")]);
    m_parent_request_id_isSet = !json[QString("parentRequestId")].isNull() && m_parent_request_id_isValid;

    m_resource_location_isValid = ::OpenAPI::fromJsonValue(m_resource_location, json[QString("resourceLocation")]);
    m_resource_location_isSet = !json[QString("resourceLocation")].isNull() && m_resource_location_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;
}

QString OAIAsyncOperationStatus::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAsyncOperationStatus::asJsonObject() const {
    QJsonObject obj;
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_end_time_isSet) {
        obj.insert(QString("endTime"), ::OpenAPI::toJsonValue(m_end_time));
    }
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_operation_details.isSet()) {
        obj.insert(QString("operationDetails"), ::OpenAPI::toJsonValue(m_operation_details));
    }
    if (m_operation_log_isSet) {
        obj.insert(QString("operationLog"), ::OpenAPI::toJsonValue(m_operation_log));
    }
    if (m_operation_type_isSet) {
        obj.insert(QString("operationType"), ::OpenAPI::toJsonValue(m_operation_type));
    }
    if (m_parent_request_id_isSet) {
        obj.insert(QString("parentRequestId"), ::OpenAPI::toJsonValue(m_parent_request_id));
    }
    if (m_resource_location_isSet) {
        obj.insert(QString("resourceLocation"), ::OpenAPI::toJsonValue(m_resource_location));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    return obj;
}

QDateTime OAIAsyncOperationStatus::getCreatedTime() const {
    return m_created_time;
}
void OAIAsyncOperationStatus::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIAsyncOperationStatus::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIAsyncOperationStatus::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QDateTime OAIAsyncOperationStatus::getEndTime() const {
    return m_end_time;
}
void OAIAsyncOperationStatus::setEndTime(const QDateTime &end_time) {
    m_end_time = end_time;
    m_end_time_isSet = true;
}

bool OAIAsyncOperationStatus::is_end_time_Set() const{
    return m_end_time_isSet;
}

bool OAIAsyncOperationStatus::is_end_time_Valid() const{
    return m_end_time_isValid;
}

OAIModelErrorResponse OAIAsyncOperationStatus::getError() const {
    return m_error;
}
void OAIAsyncOperationStatus::setError(const OAIModelErrorResponse &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIAsyncOperationStatus::is_error_Set() const{
    return m_error_isSet;
}

bool OAIAsyncOperationStatus::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIAsyncOperationStatus::getId() const {
    return m_id;
}
void OAIAsyncOperationStatus::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAsyncOperationStatus::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAsyncOperationStatus::is_id_Valid() const{
    return m_id_isValid;
}

OAIAsyncOperationDetails OAIAsyncOperationStatus::getOperationDetails() const {
    return m_operation_details;
}
void OAIAsyncOperationStatus::setOperationDetails(const OAIAsyncOperationDetails &operation_details) {
    m_operation_details = operation_details;
    m_operation_details_isSet = true;
}

bool OAIAsyncOperationStatus::is_operation_details_Set() const{
    return m_operation_details_isSet;
}

bool OAIAsyncOperationStatus::is_operation_details_Valid() const{
    return m_operation_details_isValid;
}

QString OAIAsyncOperationStatus::getOperationLog() const {
    return m_operation_log;
}
void OAIAsyncOperationStatus::setOperationLog(const QString &operation_log) {
    m_operation_log = operation_log;
    m_operation_log_isSet = true;
}

bool OAIAsyncOperationStatus::is_operation_log_Set() const{
    return m_operation_log_isSet;
}

bool OAIAsyncOperationStatus::is_operation_log_Valid() const{
    return m_operation_log_isValid;
}

QString OAIAsyncOperationStatus::getOperationType() const {
    return m_operation_type;
}
void OAIAsyncOperationStatus::setOperationType(const QString &operation_type) {
    m_operation_type = operation_type;
    m_operation_type_isSet = true;
}

bool OAIAsyncOperationStatus::is_operation_type_Set() const{
    return m_operation_type_isSet;
}

bool OAIAsyncOperationStatus::is_operation_type_Valid() const{
    return m_operation_type_isValid;
}

QString OAIAsyncOperationStatus::getParentRequestId() const {
    return m_parent_request_id;
}
void OAIAsyncOperationStatus::setParentRequestId(const QString &parent_request_id) {
    m_parent_request_id = parent_request_id;
    m_parent_request_id_isSet = true;
}

bool OAIAsyncOperationStatus::is_parent_request_id_Set() const{
    return m_parent_request_id_isSet;
}

bool OAIAsyncOperationStatus::is_parent_request_id_Valid() const{
    return m_parent_request_id_isValid;
}

QString OAIAsyncOperationStatus::getResourceLocation() const {
    return m_resource_location;
}
void OAIAsyncOperationStatus::setResourceLocation(const QString &resource_location) {
    m_resource_location = resource_location;
    m_resource_location_isSet = true;
}

bool OAIAsyncOperationStatus::is_resource_location_Set() const{
    return m_resource_location_isSet;
}

bool OAIAsyncOperationStatus::is_resource_location_Valid() const{
    return m_resource_location_isValid;
}

QString OAIAsyncOperationStatus::getState() const {
    return m_state;
}
void OAIAsyncOperationStatus::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIAsyncOperationStatus::is_state_Set() const{
    return m_state_isSet;
}

bool OAIAsyncOperationStatus::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIAsyncOperationStatus::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_log_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_request_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAsyncOperationStatus::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
