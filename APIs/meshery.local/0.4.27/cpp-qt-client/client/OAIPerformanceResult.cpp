/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPerformanceResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPerformanceResult::OAIPerformanceResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPerformanceResult::OAIPerformanceResult() {
    this->initializeModel();
}

OAIPerformanceResult::~OAIPerformanceResult() {}

void OAIPerformanceResult::initializeModel() {

    m_mesh_isSet = false;
    m_mesh_isValid = false;

    m_meshery_id_isSet = false;
    m_meshery_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_performance_profile_isSet = false;
    m_performance_profile_isValid = false;

    m_runner_results_isSet = false;
    m_runner_results_isValid = false;

    m_server_board_config_isSet = false;
    m_server_board_config_isValid = false;

    m_server_metrics_isSet = false;
    m_server_metrics_isValid = false;

    m_test_start_time_isSet = false;
    m_test_start_time_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIPerformanceResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPerformanceResult::fromJsonObject(QJsonObject json) {

    m_mesh_isValid = ::OpenAPI::fromJsonValue(m_mesh, json[QString("mesh")]);
    m_mesh_isSet = !json[QString("mesh")].isNull() && m_mesh_isValid;

    m_meshery_id_isValid = ::OpenAPI::fromJsonValue(m_meshery_id, json[QString("meshery_id")]);
    m_meshery_id_isSet = !json[QString("meshery_id")].isNull() && m_meshery_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_performance_profile_isValid = ::OpenAPI::fromJsonValue(m_performance_profile, json[QString("performance_profile")]);
    m_performance_profile_isSet = !json[QString("performance_profile")].isNull() && m_performance_profile_isValid;

    m_runner_results_isValid = ::OpenAPI::fromJsonValue(m_runner_results, json[QString("runner_results")]);
    m_runner_results_isSet = !json[QString("runner_results")].isNull() && m_runner_results_isValid;

    m_server_board_config_isValid = ::OpenAPI::fromJsonValue(m_server_board_config, json[QString("server_board_config")]);
    m_server_board_config_isSet = !json[QString("server_board_config")].isNull() && m_server_board_config_isValid;

    m_server_metrics_isValid = ::OpenAPI::fromJsonValue(m_server_metrics, json[QString("server_metrics")]);
    m_server_metrics_isSet = !json[QString("server_metrics")].isNull() && m_server_metrics_isValid;

    m_test_start_time_isValid = ::OpenAPI::fromJsonValue(m_test_start_time, json[QString("test_start_time")]);
    m_test_start_time_isSet = !json[QString("test_start_time")].isNull() && m_test_start_time_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;
}

QString OAIPerformanceResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPerformanceResult::asJsonObject() const {
    QJsonObject obj;
    if (m_mesh_isSet) {
        obj.insert(QString("mesh"), ::OpenAPI::toJsonValue(m_mesh));
    }
    if (m_meshery_id.size() > 0) {
        obj.insert(QString("meshery_id"), ::OpenAPI::toJsonValue(m_meshery_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_performance_profile.size() > 0) {
        obj.insert(QString("performance_profile"), ::OpenAPI::toJsonValue(m_performance_profile));
    }
    if (m_runner_results.isSet()) {
        obj.insert(QString("runner_results"), ::OpenAPI::toJsonValue(m_runner_results));
    }
    if (m_server_board_config_isSet) {
        obj.insert(QString("server_board_config"), ::OpenAPI::toJsonValue(m_server_board_config));
    }
    if (m_server_metrics_isSet) {
        obj.insert(QString("server_metrics"), ::OpenAPI::toJsonValue(m_server_metrics));
    }
    if (m_test_start_time_isSet) {
        obj.insert(QString("test_start_time"), ::OpenAPI::toJsonValue(m_test_start_time));
    }
    if (m_user_id.size() > 0) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIPerformanceResult::getMesh() const {
    return m_mesh;
}
void OAIPerformanceResult::setMesh(const QString &mesh) {
    m_mesh = mesh;
    m_mesh_isSet = true;
}

bool OAIPerformanceResult::is_mesh_Set() const{
    return m_mesh_isSet;
}

bool OAIPerformanceResult::is_mesh_Valid() const{
    return m_mesh_isValid;
}

QList<qint32> OAIPerformanceResult::getMesheryId() const {
    return m_meshery_id;
}
void OAIPerformanceResult::setMesheryId(const QList<qint32> &meshery_id) {
    m_meshery_id = meshery_id;
    m_meshery_id_isSet = true;
}

bool OAIPerformanceResult::is_meshery_id_Set() const{
    return m_meshery_id_isSet;
}

bool OAIPerformanceResult::is_meshery_id_Valid() const{
    return m_meshery_id_isValid;
}

QString OAIPerformanceResult::getName() const {
    return m_name;
}
void OAIPerformanceResult::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPerformanceResult::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPerformanceResult::is_name_Valid() const{
    return m_name_isValid;
}

QList<qint32> OAIPerformanceResult::getPerformanceProfile() const {
    return m_performance_profile;
}
void OAIPerformanceResult::setPerformanceProfile(const QList<qint32> &performance_profile) {
    m_performance_profile = performance_profile;
    m_performance_profile_isSet = true;
}

bool OAIPerformanceResult::is_performance_profile_Set() const{
    return m_performance_profile_isSet;
}

bool OAIPerformanceResult::is_performance_profile_Valid() const{
    return m_performance_profile_isValid;
}

OAIRunnerResults OAIPerformanceResult::getRunnerResults() const {
    return m_runner_results;
}
void OAIPerformanceResult::setRunnerResults(const OAIRunnerResults &runner_results) {
    m_runner_results = runner_results;
    m_runner_results_isSet = true;
}

bool OAIPerformanceResult::is_runner_results_Set() const{
    return m_runner_results_isSet;
}

bool OAIPerformanceResult::is_runner_results_Valid() const{
    return m_runner_results_isValid;
}

OAIObject OAIPerformanceResult::getServerBoardConfig() const {
    return m_server_board_config;
}
void OAIPerformanceResult::setServerBoardConfig(const OAIObject &server_board_config) {
    m_server_board_config = server_board_config;
    m_server_board_config_isSet = true;
}

bool OAIPerformanceResult::is_server_board_config_Set() const{
    return m_server_board_config_isSet;
}

bool OAIPerformanceResult::is_server_board_config_Valid() const{
    return m_server_board_config_isValid;
}

OAIObject OAIPerformanceResult::getServerMetrics() const {
    return m_server_metrics;
}
void OAIPerformanceResult::setServerMetrics(const OAIObject &server_metrics) {
    m_server_metrics = server_metrics;
    m_server_metrics_isSet = true;
}

bool OAIPerformanceResult::is_server_metrics_Set() const{
    return m_server_metrics_isSet;
}

bool OAIPerformanceResult::is_server_metrics_Valid() const{
    return m_server_metrics_isValid;
}

QDateTime OAIPerformanceResult::getTestStartTime() const {
    return m_test_start_time;
}
void OAIPerformanceResult::setTestStartTime(const QDateTime &test_start_time) {
    m_test_start_time = test_start_time;
    m_test_start_time_isSet = true;
}

bool OAIPerformanceResult::is_test_start_time_Set() const{
    return m_test_start_time_isSet;
}

bool OAIPerformanceResult::is_test_start_time_Valid() const{
    return m_test_start_time_isValid;
}

QList<qint32> OAIPerformanceResult::getUserId() const {
    return m_user_id;
}
void OAIPerformanceResult::setUserId(const QList<qint32> &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIPerformanceResult::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIPerformanceResult::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIPerformanceResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_mesh_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_meshery_id.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_performance_profile.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_runner_results.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_board_config_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_metrics_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_test_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPerformanceResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
