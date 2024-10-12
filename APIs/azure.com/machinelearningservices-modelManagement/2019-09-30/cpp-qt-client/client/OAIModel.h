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
 * OAIModel.h
 *
 * An Azure Machine Learning Model.
 */

#ifndef OAIModel_H
#define OAIModel_H

#include <QJsonObject>

#include "OAIDatasetReference.h"
#include <QDateTime>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDatasetReference;

class OAIModel : public OAIObject {
public:
    OAIModel();
    OAIModel(QString json);
    ~OAIModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreatedTime() const;
    void setCreatedTime(const QDateTime &created_time);
    bool is_created_time_Set() const;
    bool is_created_time_Valid() const;

    QList<OAIDatasetReference> getDatasets() const;
    void setDatasets(const QList<OAIDatasetReference> &datasets);
    bool is_datasets_Set() const;
    bool is_datasets_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getExperimentName() const;
    void setExperimentName(const QString &experiment_name);
    bool is_experiment_name_Set() const;
    bool is_experiment_name_Valid() const;

    QString getFramework() const;
    void setFramework(const QString &framework);
    bool is_framework_Set() const;
    bool is_framework_Valid() const;

    QString getFrameworkVersion() const;
    void setFrameworkVersion(const QString &framework_version);
    bool is_framework_version_Set() const;
    bool is_framework_version_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QMap<QString, QString> getKvTags() const;
    void setKvTags(const QMap<QString, QString> &kv_tags);
    bool is_kv_tags_Set() const;
    bool is_kv_tags_Valid() const;

    QString getMimeType() const;
    void setMimeType(const QString &mime_type);
    bool is_mime_type_Set() const;
    bool is_mime_type_Valid() const;

    QDateTime getModifiedTime() const;
    void setModifiedTime(const QDateTime &modified_time);
    bool is_modified_time_Set() const;
    bool is_modified_time_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getParentModelId() const;
    void setParentModelId(const QString &parent_model_id);
    bool is_parent_model_id_Set() const;
    bool is_parent_model_id_Valid() const;

    QMap<QString, QString> getProperties() const;
    void setProperties(const QMap<QString, QString> &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getRunId() const;
    void setRunId(const QString &run_id);
    bool is_run_id_Set() const;
    bool is_run_id_Valid() const;

    bool isUnpack() const;
    void setUnpack(const bool &unpack);
    bool is_unpack_Set() const;
    bool is_unpack_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    qint64 getVersion() const;
    void setVersion(const qint64 &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created_time;
    bool m_created_time_isSet;
    bool m_created_time_isValid;

    QList<OAIDatasetReference> m_datasets;
    bool m_datasets_isSet;
    bool m_datasets_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_experiment_name;
    bool m_experiment_name_isSet;
    bool m_experiment_name_isValid;

    QString m_framework;
    bool m_framework_isSet;
    bool m_framework_isValid;

    QString m_framework_version;
    bool m_framework_version_isSet;
    bool m_framework_version_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QMap<QString, QString> m_kv_tags;
    bool m_kv_tags_isSet;
    bool m_kv_tags_isValid;

    QString m_mime_type;
    bool m_mime_type_isSet;
    bool m_mime_type_isValid;

    QDateTime m_modified_time;
    bool m_modified_time_isSet;
    bool m_modified_time_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_parent_model_id;
    bool m_parent_model_id_isSet;
    bool m_parent_model_id_isValid;

    QMap<QString, QString> m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_run_id;
    bool m_run_id_isSet;
    bool m_run_id_isValid;

    bool m_unpack;
    bool m_unpack_isSet;
    bool m_unpack_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;

    qint64 m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIModel)

#endif // OAIModel_H
