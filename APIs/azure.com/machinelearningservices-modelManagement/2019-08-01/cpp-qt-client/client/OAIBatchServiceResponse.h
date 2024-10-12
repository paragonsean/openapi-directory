/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBatchServiceResponse.h
 *
 * 
 */

#ifndef OAIBatchServiceResponse_H
#define OAIBatchServiceResponse_H

#include <QJsonObject>

#include "OAIModelDataCollection.h"
#include "OAIModelErrorResponse.h"
#include "OAIServiceResponseBase.h"
#include <QDateTime>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIModelErrorResponse;
class OAIModelDataCollection;

class OAIBatchServiceResponse : public OAIObject {
public:
    OAIBatchServiceResponse();
    OAIBatchServiceResponse(QString json);
    ~OAIBatchServiceResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getComputeType() const;
    void setComputeType(const QString &compute_type);
    bool is_compute_type_Set() const;
    bool is_compute_type_Valid() const;

    QDateTime getCreatedTime() const;
    void setCreatedTime(const QDateTime &created_time);
    bool is_created_time_Set() const;
    bool is_created_time_Valid() const;

    QString getDeploymentType() const;
    void setDeploymentType(const QString &deployment_type);
    bool is_deployment_type_Set() const;
    bool is_deployment_type_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAIModelErrorResponse getError() const;
    void setError(const OAIModelErrorResponse &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QMap<QString, QString> getKvTags() const;
    void setKvTags(const QMap<QString, QString> &kv_tags);
    bool is_kv_tags_Set() const;
    bool is_kv_tags_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOperationId() const;
    void setOperationId(const QString &operation_id);
    bool is_operation_id_Set() const;
    bool is_operation_id_Valid() const;

    QMap<QString, QString> getProperties() const;
    void setProperties(const QMap<QString, QString> &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QDateTime getUpdatedTime() const;
    void setUpdatedTime(const QDateTime &updated_time);
    bool is_updated_time_Set() const;
    bool is_updated_time_Valid() const;

    bool isAppInsightsEnabled() const;
    void setAppInsightsEnabled(const bool &app_insights_enabled);
    bool is_app_insights_enabled_Set() const;
    bool is_app_insights_enabled_Valid() const;

    QString getComputeName() const;
    void setComputeName(const QString &compute_name);
    bool is_compute_name_Set() const;
    bool is_compute_name_Valid() const;

    QString getEntryScript() const;
    void setEntryScript(const QString &entry_script);
    bool is_entry_script_Set() const;
    bool is_entry_script_Valid() const;

    QString getEnvironmentName() const;
    void setEnvironmentName(const QString &environment_name);
    bool is_environment_name_Set() const;
    bool is_environment_name_Valid() const;

    QString getEnvironmentVersion() const;
    void setEnvironmentVersion(const QString &environment_version);
    bool is_environment_version_Set() const;
    bool is_environment_version_Valid() const;

    double getErrorThreshold() const;
    void setErrorThreshold(const double &error_threshold);
    bool is_error_threshold_Set() const;
    bool is_error_threshold_Valid() const;

    QString getInputFormat() const;
    void setInputFormat(const QString &input_format);
    bool is_input_format_Set() const;
    bool is_input_format_Valid() const;

    qint32 getMiniBatchSize() const;
    void setMiniBatchSize(const qint32 &mini_batch_size);
    bool is_mini_batch_size_Set() const;
    bool is_mini_batch_size_Valid() const;

    OAIModelDataCollection getModelDataCollection() const;
    void setModelDataCollection(const OAIModelDataCollection &model_data_collection);
    bool is_model_data_collection_Set() const;
    bool is_model_data_collection_Valid() const;

    QList<QString> getModelIds() const;
    void setModelIds(const QList<QString> &model_ids);
    bool is_model_ids_Set() const;
    bool is_model_ids_Valid() const;

    qint32 getNodeCount() const;
    void setNodeCount(const qint32 &node_count);
    bool is_node_count_Set() const;
    bool is_node_count_Valid() const;

    QString getOutputAction() const;
    void setOutputAction(const QString &output_action);
    bool is_output_action_Set() const;
    bool is_output_action_Valid() const;

    qint32 getProcessCountPerNode() const;
    void setProcessCountPerNode(const qint32 &process_count_per_node);
    bool is_process_count_per_node_Set() const;
    bool is_process_count_per_node_Valid() const;

    QString getScoringUri() const;
    void setScoringUri(const QString &scoring_uri);
    bool is_scoring_uri_Set() const;
    bool is_scoring_uri_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_compute_type;
    bool m_compute_type_isSet;
    bool m_compute_type_isValid;

    QDateTime m_created_time;
    bool m_created_time_isSet;
    bool m_created_time_isValid;

    QString m_deployment_type;
    bool m_deployment_type_isSet;
    bool m_deployment_type_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAIModelErrorResponse m_error;
    bool m_error_isSet;
    bool m_error_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QMap<QString, QString> m_kv_tags;
    bool m_kv_tags_isSet;
    bool m_kv_tags_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_operation_id;
    bool m_operation_id_isSet;
    bool m_operation_id_isValid;

    QMap<QString, QString> m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QDateTime m_updated_time;
    bool m_updated_time_isSet;
    bool m_updated_time_isValid;

    bool m_app_insights_enabled;
    bool m_app_insights_enabled_isSet;
    bool m_app_insights_enabled_isValid;

    QString m_compute_name;
    bool m_compute_name_isSet;
    bool m_compute_name_isValid;

    QString m_entry_script;
    bool m_entry_script_isSet;
    bool m_entry_script_isValid;

    QString m_environment_name;
    bool m_environment_name_isSet;
    bool m_environment_name_isValid;

    QString m_environment_version;
    bool m_environment_version_isSet;
    bool m_environment_version_isValid;

    double m_error_threshold;
    bool m_error_threshold_isSet;
    bool m_error_threshold_isValid;

    QString m_input_format;
    bool m_input_format_isSet;
    bool m_input_format_isValid;

    qint32 m_mini_batch_size;
    bool m_mini_batch_size_isSet;
    bool m_mini_batch_size_isValid;

    OAIModelDataCollection m_model_data_collection;
    bool m_model_data_collection_isSet;
    bool m_model_data_collection_isValid;

    QList<QString> m_model_ids;
    bool m_model_ids_isSet;
    bool m_model_ids_isValid;

    qint32 m_node_count;
    bool m_node_count_isSet;
    bool m_node_count_isValid;

    QString m_output_action;
    bool m_output_action_isSet;
    bool m_output_action_isValid;

    qint32 m_process_count_per_node;
    bool m_process_count_per_node_isSet;
    bool m_process_count_per_node_isValid;

    QString m_scoring_uri;
    bool m_scoring_uri_isSet;
    bool m_scoring_uri_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBatchServiceResponse)

#endif // OAIBatchServiceResponse_H
