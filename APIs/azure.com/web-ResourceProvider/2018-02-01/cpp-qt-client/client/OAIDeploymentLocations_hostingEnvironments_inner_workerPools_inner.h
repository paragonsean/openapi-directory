/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDeploymentLocations_hostingEnvironments_inner_workerPools_inner.h
 *
 * Worker pool of an App Service Environment.
 */

#ifndef OAIDeploymentLocations_hostingEnvironments_inner_workerPools_inner_H
#define OAIDeploymentLocations_hostingEnvironments_inner_workerPools_inner_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDeploymentLocations_hostingEnvironments_inner_workerPools_inner : public OAIObject {
public:
    OAIDeploymentLocations_hostingEnvironments_inner_workerPools_inner();
    OAIDeploymentLocations_hostingEnvironments_inner_workerPools_inner(QString json);
    ~OAIDeploymentLocations_hostingEnvironments_inner_workerPools_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getComputeMode() const;
    void setComputeMode(const QString &compute_mode);
    bool is_compute_mode_Set() const;
    bool is_compute_mode_Valid() const;

    QList<QString> getInstanceNames() const;
    void setInstanceNames(const QList<QString> &instance_names);
    bool is_instance_names_Set() const;
    bool is_instance_names_Valid() const;

    qint32 getWorkerCount() const;
    void setWorkerCount(const qint32 &worker_count);
    bool is_worker_count_Set() const;
    bool is_worker_count_Valid() const;

    QString getWorkerSize() const;
    void setWorkerSize(const QString &worker_size);
    bool is_worker_size_Set() const;
    bool is_worker_size_Valid() const;

    qint32 getWorkerSizeId() const;
    void setWorkerSizeId(const qint32 &worker_size_id);
    bool is_worker_size_id_Set() const;
    bool is_worker_size_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_compute_mode;
    bool m_compute_mode_isSet;
    bool m_compute_mode_isValid;

    QList<QString> m_instance_names;
    bool m_instance_names_isSet;
    bool m_instance_names_isValid;

    qint32 m_worker_count;
    bool m_worker_count_isSet;
    bool m_worker_count_isValid;

    QString m_worker_size;
    bool m_worker_size_isSet;
    bool m_worker_size_isValid;

    qint32 m_worker_size_id;
    bool m_worker_size_id_isSet;
    bool m_worker_size_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDeploymentLocations_hostingEnvironments_inner_workerPools_inner)

#endif // OAIDeploymentLocations_hostingEnvironments_inner_workerPools_inner_H
