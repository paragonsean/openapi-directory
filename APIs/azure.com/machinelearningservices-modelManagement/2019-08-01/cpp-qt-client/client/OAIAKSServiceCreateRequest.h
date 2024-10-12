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
 * OAIAKSServiceCreateRequest.h
 *
 * The request to create an AKS service.
 */

#ifndef OAIAKSServiceCreateRequest_H
#define OAIAKSServiceCreateRequest_H

#include <QJsonObject>

#include "OAIAuthKeys.h"
#include "OAIAutoScaler.h"
#include "OAIContainerResourceRequirements.h"
#include "OAICreateEndpointVariantRequest.h"
#include "OAIEnvironmentImageRequest.h"
#include "OAILivenessProbeRequirements.h"
#include "OAIModelDataCollection.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEnvironmentImageRequest;
class OAIAuthKeys;
class OAIAutoScaler;
class OAIContainerResourceRequirements;
class OAIModelDataCollection;
class OAILivenessProbeRequirements;

class OAIAKSServiceCreateRequest : public OAIObject {
public:
    OAIAKSServiceCreateRequest();
    OAIAKSServiceCreateRequest(QString json);
    ~OAIAKSServiceCreateRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getComputeType() const;
    void setComputeType(const QString &compute_type);
    bool is_compute_type_Set() const;
    bool is_compute_type_Valid() const;

    QString getDeploymentType() const;
    void setDeploymentType(const QString &deployment_type);
    bool is_deployment_type_Set() const;
    bool is_deployment_type_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAIEnvironmentImageRequest getEnvironmentImageRequest() const;
    void setEnvironmentImageRequest(const OAIEnvironmentImageRequest &environment_image_request);
    bool is_environment_image_request_Set() const;
    bool is_environment_image_request_Valid() const;

    QString getImageId() const;
    void setImageId(const QString &image_id);
    bool is_image_id_Set() const;
    bool is_image_id_Valid() const;

    OAIAuthKeys getKeys() const;
    void setKeys(const OAIAuthKeys &keys);
    bool is_keys_Set() const;
    bool is_keys_Valid() const;

    QMap<QString, QString> getKvTags() const;
    void setKvTags(const QMap<QString, QString> &kv_tags);
    bool is_kv_tags_Set() const;
    bool is_kv_tags_Valid() const;

    QString getLocation() const;
    void setLocation(const QString &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QMap<QString, QString> getProperties() const;
    void setProperties(const QMap<QString, QString> &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    bool isIsDefault() const;
    void setIsDefault(const bool &is_default);
    bool is_is_default_Set() const;
    bool is_is_default_Valid() const;

    float getTrafficPercentile() const;
    void setTrafficPercentile(const float &traffic_percentile);
    bool is_traffic_percentile_Set() const;
    bool is_traffic_percentile_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    bool isAadAuthEnabled() const;
    void setAadAuthEnabled(const bool &aad_auth_enabled);
    bool is_aad_auth_enabled_Set() const;
    bool is_aad_auth_enabled_Valid() const;

    bool isAppInsightsEnabled() const;
    void setAppInsightsEnabled(const bool &app_insights_enabled);
    bool is_app_insights_enabled_Set() const;
    bool is_app_insights_enabled_Valid() const;

    bool isAuthEnabled() const;
    void setAuthEnabled(const bool &auth_enabled);
    bool is_auth_enabled_Set() const;
    bool is_auth_enabled_Valid() const;

    OAIAutoScaler getAutoScaler() const;
    void setAutoScaler(const OAIAutoScaler &auto_scaler);
    bool is_auto_scaler_Set() const;
    bool is_auto_scaler_Valid() const;

    QString getComputeName() const;
    void setComputeName(const QString &compute_name);
    bool is_compute_name_Set() const;
    bool is_compute_name_Valid() const;

    OAIContainerResourceRequirements getContainerResourceRequirements() const;
    void setContainerResourceRequirements(const OAIContainerResourceRequirements &container_resource_requirements);
    bool is_container_resource_requirements_Set() const;
    bool is_container_resource_requirements_Valid() const;

    OAIModelDataCollection getDataCollection() const;
    void setDataCollection(const OAIModelDataCollection &data_collection);
    bool is_data_collection_Set() const;
    bool is_data_collection_Valid() const;

    OAILivenessProbeRequirements getLivenessProbeRequirements() const;
    void setLivenessProbeRequirements(const OAILivenessProbeRequirements &liveness_probe_requirements);
    bool is_liveness_probe_requirements_Set() const;
    bool is_liveness_probe_requirements_Valid() const;

    qint32 getMaxConcurrentRequestsPerContainer() const;
    void setMaxConcurrentRequestsPerContainer(const qint32 &max_concurrent_requests_per_container);
    bool is_max_concurrent_requests_per_container_Set() const;
    bool is_max_concurrent_requests_per_container_Valid() const;

    qint32 getMaxQueueWaitMs() const;
    void setMaxQueueWaitMs(const qint32 &max_queue_wait_ms);
    bool is_max_queue_wait_ms_Set() const;
    bool is_max_queue_wait_ms_Valid() const;

    QString getRNamespace() const;
    void setRNamespace(const QString &r_namespace);
    bool is_r_namespace_Set() const;
    bool is_r_namespace_Valid() const;

    qint32 getNumReplicas() const;
    void setNumReplicas(const qint32 &num_replicas);
    bool is_num_replicas_Set() const;
    bool is_num_replicas_Valid() const;

    qint32 getScoringTimeoutMs() const;
    void setScoringTimeoutMs(const qint32 &scoring_timeout_ms);
    bool is_scoring_timeout_ms_Set() const;
    bool is_scoring_timeout_ms_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_compute_type;
    bool m_compute_type_isSet;
    bool m_compute_type_isValid;

    QString m_deployment_type;
    bool m_deployment_type_isSet;
    bool m_deployment_type_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAIEnvironmentImageRequest m_environment_image_request;
    bool m_environment_image_request_isSet;
    bool m_environment_image_request_isValid;

    QString m_image_id;
    bool m_image_id_isSet;
    bool m_image_id_isValid;

    OAIAuthKeys m_keys;
    bool m_keys_isSet;
    bool m_keys_isValid;

    QMap<QString, QString> m_kv_tags;
    bool m_kv_tags_isSet;
    bool m_kv_tags_isValid;

    QString m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QMap<QString, QString> m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    bool m_is_default;
    bool m_is_default_isSet;
    bool m_is_default_isValid;

    float m_traffic_percentile;
    bool m_traffic_percentile_isSet;
    bool m_traffic_percentile_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    bool m_aad_auth_enabled;
    bool m_aad_auth_enabled_isSet;
    bool m_aad_auth_enabled_isValid;

    bool m_app_insights_enabled;
    bool m_app_insights_enabled_isSet;
    bool m_app_insights_enabled_isValid;

    bool m_auth_enabled;
    bool m_auth_enabled_isSet;
    bool m_auth_enabled_isValid;

    OAIAutoScaler m_auto_scaler;
    bool m_auto_scaler_isSet;
    bool m_auto_scaler_isValid;

    QString m_compute_name;
    bool m_compute_name_isSet;
    bool m_compute_name_isValid;

    OAIContainerResourceRequirements m_container_resource_requirements;
    bool m_container_resource_requirements_isSet;
    bool m_container_resource_requirements_isValid;

    OAIModelDataCollection m_data_collection;
    bool m_data_collection_isSet;
    bool m_data_collection_isValid;

    OAILivenessProbeRequirements m_liveness_probe_requirements;
    bool m_liveness_probe_requirements_isSet;
    bool m_liveness_probe_requirements_isValid;

    qint32 m_max_concurrent_requests_per_container;
    bool m_max_concurrent_requests_per_container_isSet;
    bool m_max_concurrent_requests_per_container_isValid;

    qint32 m_max_queue_wait_ms;
    bool m_max_queue_wait_ms_isSet;
    bool m_max_queue_wait_ms_isValid;

    QString m_r_namespace;
    bool m_r_namespace_isSet;
    bool m_r_namespace_isValid;

    qint32 m_num_replicas;
    bool m_num_replicas_isSet;
    bool m_num_replicas_isValid;

    qint32 m_scoring_timeout_ms;
    bool m_scoring_timeout_ms_isSet;
    bool m_scoring_timeout_ms_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAKSServiceCreateRequest)

#endif // OAIAKSServiceCreateRequest_H
