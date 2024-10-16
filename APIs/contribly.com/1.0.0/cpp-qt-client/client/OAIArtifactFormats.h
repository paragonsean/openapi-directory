/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIArtifactFormats.h
 *
 * 
 */

#ifndef OAIArtifactFormats_H
#define OAIArtifactFormats_H

#include <QJsonObject>

#include "OAIArtifactFormat.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIArtifactFormat;

class OAIArtifactFormats : public OAIObject {
public:
    OAIArtifactFormats();
    OAIArtifactFormats(QString json);
    ~OAIArtifactFormats() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIArtifactFormat> getContribution() const;
    void setContribution(const QList<OAIArtifactFormat> &contribution);
    bool is_contribution_Set() const;
    bool is_contribution_Valid() const;

    QList<OAIArtifactFormat> getCover() const;
    void setCover(const QList<OAIArtifactFormat> &cover);
    bool is_cover_Set() const;
    bool is_cover_Valid() const;

    QList<OAIArtifactFormat> getProfileImage() const;
    void setProfileImage(const QList<OAIArtifactFormat> &profile_image);
    bool is_profile_image_Set() const;
    bool is_profile_image_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIArtifactFormat> m_contribution;
    bool m_contribution_isSet;
    bool m_contribution_isValid;

    QList<OAIArtifactFormat> m_cover;
    bool m_cover_isSet;
    bool m_cover_isValid;

    QList<OAIArtifactFormat> m_profile_image;
    bool m_profile_image_isSet;
    bool m_profile_image_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArtifactFormats)

#endif // OAIArtifactFormats_H
