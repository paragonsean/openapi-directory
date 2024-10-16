/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDistributionGroupAADGroupRequest.h
 *
 * 
 */

#ifndef OAIDistributionGroupAADGroupRequest_H
#define OAIDistributionGroupAADGroupRequest_H

#include <QJsonObject>

#include "OAIDistributionGroupAADGroupRequest_aad_groups_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDistributionGroupAADGroupRequest_aad_groups_inner;

class OAIDistributionGroupAADGroupRequest : public OAIObject {
public:
    OAIDistributionGroupAADGroupRequest();
    OAIDistributionGroupAADGroupRequest(QString json);
    ~OAIDistributionGroupAADGroupRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIDistributionGroupAADGroupRequest_aad_groups_inner> getAadGroups() const;
    void setAadGroups(const QList<OAIDistributionGroupAADGroupRequest_aad_groups_inner> &aad_groups);
    bool is_aad_groups_Set() const;
    bool is_aad_groups_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIDistributionGroupAADGroupRequest_aad_groups_inner> m_aad_groups;
    bool m_aad_groups_isSet;
    bool m_aad_groups_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDistributionGroupAADGroupRequest)

#endif // OAIDistributionGroupAADGroupRequest_H
