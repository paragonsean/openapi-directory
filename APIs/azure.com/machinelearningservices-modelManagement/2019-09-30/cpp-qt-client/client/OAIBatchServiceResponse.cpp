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

#include "OAIBatchServiceResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBatchServiceResponse::OAIBatchServiceResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBatchServiceResponse::OAIBatchServiceResponse() {
    this->initializeModel();
}

OAIBatchServiceResponse::~OAIBatchServiceResponse() {}

void OAIBatchServiceResponse::initializeModel() {

    m_compute_type_isSet = false;
    m_compute_type_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_deployment_type_isSet = false;
    m_deployment_type_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_kv_tags_isSet = false;
    m_kv_tags_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_operation_id_isSet = false;
    m_operation_id_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_app_insights_enabled_isSet = false;
    m_app_insights_enabled_isValid = false;

    m_compute_name_isSet = false;
    m_compute_name_isValid = false;

    m_entry_script_isSet = false;
    m_entry_script_isValid = false;

    m_environment_name_isSet = false;
    m_environment_name_isValid = false;

    m_environment_version_isSet = false;
    m_environment_version_isValid = false;

    m_error_threshold_isSet = false;
    m_error_threshold_isValid = false;

    m_input_format_isSet = false;
    m_input_format_isValid = false;

    m_mini_batch_size_isSet = false;
    m_mini_batch_size_isValid = false;

    m_model_data_collection_isSet = false;
    m_model_data_collection_isValid = false;

    m_model_ids_isSet = false;
    m_model_ids_isValid = false;

    m_node_count_isSet = false;
    m_node_count_isValid = false;

    m_output_action_isSet = false;
    m_output_action_isValid = false;

    m_process_count_per_node_isSet = false;
    m_process_count_per_node_isValid = false;

    m_scoring_uri_isSet = false;
    m_scoring_uri_isValid = false;
}

void OAIBatchServiceResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBatchServiceResponse::fromJsonObject(QJsonObject json) {

    m_compute_type_isValid = ::OpenAPI::fromJsonValue(m_compute_type, json[QString("computeType")]);
    m_compute_type_isSet = !json[QString("computeType")].isNull() && m_compute_type_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_deployment_type_isValid = ::OpenAPI::fromJsonValue(m_deployment_type, json[QString("deploymentType")]);
    m_deployment_type_isSet = !json[QString("deploymentType")].isNull() && m_deployment_type_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_kv_tags_isValid = ::OpenAPI::fromJsonValue(m_kv_tags, json[QString("kvTags")]);
    m_kv_tags_isSet = !json[QString("kvTags")].isNull() && m_kv_tags_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_operation_id_isValid = ::OpenAPI::fromJsonValue(m_operation_id, json[QString("operationId")]);
    m_operation_id_isSet = !json[QString("operationId")].isNull() && m_operation_id_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m_app_insights_enabled_isValid = ::OpenAPI::fromJsonValue(m_app_insights_enabled, json[QString("appInsightsEnabled")]);
    m_app_insights_enabled_isSet = !json[QString("appInsightsEnabled")].isNull() && m_app_insights_enabled_isValid;

    m_compute_name_isValid = ::OpenAPI::fromJsonValue(m_compute_name, json[QString("computeName")]);
    m_compute_name_isSet = !json[QString("computeName")].isNull() && m_compute_name_isValid;

    m_entry_script_isValid = ::OpenAPI::fromJsonValue(m_entry_script, json[QString("entryScript")]);
    m_entry_script_isSet = !json[QString("entryScript")].isNull() && m_entry_script_isValid;

    m_environment_name_isValid = ::OpenAPI::fromJsonValue(m_environment_name, json[QString("environmentName")]);
    m_environment_name_isSet = !json[QString("environmentName")].isNull() && m_environment_name_isValid;

    m_environment_version_isValid = ::OpenAPI::fromJsonValue(m_environment_version, json[QString("environmentVersion")]);
    m_environment_version_isSet = !json[QString("environmentVersion")].isNull() && m_environment_version_isValid;

    m_error_threshold_isValid = ::OpenAPI::fromJsonValue(m_error_threshold, json[QString("errorThreshold")]);
    m_error_threshold_isSet = !json[QString("errorThreshold")].isNull() && m_error_threshold_isValid;

    m_input_format_isValid = ::OpenAPI::fromJsonValue(m_input_format, json[QString("inputFormat")]);
    m_input_format_isSet = !json[QString("inputFormat")].isNull() && m_input_format_isValid;

    m_mini_batch_size_isValid = ::OpenAPI::fromJsonValue(m_mini_batch_size, json[QString("miniBatchSize")]);
    m_mini_batch_size_isSet = !json[QString("miniBatchSize")].isNull() && m_mini_batch_size_isValid;

    m_model_data_collection_isValid = ::OpenAPI::fromJsonValue(m_model_data_collection, json[QString("modelDataCollection")]);
    m_model_data_collection_isSet = !json[QString("modelDataCollection")].isNull() && m_model_data_collection_isValid;

    m_model_ids_isValid = ::OpenAPI::fromJsonValue(m_model_ids, json[QString("modelIds")]);
    m_model_ids_isSet = !json[QString("modelIds")].isNull() && m_model_ids_isValid;

    m_node_count_isValid = ::OpenAPI::fromJsonValue(m_node_count, json[QString("nodeCount")]);
    m_node_count_isSet = !json[QString("nodeCount")].isNull() && m_node_count_isValid;

    m_output_action_isValid = ::OpenAPI::fromJsonValue(m_output_action, json[QString("outputAction")]);
    m_output_action_isSet = !json[QString("outputAction")].isNull() && m_output_action_isValid;

    m_process_count_per_node_isValid = ::OpenAPI::fromJsonValue(m_process_count_per_node, json[QString("processCountPerNode")]);
    m_process_count_per_node_isSet = !json[QString("processCountPerNode")].isNull() && m_process_count_per_node_isValid;

    m_scoring_uri_isValid = ::OpenAPI::fromJsonValue(m_scoring_uri, json[QString("scoringUri")]);
    m_scoring_uri_isSet = !json[QString("scoringUri")].isNull() && m_scoring_uri_isValid;
}

QString OAIBatchServiceResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBatchServiceResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_compute_type_isSet) {
        obj.insert(QString("computeType"), ::OpenAPI::toJsonValue(m_compute_type));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_deployment_type_isSet) {
        obj.insert(QString("deploymentType"), ::OpenAPI::toJsonValue(m_deployment_type));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_kv_tags.size() > 0) {
        obj.insert(QString("kvTags"), ::OpenAPI::toJsonValue(m_kv_tags));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_operation_id_isSet) {
        obj.insert(QString("operationId"), ::OpenAPI::toJsonValue(m_operation_id));
    }
    if (m_properties.size() > 0) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_app_insights_enabled_isSet) {
        obj.insert(QString("appInsightsEnabled"), ::OpenAPI::toJsonValue(m_app_insights_enabled));
    }
    if (m_compute_name_isSet) {
        obj.insert(QString("computeName"), ::OpenAPI::toJsonValue(m_compute_name));
    }
    if (m_entry_script_isSet) {
        obj.insert(QString("entryScript"), ::OpenAPI::toJsonValue(m_entry_script));
    }
    if (m_environment_name_isSet) {
        obj.insert(QString("environmentName"), ::OpenAPI::toJsonValue(m_environment_name));
    }
    if (m_environment_version_isSet) {
        obj.insert(QString("environmentVersion"), ::OpenAPI::toJsonValue(m_environment_version));
    }
    if (m_error_threshold_isSet) {
        obj.insert(QString("errorThreshold"), ::OpenAPI::toJsonValue(m_error_threshold));
    }
    if (m_input_format_isSet) {
        obj.insert(QString("inputFormat"), ::OpenAPI::toJsonValue(m_input_format));
    }
    if (m_mini_batch_size_isSet) {
        obj.insert(QString("miniBatchSize"), ::OpenAPI::toJsonValue(m_mini_batch_size));
    }
    if (m_model_data_collection.isSet()) {
        obj.insert(QString("modelDataCollection"), ::OpenAPI::toJsonValue(m_model_data_collection));
    }
    if (m_model_ids.size() > 0) {
        obj.insert(QString("modelIds"), ::OpenAPI::toJsonValue(m_model_ids));
    }
    if (m_node_count_isSet) {
        obj.insert(QString("nodeCount"), ::OpenAPI::toJsonValue(m_node_count));
    }
    if (m_output_action_isSet) {
        obj.insert(QString("outputAction"), ::OpenAPI::toJsonValue(m_output_action));
    }
    if (m_process_count_per_node_isSet) {
        obj.insert(QString("processCountPerNode"), ::OpenAPI::toJsonValue(m_process_count_per_node));
    }
    if (m_scoring_uri_isSet) {
        obj.insert(QString("scoringUri"), ::OpenAPI::toJsonValue(m_scoring_uri));
    }
    return obj;
}

QString OAIBatchServiceResponse::getComputeType() const {
    return m_compute_type;
}
void OAIBatchServiceResponse::setComputeType(const QString &compute_type) {
    m_compute_type = compute_type;
    m_compute_type_isSet = true;
}

bool OAIBatchServiceResponse::is_compute_type_Set() const{
    return m_compute_type_isSet;
}

bool OAIBatchServiceResponse::is_compute_type_Valid() const{
    return m_compute_type_isValid;
}

QDateTime OAIBatchServiceResponse::getCreatedTime() const {
    return m_created_time;
}
void OAIBatchServiceResponse::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIBatchServiceResponse::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIBatchServiceResponse::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAIBatchServiceResponse::getDeploymentType() const {
    return m_deployment_type;
}
void OAIBatchServiceResponse::setDeploymentType(const QString &deployment_type) {
    m_deployment_type = deployment_type;
    m_deployment_type_isSet = true;
}

bool OAIBatchServiceResponse::is_deployment_type_Set() const{
    return m_deployment_type_isSet;
}

bool OAIBatchServiceResponse::is_deployment_type_Valid() const{
    return m_deployment_type_isValid;
}

QString OAIBatchServiceResponse::getDescription() const {
    return m_description;
}
void OAIBatchServiceResponse::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIBatchServiceResponse::is_description_Set() const{
    return m_description_isSet;
}

bool OAIBatchServiceResponse::is_description_Valid() const{
    return m_description_isValid;
}

OAIModelErrorResponse OAIBatchServiceResponse::getError() const {
    return m_error;
}
void OAIBatchServiceResponse::setError(const OAIModelErrorResponse &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIBatchServiceResponse::is_error_Set() const{
    return m_error_isSet;
}

bool OAIBatchServiceResponse::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIBatchServiceResponse::getId() const {
    return m_id;
}
void OAIBatchServiceResponse::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBatchServiceResponse::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBatchServiceResponse::is_id_Valid() const{
    return m_id_isValid;
}

QMap<QString, QString> OAIBatchServiceResponse::getKvTags() const {
    return m_kv_tags;
}
void OAIBatchServiceResponse::setKvTags(const QMap<QString, QString> &kv_tags) {
    m_kv_tags = kv_tags;
    m_kv_tags_isSet = true;
}

bool OAIBatchServiceResponse::is_kv_tags_Set() const{
    return m_kv_tags_isSet;
}

bool OAIBatchServiceResponse::is_kv_tags_Valid() const{
    return m_kv_tags_isValid;
}

QString OAIBatchServiceResponse::getName() const {
    return m_name;
}
void OAIBatchServiceResponse::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBatchServiceResponse::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBatchServiceResponse::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIBatchServiceResponse::getOperationId() const {
    return m_operation_id;
}
void OAIBatchServiceResponse::setOperationId(const QString &operation_id) {
    m_operation_id = operation_id;
    m_operation_id_isSet = true;
}

bool OAIBatchServiceResponse::is_operation_id_Set() const{
    return m_operation_id_isSet;
}

bool OAIBatchServiceResponse::is_operation_id_Valid() const{
    return m_operation_id_isValid;
}

QMap<QString, QString> OAIBatchServiceResponse::getProperties() const {
    return m_properties;
}
void OAIBatchServiceResponse::setProperties(const QMap<QString, QString> &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIBatchServiceResponse::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIBatchServiceResponse::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIBatchServiceResponse::getState() const {
    return m_state;
}
void OAIBatchServiceResponse::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIBatchServiceResponse::is_state_Set() const{
    return m_state_isSet;
}

bool OAIBatchServiceResponse::is_state_Valid() const{
    return m_state_isValid;
}

QDateTime OAIBatchServiceResponse::getUpdatedTime() const {
    return m_updated_time;
}
void OAIBatchServiceResponse::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIBatchServiceResponse::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIBatchServiceResponse::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAIBatchServiceResponse::isAppInsightsEnabled() const {
    return m_app_insights_enabled;
}
void OAIBatchServiceResponse::setAppInsightsEnabled(const bool &app_insights_enabled) {
    m_app_insights_enabled = app_insights_enabled;
    m_app_insights_enabled_isSet = true;
}

bool OAIBatchServiceResponse::is_app_insights_enabled_Set() const{
    return m_app_insights_enabled_isSet;
}

bool OAIBatchServiceResponse::is_app_insights_enabled_Valid() const{
    return m_app_insights_enabled_isValid;
}

QString OAIBatchServiceResponse::getComputeName() const {
    return m_compute_name;
}
void OAIBatchServiceResponse::setComputeName(const QString &compute_name) {
    m_compute_name = compute_name;
    m_compute_name_isSet = true;
}

bool OAIBatchServiceResponse::is_compute_name_Set() const{
    return m_compute_name_isSet;
}

bool OAIBatchServiceResponse::is_compute_name_Valid() const{
    return m_compute_name_isValid;
}

QString OAIBatchServiceResponse::getEntryScript() const {
    return m_entry_script;
}
void OAIBatchServiceResponse::setEntryScript(const QString &entry_script) {
    m_entry_script = entry_script;
    m_entry_script_isSet = true;
}

bool OAIBatchServiceResponse::is_entry_script_Set() const{
    return m_entry_script_isSet;
}

bool OAIBatchServiceResponse::is_entry_script_Valid() const{
    return m_entry_script_isValid;
}

QString OAIBatchServiceResponse::getEnvironmentName() const {
    return m_environment_name;
}
void OAIBatchServiceResponse::setEnvironmentName(const QString &environment_name) {
    m_environment_name = environment_name;
    m_environment_name_isSet = true;
}

bool OAIBatchServiceResponse::is_environment_name_Set() const{
    return m_environment_name_isSet;
}

bool OAIBatchServiceResponse::is_environment_name_Valid() const{
    return m_environment_name_isValid;
}

QString OAIBatchServiceResponse::getEnvironmentVersion() const {
    return m_environment_version;
}
void OAIBatchServiceResponse::setEnvironmentVersion(const QString &environment_version) {
    m_environment_version = environment_version;
    m_environment_version_isSet = true;
}

bool OAIBatchServiceResponse::is_environment_version_Set() const{
    return m_environment_version_isSet;
}

bool OAIBatchServiceResponse::is_environment_version_Valid() const{
    return m_environment_version_isValid;
}

double OAIBatchServiceResponse::getErrorThreshold() const {
    return m_error_threshold;
}
void OAIBatchServiceResponse::setErrorThreshold(const double &error_threshold) {
    m_error_threshold = error_threshold;
    m_error_threshold_isSet = true;
}

bool OAIBatchServiceResponse::is_error_threshold_Set() const{
    return m_error_threshold_isSet;
}

bool OAIBatchServiceResponse::is_error_threshold_Valid() const{
    return m_error_threshold_isValid;
}

QString OAIBatchServiceResponse::getInputFormat() const {
    return m_input_format;
}
void OAIBatchServiceResponse::setInputFormat(const QString &input_format) {
    m_input_format = input_format;
    m_input_format_isSet = true;
}

bool OAIBatchServiceResponse::is_input_format_Set() const{
    return m_input_format_isSet;
}

bool OAIBatchServiceResponse::is_input_format_Valid() const{
    return m_input_format_isValid;
}

qint32 OAIBatchServiceResponse::getMiniBatchSize() const {
    return m_mini_batch_size;
}
void OAIBatchServiceResponse::setMiniBatchSize(const qint32 &mini_batch_size) {
    m_mini_batch_size = mini_batch_size;
    m_mini_batch_size_isSet = true;
}

bool OAIBatchServiceResponse::is_mini_batch_size_Set() const{
    return m_mini_batch_size_isSet;
}

bool OAIBatchServiceResponse::is_mini_batch_size_Valid() const{
    return m_mini_batch_size_isValid;
}

OAIModelDataCollection OAIBatchServiceResponse::getModelDataCollection() const {
    return m_model_data_collection;
}
void OAIBatchServiceResponse::setModelDataCollection(const OAIModelDataCollection &model_data_collection) {
    m_model_data_collection = model_data_collection;
    m_model_data_collection_isSet = true;
}

bool OAIBatchServiceResponse::is_model_data_collection_Set() const{
    return m_model_data_collection_isSet;
}

bool OAIBatchServiceResponse::is_model_data_collection_Valid() const{
    return m_model_data_collection_isValid;
}

QList<QString> OAIBatchServiceResponse::getModelIds() const {
    return m_model_ids;
}
void OAIBatchServiceResponse::setModelIds(const QList<QString> &model_ids) {
    m_model_ids = model_ids;
    m_model_ids_isSet = true;
}

bool OAIBatchServiceResponse::is_model_ids_Set() const{
    return m_model_ids_isSet;
}

bool OAIBatchServiceResponse::is_model_ids_Valid() const{
    return m_model_ids_isValid;
}

qint32 OAIBatchServiceResponse::getNodeCount() const {
    return m_node_count;
}
void OAIBatchServiceResponse::setNodeCount(const qint32 &node_count) {
    m_node_count = node_count;
    m_node_count_isSet = true;
}

bool OAIBatchServiceResponse::is_node_count_Set() const{
    return m_node_count_isSet;
}

bool OAIBatchServiceResponse::is_node_count_Valid() const{
    return m_node_count_isValid;
}

QString OAIBatchServiceResponse::getOutputAction() const {
    return m_output_action;
}
void OAIBatchServiceResponse::setOutputAction(const QString &output_action) {
    m_output_action = output_action;
    m_output_action_isSet = true;
}

bool OAIBatchServiceResponse::is_output_action_Set() const{
    return m_output_action_isSet;
}

bool OAIBatchServiceResponse::is_output_action_Valid() const{
    return m_output_action_isValid;
}

qint32 OAIBatchServiceResponse::getProcessCountPerNode() const {
    return m_process_count_per_node;
}
void OAIBatchServiceResponse::setProcessCountPerNode(const qint32 &process_count_per_node) {
    m_process_count_per_node = process_count_per_node;
    m_process_count_per_node_isSet = true;
}

bool OAIBatchServiceResponse::is_process_count_per_node_Set() const{
    return m_process_count_per_node_isSet;
}

bool OAIBatchServiceResponse::is_process_count_per_node_Valid() const{
    return m_process_count_per_node_isValid;
}

QString OAIBatchServiceResponse::getScoringUri() const {
    return m_scoring_uri;
}
void OAIBatchServiceResponse::setScoringUri(const QString &scoring_uri) {
    m_scoring_uri = scoring_uri;
    m_scoring_uri_isSet = true;
}

bool OAIBatchServiceResponse::is_scoring_uri_Set() const{
    return m_scoring_uri_isSet;
}

bool OAIBatchServiceResponse::is_scoring_uri_Valid() const{
    return m_scoring_uri_isValid;
}

bool OAIBatchServiceResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_compute_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deployment_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
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

        if (m_kv_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_app_insights_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_compute_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entry_script_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_environment_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_environment_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_threshold_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_input_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mini_batch_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_data_collection.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_node_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_output_action_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_process_count_per_node_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scoring_uri_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBatchServiceResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_compute_type_isValid && true;
}

} // namespace OpenAPI
