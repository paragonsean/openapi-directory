/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIArtistForSongContract.h
 *
 * 
 */

#ifndef OAIArtistForSongContract_H
#define OAIArtistForSongContract_H

#include <QJsonObject>

#include "OAIArtistCategories.h"
#include "OAIArtistContract.h"
#include "OAIArtistRoles.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIArtistContract;

class OAIArtistForSongContract : public OAIObject {
public:
    OAIArtistForSongContract();
    OAIArtistForSongContract(QString json);
    ~OAIArtistForSongContract() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIArtistContract getArtist() const;
    void setArtist(const OAIArtistContract &artist);
    bool is_artist_Set() const;
    bool is_artist_Valid() const;

    OAIArtistCategories getCategories() const;
    void setCategories(const OAIArtistCategories &categories);
    bool is_categories_Set() const;
    bool is_categories_Valid() const;

    OAIArtistRoles getEffectiveRoles() const;
    void setEffectiveRoles(const OAIArtistRoles &effective_roles);
    bool is_effective_roles_Set() const;
    bool is_effective_roles_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsCustomName() const;
    void setIsCustomName(const bool &is_custom_name);
    bool is_is_custom_name_Set() const;
    bool is_is_custom_name_Valid() const;

    bool isIsSupport() const;
    void setIsSupport(const bool &is_support);
    bool is_is_support_Set() const;
    bool is_is_support_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAIArtistRoles getRoles() const;
    void setRoles(const OAIArtistRoles &roles);
    bool is_roles_Set() const;
    bool is_roles_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIArtistContract m_artist;
    bool m_artist_isSet;
    bool m_artist_isValid;

    OAIArtistCategories m_categories;
    bool m_categories_isSet;
    bool m_categories_isValid;

    OAIArtistRoles m_effective_roles;
    bool m_effective_roles_isSet;
    bool m_effective_roles_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_custom_name;
    bool m_is_custom_name_isSet;
    bool m_is_custom_name_isValid;

    bool m_is_support;
    bool m_is_support_isSet;
    bool m_is_support_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAIArtistRoles m_roles;
    bool m_roles_isSet;
    bool m_roles_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArtistForSongContract)

#endif // OAIArtistForSongContract_H
