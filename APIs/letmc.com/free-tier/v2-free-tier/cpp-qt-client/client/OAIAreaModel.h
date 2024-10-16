/**
 * LetMC Api V2, Free (Tier 1)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-free-tier
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAreaModel.h
 *
 * Stores the information about a single property area.
 */

#ifndef OAIAreaModel_H
#define OAIAreaModel_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAreaModel : public OAIObject {
public:
    OAIAreaModel();
    OAIAreaModel(QString json);
    ~OAIAreaModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBranch() const;
    void setBranch(const QString &branch);
    bool is_branch_Set() const;
    bool is_branch_Valid() const;

    QString getETag() const;
    void setETag(const QString &e_tag);
    bool is_e_tag_Set() const;
    bool is_e_tag_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOid() const;
    void setOid(const QString &oid);
    bool is_oid_Set() const;
    bool is_oid_Valid() const;

    bool isShowOnSites() const;
    void setShowOnSites(const bool &show_on_sites);
    bool is_show_on_sites_Set() const;
    bool is_show_on_sites_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_branch;
    bool m_branch_isSet;
    bool m_branch_isValid;

    QString m_e_tag;
    bool m_e_tag_isSet;
    bool m_e_tag_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_oid;
    bool m_oid_isSet;
    bool m_oid_isValid;

    bool m_show_on_sites;
    bool m_show_on_sites_isSet;
    bool m_show_on_sites_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAreaModel)

#endif // OAIAreaModel_H
