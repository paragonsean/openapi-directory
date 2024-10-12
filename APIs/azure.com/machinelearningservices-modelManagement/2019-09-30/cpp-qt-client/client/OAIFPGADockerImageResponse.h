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

/*
 * OAIFPGADockerImageResponse.h
 *
 * The FPGA Docker Image response.
 */

#ifndef OAIFPGADockerImageResponse_H
#define OAIFPGADockerImageResponse_H

#include <QJsonObject>

#include "OAIImageResponseBase.h"
#include "OAIModel.h"
#include "OAIModelErrorResponse.h"
#include <QDateTime>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIModelErrorResponse;
class OAIModel;

class OAIFPGADockerImageResponse : public OAIObject {
public:
    OAIFPGADockerImageResponse();
    OAIFPGADockerImageResponse(QString json);
    ~OAIFPGADockerImageResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAutoDelete() const;
    void setAutoDelete(const bool &auto_delete);
    bool is_auto_delete_Set() const;
    bool is_auto_delete_Valid() const;

    QDateTime getCreatedTime() const;
    void setCreatedTime(const QDateTime &created_time);
    bool is_created_time_Set() const;
    bool is_created_time_Valid() const;

    QString getCreationState() const;
    void setCreationState(const QString &creation_state);
    bool is_creation_state_Set() const;
    bool is_creation_state_Valid() const;

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

    QString getImageBuildLogUri() const;
    void setImageBuildLogUri(const QString &image_build_log_uri);
    bool is_image_build_log_uri_Set() const;
    bool is_image_build_log_uri_Valid() const;

    QString getImageFlavor() const;
    void setImageFlavor(const QString &image_flavor);
    bool is_image_flavor_Set() const;
    bool is_image_flavor_Valid() const;

    QString getImageLocation() const;
    void setImageLocation(const QString &image_location);
    bool is_image_location_Set() const;
    bool is_image_location_Valid() const;

    QString getImageType() const;
    void setImageType(const QString &image_type);
    bool is_image_type_Set() const;
    bool is_image_type_Valid() const;

    QMap<QString, QString> getKvTags() const;
    void setKvTags(const QMap<QString, QString> &kv_tags);
    bool is_kv_tags_Set() const;
    bool is_kv_tags_Valid() const;

    QList<OAIModel> getModelDetails() const;
    void setModelDetails(const QList<OAIModel> &model_details);
    bool is_model_details_Set() const;
    bool is_model_details_Valid() const;

    QList<QString> getModelIds() const;
    void setModelIds(const QList<QString> &model_ids);
    bool is_model_ids_Set() const;
    bool is_model_ids_Valid() const;

    QDateTime getModifiedTime() const;
    void setModifiedTime(const QDateTime &modified_time);
    bool is_modified_time_Set() const;
    bool is_modified_time_Valid() const;

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

    qint64 getVersion() const;
    void setVersion(const qint64 &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_auto_delete;
    bool m_auto_delete_isSet;
    bool m_auto_delete_isValid;

    QDateTime m_created_time;
    bool m_created_time_isSet;
    bool m_created_time_isValid;

    QString m_creation_state;
    bool m_creation_state_isSet;
    bool m_creation_state_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAIModelErrorResponse m_error;
    bool m_error_isSet;
    bool m_error_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_image_build_log_uri;
    bool m_image_build_log_uri_isSet;
    bool m_image_build_log_uri_isValid;

    QString m_image_flavor;
    bool m_image_flavor_isSet;
    bool m_image_flavor_isValid;

    QString m_image_location;
    bool m_image_location_isSet;
    bool m_image_location_isValid;

    QString m_image_type;
    bool m_image_type_isSet;
    bool m_image_type_isValid;

    QMap<QString, QString> m_kv_tags;
    bool m_kv_tags_isSet;
    bool m_kv_tags_isValid;

    QList<OAIModel> m_model_details;
    bool m_model_details_isSet;
    bool m_model_details_isValid;

    QList<QString> m_model_ids;
    bool m_model_ids_isSet;
    bool m_model_ids_isValid;

    QDateTime m_modified_time;
    bool m_modified_time_isSet;
    bool m_modified_time_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_operation_id;
    bool m_operation_id_isSet;
    bool m_operation_id_isValid;

    QMap<QString, QString> m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    qint64 m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFPGADockerImageResponse)

#endif // OAIFPGADockerImageResponse_H
