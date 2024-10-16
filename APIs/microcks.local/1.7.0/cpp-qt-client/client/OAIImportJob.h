/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImportJob.h
 *
 * An ImportJob allow defining a repository artifact to poll for discovering Services and APIs mocks and tests
 */

#ifndef OAIImportJob_H
#define OAIImportJob_H

#include <QJsonObject>

#include "OAIMetadata.h"
#include "OAISecretRef.h"
#include "OAIServiceRef.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMetadata;
class OAISecretRef;
class OAIServiceRef;

class OAIImportJob : public OAIObject {
public:
    OAIImportJob();
    OAIImportJob(QString json);
    ~OAIImportJob() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isActive() const;
    void setActive(const bool &active);
    bool is_active_Set() const;
    bool is_active_Valid() const;

    QDateTime getCreatedDate() const;
    void setCreatedDate(const QDateTime &created_date);
    bool is_created_date_Set() const;
    bool is_created_date_Valid() const;

    QString getEtag() const;
    void setEtag(const QString &etag);
    bool is_etag_Set() const;
    bool is_etag_Valid() const;

    QString getFrequency() const;
    void setFrequency(const QString &frequency);
    bool is_frequency_Set() const;
    bool is_frequency_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QDateTime getLastImportDate() const;
    void setLastImportDate(const QDateTime &last_import_date);
    bool is_last_import_date_Set() const;
    bool is_last_import_date_Valid() const;

    QString getLastImportError() const;
    void setLastImportError(const QString &last_import_error);
    bool is_last_import_error_Set() const;
    bool is_last_import_error_Valid() const;

    bool isMainArtifact() const;
    void setMainArtifact(const bool &main_artifact);
    bool is_main_artifact_Set() const;
    bool is_main_artifact_Valid() const;

    OAIMetadata getMetadata() const;
    void setMetadata(const OAIMetadata &metadata);
    bool is_metadata_Set() const;
    bool is_metadata_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    bool isRepositoryDisableSslValidation() const;
    void setRepositoryDisableSslValidation(const bool &repository_disable_ssl_validation);
    bool is_repository_disable_ssl_validation_Set() const;
    bool is_repository_disable_ssl_validation_Valid() const;

    QString getRepositoryUrl() const;
    void setRepositoryUrl(const QString &repository_url);
    bool is_repository_url_Set() const;
    bool is_repository_url_Valid() const;

    OAISecretRef getSecretRef() const;
    void setSecretRef(const OAISecretRef &secret_ref);
    bool is_secret_ref_Set() const;
    bool is_secret_ref_Valid() const;

    QList<OAIServiceRef> getServiceRefs() const;
    void setServiceRefs(const QList<OAIServiceRef> &service_refs);
    bool is_service_refs_Set() const;
    bool is_service_refs_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_active;
    bool m_active_isSet;
    bool m_active_isValid;

    QDateTime m_created_date;
    bool m_created_date_isSet;
    bool m_created_date_isValid;

    QString m_etag;
    bool m_etag_isSet;
    bool m_etag_isValid;

    QString m_frequency;
    bool m_frequency_isSet;
    bool m_frequency_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QDateTime m_last_import_date;
    bool m_last_import_date_isSet;
    bool m_last_import_date_isValid;

    QString m_last_import_error;
    bool m_last_import_error_isSet;
    bool m_last_import_error_isValid;

    bool m_main_artifact;
    bool m_main_artifact_isSet;
    bool m_main_artifact_isValid;

    OAIMetadata m_metadata;
    bool m_metadata_isSet;
    bool m_metadata_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    bool m_repository_disable_ssl_validation;
    bool m_repository_disable_ssl_validation_isSet;
    bool m_repository_disable_ssl_validation_isValid;

    QString m_repository_url;
    bool m_repository_url_isSet;
    bool m_repository_url_isValid;

    OAISecretRef m_secret_ref;
    bool m_secret_ref_isSet;
    bool m_secret_ref_isValid;

    QList<OAIServiceRef> m_service_refs;
    bool m_service_refs_isSet;
    bool m_service_refs_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImportJob)

#endif // OAIImportJob_H
