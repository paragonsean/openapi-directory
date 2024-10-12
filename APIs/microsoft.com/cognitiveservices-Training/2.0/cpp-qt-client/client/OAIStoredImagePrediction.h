/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIStoredImagePrediction.h
 *
 * result of an image classification request
 */

#ifndef OAIStoredImagePrediction_H
#define OAIStoredImagePrediction_H

#include <QJsonObject>

#include "OAIPrediction.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPrediction;

class OAIStoredImagePrediction : public OAIObject {
public:
    OAIStoredImagePrediction();
    OAIStoredImagePrediction(QString json);
    ~OAIStoredImagePrediction() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreated() const;
    void setCreated(const QDateTime &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    QString getDomain() const;
    void setDomain(const QString &domain);
    bool is_domain_Set() const;
    bool is_domain_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getImageUri() const;
    void setImageUri(const QString &image_uri);
    bool is_image_uri_Set() const;
    bool is_image_uri_Valid() const;

    QString getIteration() const;
    void setIteration(const QString &iteration);
    bool is_iteration_Set() const;
    bool is_iteration_Valid() const;

    QList<OAIPrediction> getPredictions() const;
    void setPredictions(const QList<OAIPrediction> &predictions);
    bool is_predictions_Set() const;
    bool is_predictions_Valid() const;

    QString getProject() const;
    void setProject(const QString &project);
    bool is_project_Set() const;
    bool is_project_Valid() const;

    QString getThumbnailUri() const;
    void setThumbnailUri(const QString &thumbnail_uri);
    bool is_thumbnail_uri_Set() const;
    bool is_thumbnail_uri_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    QString m_domain;
    bool m_domain_isSet;
    bool m_domain_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_image_uri;
    bool m_image_uri_isSet;
    bool m_image_uri_isValid;

    QString m_iteration;
    bool m_iteration_isSet;
    bool m_iteration_isValid;

    QList<OAIPrediction> m_predictions;
    bool m_predictions_isSet;
    bool m_predictions_isValid;

    QString m_project;
    bool m_project_isSet;
    bool m_project_isValid;

    QString m_thumbnail_uri;
    bool m_thumbnail_uri_isSet;
    bool m_thumbnail_uri_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStoredImagePrediction)

#endif // OAIStoredImagePrediction_H
