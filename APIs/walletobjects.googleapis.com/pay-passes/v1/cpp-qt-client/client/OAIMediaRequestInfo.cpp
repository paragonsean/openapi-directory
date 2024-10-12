/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMediaRequestInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMediaRequestInfo::OAIMediaRequestInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMediaRequestInfo::OAIMediaRequestInfo() {
    this->initializeModel();
}

OAIMediaRequestInfo::~OAIMediaRequestInfo() {}

void OAIMediaRequestInfo::initializeModel() {

    m_current_bytes_isSet = false;
    m_current_bytes_isValid = false;

    m_custom_data_isSet = false;
    m_custom_data_isValid = false;

    m_diff_object_version_isSet = false;
    m_diff_object_version_isValid = false;

    m_final_status_isSet = false;
    m_final_status_isValid = false;

    m_notification_type_isSet = false;
    m_notification_type_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_total_bytes_isSet = false;
    m_total_bytes_isValid = false;

    m_total_bytes_is_estimated_isSet = false;
    m_total_bytes_is_estimated_isValid = false;
}

void OAIMediaRequestInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMediaRequestInfo::fromJsonObject(QJsonObject json) {

    m_current_bytes_isValid = ::OpenAPI::fromJsonValue(m_current_bytes, json[QString("currentBytes")]);
    m_current_bytes_isSet = !json[QString("currentBytes")].isNull() && m_current_bytes_isValid;

    m_custom_data_isValid = ::OpenAPI::fromJsonValue(m_custom_data, json[QString("customData")]);
    m_custom_data_isSet = !json[QString("customData")].isNull() && m_custom_data_isValid;

    m_diff_object_version_isValid = ::OpenAPI::fromJsonValue(m_diff_object_version, json[QString("diffObjectVersion")]);
    m_diff_object_version_isSet = !json[QString("diffObjectVersion")].isNull() && m_diff_object_version_isValid;

    m_final_status_isValid = ::OpenAPI::fromJsonValue(m_final_status, json[QString("finalStatus")]);
    m_final_status_isSet = !json[QString("finalStatus")].isNull() && m_final_status_isValid;

    m_notification_type_isValid = ::OpenAPI::fromJsonValue(m_notification_type, json[QString("notificationType")]);
    m_notification_type_isSet = !json[QString("notificationType")].isNull() && m_notification_type_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_total_bytes_isValid = ::OpenAPI::fromJsonValue(m_total_bytes, json[QString("totalBytes")]);
    m_total_bytes_isSet = !json[QString("totalBytes")].isNull() && m_total_bytes_isValid;

    m_total_bytes_is_estimated_isValid = ::OpenAPI::fromJsonValue(m_total_bytes_is_estimated, json[QString("totalBytesIsEstimated")]);
    m_total_bytes_is_estimated_isSet = !json[QString("totalBytesIsEstimated")].isNull() && m_total_bytes_is_estimated_isValid;
}

QString OAIMediaRequestInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMediaRequestInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_current_bytes_isSet) {
        obj.insert(QString("currentBytes"), ::OpenAPI::toJsonValue(m_current_bytes));
    }
    if (m_custom_data_isSet) {
        obj.insert(QString("customData"), ::OpenAPI::toJsonValue(m_custom_data));
    }
    if (m_diff_object_version_isSet) {
        obj.insert(QString("diffObjectVersion"), ::OpenAPI::toJsonValue(m_diff_object_version));
    }
    if (m_final_status_isSet) {
        obj.insert(QString("finalStatus"), ::OpenAPI::toJsonValue(m_final_status));
    }
    if (m_notification_type_isSet) {
        obj.insert(QString("notificationType"), ::OpenAPI::toJsonValue(m_notification_type));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_total_bytes_isSet) {
        obj.insert(QString("totalBytes"), ::OpenAPI::toJsonValue(m_total_bytes));
    }
    if (m_total_bytes_is_estimated_isSet) {
        obj.insert(QString("totalBytesIsEstimated"), ::OpenAPI::toJsonValue(m_total_bytes_is_estimated));
    }
    return obj;
}

QString OAIMediaRequestInfo::getCurrentBytes() const {
    return m_current_bytes;
}
void OAIMediaRequestInfo::setCurrentBytes(const QString &current_bytes) {
    m_current_bytes = current_bytes;
    m_current_bytes_isSet = true;
}

bool OAIMediaRequestInfo::is_current_bytes_Set() const{
    return m_current_bytes_isSet;
}

bool OAIMediaRequestInfo::is_current_bytes_Valid() const{
    return m_current_bytes_isValid;
}

QString OAIMediaRequestInfo::getCustomData() const {
    return m_custom_data;
}
void OAIMediaRequestInfo::setCustomData(const QString &custom_data) {
    m_custom_data = custom_data;
    m_custom_data_isSet = true;
}

bool OAIMediaRequestInfo::is_custom_data_Set() const{
    return m_custom_data_isSet;
}

bool OAIMediaRequestInfo::is_custom_data_Valid() const{
    return m_custom_data_isValid;
}

QString OAIMediaRequestInfo::getDiffObjectVersion() const {
    return m_diff_object_version;
}
void OAIMediaRequestInfo::setDiffObjectVersion(const QString &diff_object_version) {
    m_diff_object_version = diff_object_version;
    m_diff_object_version_isSet = true;
}

bool OAIMediaRequestInfo::is_diff_object_version_Set() const{
    return m_diff_object_version_isSet;
}

bool OAIMediaRequestInfo::is_diff_object_version_Valid() const{
    return m_diff_object_version_isValid;
}

qint32 OAIMediaRequestInfo::getFinalStatus() const {
    return m_final_status;
}
void OAIMediaRequestInfo::setFinalStatus(const qint32 &final_status) {
    m_final_status = final_status;
    m_final_status_isSet = true;
}

bool OAIMediaRequestInfo::is_final_status_Set() const{
    return m_final_status_isSet;
}

bool OAIMediaRequestInfo::is_final_status_Valid() const{
    return m_final_status_isValid;
}

QString OAIMediaRequestInfo::getNotificationType() const {
    return m_notification_type;
}
void OAIMediaRequestInfo::setNotificationType(const QString &notification_type) {
    m_notification_type = notification_type;
    m_notification_type_isSet = true;
}

bool OAIMediaRequestInfo::is_notification_type_Set() const{
    return m_notification_type_isSet;
}

bool OAIMediaRequestInfo::is_notification_type_Valid() const{
    return m_notification_type_isValid;
}

QString OAIMediaRequestInfo::getRequestId() const {
    return m_request_id;
}
void OAIMediaRequestInfo::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIMediaRequestInfo::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIMediaRequestInfo::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QString OAIMediaRequestInfo::getTotalBytes() const {
    return m_total_bytes;
}
void OAIMediaRequestInfo::setTotalBytes(const QString &total_bytes) {
    m_total_bytes = total_bytes;
    m_total_bytes_isSet = true;
}

bool OAIMediaRequestInfo::is_total_bytes_Set() const{
    return m_total_bytes_isSet;
}

bool OAIMediaRequestInfo::is_total_bytes_Valid() const{
    return m_total_bytes_isValid;
}

bool OAIMediaRequestInfo::isTotalBytesIsEstimated() const {
    return m_total_bytes_is_estimated;
}
void OAIMediaRequestInfo::setTotalBytesIsEstimated(const bool &total_bytes_is_estimated) {
    m_total_bytes_is_estimated = total_bytes_is_estimated;
    m_total_bytes_is_estimated_isSet = true;
}

bool OAIMediaRequestInfo::is_total_bytes_is_estimated_Set() const{
    return m_total_bytes_is_estimated_isSet;
}

bool OAIMediaRequestInfo::is_total_bytes_is_estimated_Valid() const{
    return m_total_bytes_is_estimated_isValid;
}

bool OAIMediaRequestInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_current_bytes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_diff_object_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_final_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notification_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_bytes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_bytes_is_estimated_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMediaRequestInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
