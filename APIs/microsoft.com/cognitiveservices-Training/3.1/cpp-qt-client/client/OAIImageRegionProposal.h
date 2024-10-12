/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImageRegionProposal.h
 *
 * 
 */

#ifndef OAIImageRegionProposal_H
#define OAIImageRegionProposal_H

#include <QJsonObject>

#include "OAIRegionProposal.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRegionProposal;

class OAIImageRegionProposal : public OAIObject {
public:
    OAIImageRegionProposal();
    OAIImageRegionProposal(QString json);
    ~OAIImageRegionProposal() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getImageId() const;
    void setImageId(const QString &image_id);
    bool is_image_id_Set() const;
    bool is_image_id_Valid() const;

    QString getProjectId() const;
    void setProjectId(const QString &project_id);
    bool is_project_id_Set() const;
    bool is_project_id_Valid() const;

    QList<OAIRegionProposal> getProposals() const;
    void setProposals(const QList<OAIRegionProposal> &proposals);
    bool is_proposals_Set() const;
    bool is_proposals_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_image_id;
    bool m_image_id_isSet;
    bool m_image_id_isValid;

    QString m_project_id;
    bool m_project_id_isSet;
    bool m_project_id_isValid;

    QList<OAIRegionProposal> m_proposals;
    bool m_proposals_isSet;
    bool m_proposals_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageRegionProposal)

#endif // OAIImageRegionProposal_H
