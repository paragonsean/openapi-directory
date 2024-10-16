/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITest_getTestReport_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITest_getTestReport_200_response::OAITest_getTestReport_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITest_getTestReport_200_response::OAITest_getTestReport_200_response() {
    this->initializeModel();
}

OAITest_getTestReport_200_response::~OAITest_getTestReport_200_response() {}

void OAITest_getTestReport_200_response::initializeModel() {

    m_app_upload_id_isSet = false;
    m_app_upload_id_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_date_finished_isSet = false;
    m_date_finished_isValid = false;

    m_device_logs_isSet = false;
    m_device_logs_isValid = false;

    m_error_message_isSet = false;
    m_error_message_isValid = false;

    m_features_isSet = false;
    m_features_isValid = false;

    m_finished_device_snapshots_isSet = false;
    m_finished_device_snapshots_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_platform_isSet = false;
    m_platform_isValid = false;

    m_revision_isSet = false;
    m_revision_isValid = false;

    m_schema_version_isSet = false;
    m_schema_version_isValid = false;

    m_snapshot_fatal_errors_isSet = false;
    m_snapshot_fatal_errors_isValid = false;

    m_stats_isSet = false;
    m_stats_isValid = false;

    m_test_type_isSet = false;
    m_test_type_isValid = false;
}

void OAITest_getTestReport_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITest_getTestReport_200_response::fromJsonObject(QJsonObject json) {

    m_app_upload_id_isValid = ::OpenAPI::fromJsonValue(m_app_upload_id, json[QString("app_upload_id")]);
    m_app_upload_id_isSet = !json[QString("app_upload_id")].isNull() && m_app_upload_id_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

    m_date_finished_isValid = ::OpenAPI::fromJsonValue(m_date_finished, json[QString("date_finished")]);
    m_date_finished_isSet = !json[QString("date_finished")].isNull() && m_date_finished_isValid;

    m_device_logs_isValid = ::OpenAPI::fromJsonValue(m_device_logs, json[QString("device_logs")]);
    m_device_logs_isSet = !json[QString("device_logs")].isNull() && m_device_logs_isValid;

    m_error_message_isValid = ::OpenAPI::fromJsonValue(m_error_message, json[QString("errorMessage")]);
    m_error_message_isSet = !json[QString("errorMessage")].isNull() && m_error_message_isValid;

    m_features_isValid = ::OpenAPI::fromJsonValue(m_features, json[QString("features")]);
    m_features_isSet = !json[QString("features")].isNull() && m_features_isValid;

    m_finished_device_snapshots_isValid = ::OpenAPI::fromJsonValue(m_finished_device_snapshots, json[QString("finished_device_snapshots")]);
    m_finished_device_snapshots_isSet = !json[QString("finished_device_snapshots")].isNull() && m_finished_device_snapshots_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_platform_isValid = ::OpenAPI::fromJsonValue(m_platform, json[QString("platform")]);
    m_platform_isSet = !json[QString("platform")].isNull() && m_platform_isValid;

    m_revision_isValid = ::OpenAPI::fromJsonValue(m_revision, json[QString("revision")]);
    m_revision_isSet = !json[QString("revision")].isNull() && m_revision_isValid;

    m_schema_version_isValid = ::OpenAPI::fromJsonValue(m_schema_version, json[QString("schema_version")]);
    m_schema_version_isSet = !json[QString("schema_version")].isNull() && m_schema_version_isValid;

    m_snapshot_fatal_errors_isValid = ::OpenAPI::fromJsonValue(m_snapshot_fatal_errors, json[QString("snapshot_fatal_errors")]);
    m_snapshot_fatal_errors_isSet = !json[QString("snapshot_fatal_errors")].isNull() && m_snapshot_fatal_errors_isValid;

    m_stats_isValid = ::OpenAPI::fromJsonValue(m_stats, json[QString("stats")]);
    m_stats_isSet = !json[QString("stats")].isNull() && m_stats_isValid;

    m_test_type_isValid = ::OpenAPI::fromJsonValue(m_test_type, json[QString("testType")]);
    m_test_type_isSet = !json[QString("testType")].isNull() && m_test_type_isValid;
}

QString OAITest_getTestReport_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITest_getTestReport_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_app_upload_id_isSet) {
        obj.insert(QString("app_upload_id"), ::OpenAPI::toJsonValue(m_app_upload_id));
    }
    if (m_date_isSet) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_date_finished_isSet) {
        obj.insert(QString("date_finished"), ::OpenAPI::toJsonValue(m_date_finished));
    }
    if (m_device_logs.size() > 0) {
        obj.insert(QString("device_logs"), ::OpenAPI::toJsonValue(m_device_logs));
    }
    if (m_error_message_isSet) {
        obj.insert(QString("errorMessage"), ::OpenAPI::toJsonValue(m_error_message));
    }
    if (m_features.size() > 0) {
        obj.insert(QString("features"), ::OpenAPI::toJsonValue(m_features));
    }
    if (m_finished_device_snapshots.size() > 0) {
        obj.insert(QString("finished_device_snapshots"), ::OpenAPI::toJsonValue(m_finished_device_snapshots));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_platform_isSet) {
        obj.insert(QString("platform"), ::OpenAPI::toJsonValue(m_platform));
    }
    if (m_revision_isSet) {
        obj.insert(QString("revision"), ::OpenAPI::toJsonValue(m_revision));
    }
    if (m_schema_version_isSet) {
        obj.insert(QString("schema_version"), ::OpenAPI::toJsonValue(m_schema_version));
    }
    if (m_snapshot_fatal_errors.size() > 0) {
        obj.insert(QString("snapshot_fatal_errors"), ::OpenAPI::toJsonValue(m_snapshot_fatal_errors));
    }
    if (m_stats.isSet()) {
        obj.insert(QString("stats"), ::OpenAPI::toJsonValue(m_stats));
    }
    if (m_test_type_isSet) {
        obj.insert(QString("testType"), ::OpenAPI::toJsonValue(m_test_type));
    }
    return obj;
}

QString OAITest_getTestReport_200_response::getAppUploadId() const {
    return m_app_upload_id;
}
void OAITest_getTestReport_200_response::setAppUploadId(const QString &app_upload_id) {
    m_app_upload_id = app_upload_id;
    m_app_upload_id_isSet = true;
}

bool OAITest_getTestReport_200_response::is_app_upload_id_Set() const{
    return m_app_upload_id_isSet;
}

bool OAITest_getTestReport_200_response::is_app_upload_id_Valid() const{
    return m_app_upload_id_isValid;
}

QString OAITest_getTestReport_200_response::getDate() const {
    return m_date;
}
void OAITest_getTestReport_200_response::setDate(const QString &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAITest_getTestReport_200_response::is_date_Set() const{
    return m_date_isSet;
}

bool OAITest_getTestReport_200_response::is_date_Valid() const{
    return m_date_isValid;
}

QString OAITest_getTestReport_200_response::getDateFinished() const {
    return m_date_finished;
}
void OAITest_getTestReport_200_response::setDateFinished(const QString &date_finished) {
    m_date_finished = date_finished;
    m_date_finished_isSet = true;
}

bool OAITest_getTestReport_200_response::is_date_finished_Set() const{
    return m_date_finished_isSet;
}

bool OAITest_getTestReport_200_response::is_date_finished_Valid() const{
    return m_date_finished_isValid;
}

QList<OAITest_getTestReport_200_response_device_logs_inner> OAITest_getTestReport_200_response::getDeviceLogs() const {
    return m_device_logs;
}
void OAITest_getTestReport_200_response::setDeviceLogs(const QList<OAITest_getTestReport_200_response_device_logs_inner> &device_logs) {
    m_device_logs = device_logs;
    m_device_logs_isSet = true;
}

bool OAITest_getTestReport_200_response::is_device_logs_Set() const{
    return m_device_logs_isSet;
}

bool OAITest_getTestReport_200_response::is_device_logs_Valid() const{
    return m_device_logs_isValid;
}

QString OAITest_getTestReport_200_response::getErrorMessage() const {
    return m_error_message;
}
void OAITest_getTestReport_200_response::setErrorMessage(const QString &error_message) {
    m_error_message = error_message;
    m_error_message_isSet = true;
}

bool OAITest_getTestReport_200_response::is_error_message_Set() const{
    return m_error_message_isSet;
}

bool OAITest_getTestReport_200_response::is_error_message_Valid() const{
    return m_error_message_isValid;
}

QList<OAITest_getTestReport_200_response_features_inner> OAITest_getTestReport_200_response::getFeatures() const {
    return m_features;
}
void OAITest_getTestReport_200_response::setFeatures(const QList<OAITest_getTestReport_200_response_features_inner> &features) {
    m_features = features;
    m_features_isSet = true;
}

bool OAITest_getTestReport_200_response::is_features_Set() const{
    return m_features_isSet;
}

bool OAITest_getTestReport_200_response::is_features_Valid() const{
    return m_features_isValid;
}

QList<QString> OAITest_getTestReport_200_response::getFinishedDeviceSnapshots() const {
    return m_finished_device_snapshots;
}
void OAITest_getTestReport_200_response::setFinishedDeviceSnapshots(const QList<QString> &finished_device_snapshots) {
    m_finished_device_snapshots = finished_device_snapshots;
    m_finished_device_snapshots_isSet = true;
}

bool OAITest_getTestReport_200_response::is_finished_device_snapshots_Set() const{
    return m_finished_device_snapshots_isSet;
}

bool OAITest_getTestReport_200_response::is_finished_device_snapshots_Valid() const{
    return m_finished_device_snapshots_isValid;
}

QString OAITest_getTestReport_200_response::getId() const {
    return m_id;
}
void OAITest_getTestReport_200_response::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITest_getTestReport_200_response::is_id_Set() const{
    return m_id_isSet;
}

bool OAITest_getTestReport_200_response::is_id_Valid() const{
    return m_id_isValid;
}

QString OAITest_getTestReport_200_response::getPlatform() const {
    return m_platform;
}
void OAITest_getTestReport_200_response::setPlatform(const QString &platform) {
    m_platform = platform;
    m_platform_isSet = true;
}

bool OAITest_getTestReport_200_response::is_platform_Set() const{
    return m_platform_isSet;
}

bool OAITest_getTestReport_200_response::is_platform_Valid() const{
    return m_platform_isValid;
}

double OAITest_getTestReport_200_response::getRevision() const {
    return m_revision;
}
void OAITest_getTestReport_200_response::setRevision(const double &revision) {
    m_revision = revision;
    m_revision_isSet = true;
}

bool OAITest_getTestReport_200_response::is_revision_Set() const{
    return m_revision_isSet;
}

bool OAITest_getTestReport_200_response::is_revision_Valid() const{
    return m_revision_isValid;
}

double OAITest_getTestReport_200_response::getSchemaVersion() const {
    return m_schema_version;
}
void OAITest_getTestReport_200_response::setSchemaVersion(const double &schema_version) {
    m_schema_version = schema_version;
    m_schema_version_isSet = true;
}

bool OAITest_getTestReport_200_response::is_schema_version_Set() const{
    return m_schema_version_isSet;
}

bool OAITest_getTestReport_200_response::is_schema_version_Valid() const{
    return m_schema_version_isValid;
}

QList<OAITest_getTestReport_200_response_snapshot_fatal_errors_inner> OAITest_getTestReport_200_response::getSnapshotFatalErrors() const {
    return m_snapshot_fatal_errors;
}
void OAITest_getTestReport_200_response::setSnapshotFatalErrors(const QList<OAITest_getTestReport_200_response_snapshot_fatal_errors_inner> &snapshot_fatal_errors) {
    m_snapshot_fatal_errors = snapshot_fatal_errors;
    m_snapshot_fatal_errors_isSet = true;
}

bool OAITest_getTestReport_200_response::is_snapshot_fatal_errors_Set() const{
    return m_snapshot_fatal_errors_isSet;
}

bool OAITest_getTestReport_200_response::is_snapshot_fatal_errors_Valid() const{
    return m_snapshot_fatal_errors_isValid;
}

OAITest_getTestReport_200_response_stats OAITest_getTestReport_200_response::getStats() const {
    return m_stats;
}
void OAITest_getTestReport_200_response::setStats(const OAITest_getTestReport_200_response_stats &stats) {
    m_stats = stats;
    m_stats_isSet = true;
}

bool OAITest_getTestReport_200_response::is_stats_Set() const{
    return m_stats_isSet;
}

bool OAITest_getTestReport_200_response::is_stats_Valid() const{
    return m_stats_isValid;
}

QString OAITest_getTestReport_200_response::getTestType() const {
    return m_test_type;
}
void OAITest_getTestReport_200_response::setTestType(const QString &test_type) {
    m_test_type = test_type;
    m_test_type_isSet = true;
}

bool OAITest_getTestReport_200_response::is_test_type_Set() const{
    return m_test_type_isSet;
}

bool OAITest_getTestReport_200_response::is_test_type_Valid() const{
    return m_test_type_isValid;
}

bool OAITest_getTestReport_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_upload_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_finished_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_device_logs.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_features.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_finished_device_snapshots.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_platform_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_revision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schema_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_snapshot_fatal_errors.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_stats.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_test_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITest_getTestReport_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_app_upload_id_isValid && m_date_isValid && m_date_finished_isValid && m_device_logs_isValid && m_features_isValid && m_finished_device_snapshots_isValid && m_id_isValid && m_platform_isValid && m_revision_isValid && m_schema_version_isValid && m_stats_isValid && m_test_type_isValid && true;
}

} // namespace OpenAPI
