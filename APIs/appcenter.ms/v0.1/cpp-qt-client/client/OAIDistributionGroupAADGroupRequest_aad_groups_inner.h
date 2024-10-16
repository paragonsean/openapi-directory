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
 * OAIDistributionGroupAADGroupRequest_aad_groups_inner.h
 *
 * 
 */

#ifndef OAIDistributionGroupAADGroupRequest_aad_groups_inner_H
#define OAIDistributionGroupAADGroupRequest_aad_groups_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDistributionGroupAADGroupRequest_aad_groups_inner : public OAIObject {
public:
    OAIDistributionGroupAADGroupRequest_aad_groups_inner();
    OAIDistributionGroupAADGroupRequest_aad_groups_inner(QString json);
    ~OAIDistributionGroupAADGroupRequest_aad_groups_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAadGroupId() const;
    void setAadGroupId(const QString &aad_group_id);
    bool is_aad_group_id_Set() const;
    bool is_aad_group_id_Valid() const;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_aad_group_id;
    bool m_aad_group_id_isSet;
    bool m_aad_group_id_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDistributionGroupAADGroupRequest_aad_groups_inner)

#endif // OAIDistributionGroupAADGroupRequest_aad_groups_inner_H
