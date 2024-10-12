/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProjectExport.h
 *
 * Represents information about a project export.
 */

#ifndef OAIProjectExport_H
#define OAIProjectExport_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProjectExport : public OAIObject {
public:
    OAIProjectExport();
    OAIProjectExport(QString json);
    ~OAIProjectExport() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getEstimatedImportTimeInMs() const;
    void setEstimatedImportTimeInMs(const qint32 &estimated_import_time_in_ms);
    bool is_estimated_import_time_in_ms_Set() const;
    bool is_estimated_import_time_in_ms_Valid() const;

    qint32 getImageCount() const;
    void setImageCount(const qint32 &image_count);
    bool is_image_count_Set() const;
    bool is_image_count_Valid() const;

    qint32 getIterationCount() const;
    void setIterationCount(const qint32 &iteration_count);
    bool is_iteration_count_Set() const;
    bool is_iteration_count_Valid() const;

    qint32 getRegionCount() const;
    void setRegionCount(const qint32 &region_count);
    bool is_region_count_Set() const;
    bool is_region_count_Valid() const;

    qint32 getTagCount() const;
    void setTagCount(const qint32 &tag_count);
    bool is_tag_count_Set() const;
    bool is_tag_count_Valid() const;

    QString getToken() const;
    void setToken(const QString &token);
    bool is_token_Set() const;
    bool is_token_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_estimated_import_time_in_ms;
    bool m_estimated_import_time_in_ms_isSet;
    bool m_estimated_import_time_in_ms_isValid;

    qint32 m_image_count;
    bool m_image_count_isSet;
    bool m_image_count_isValid;

    qint32 m_iteration_count;
    bool m_iteration_count_isSet;
    bool m_iteration_count_isValid;

    qint32 m_region_count;
    bool m_region_count_isSet;
    bool m_region_count_isValid;

    qint32 m_tag_count;
    bool m_tag_count_isSet;
    bool m_tag_count_isValid;

    QString m_token;
    bool m_token_isSet;
    bool m_token_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjectExport)

#endif // OAIProjectExport_H
