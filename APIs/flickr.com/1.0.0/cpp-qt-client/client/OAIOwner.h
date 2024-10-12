/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOwner.h
 *
 * 
 */

#ifndef OAIOwner_H
#define OAIOwner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOwner : public OAIObject {
public:
    OAIOwner();
    OAIOwner(QString json);
    ~OAIOwner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getIconfarm() const;
    void setIconfarm(const QString &iconfarm);
    bool is_iconfarm_Set() const;
    bool is_iconfarm_Valid() const;

    QString getIconserver() const;
    void setIconserver(const QString &iconserver);
    bool is_iconserver_Set() const;
    bool is_iconserver_Valid() const;

    bool isIsAdFree() const;
    void setIsAdFree(const bool &is_ad_free);
    bool is_is_ad_free_Set() const;
    bool is_is_ad_free_Valid() const;

    bool isIspro() const;
    void setIspro(const bool &ispro);
    bool is_ispro_Set() const;
    bool is_ispro_Valid() const;

    QString getLocation() const;
    void setLocation(const QString &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    bool isNoindexfollow() const;
    void setNoindexfollow(const bool &noindexfollow);
    bool is_noindexfollow_Set() const;
    bool is_noindexfollow_Valid() const;

    QString getNsid() const;
    void setNsid(const QString &nsid);
    bool is_nsid_Set() const;
    bool is_nsid_Valid() const;

    QString getPathAlias() const;
    void setPathAlias(const QString &path_alias);
    bool is_path_alias_Set() const;
    bool is_path_alias_Valid() const;

    QString getRealname() const;
    void setRealname(const QString &realname);
    bool is_realname_Set() const;
    bool is_realname_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_iconfarm;
    bool m_iconfarm_isSet;
    bool m_iconfarm_isValid;

    QString m_iconserver;
    bool m_iconserver_isSet;
    bool m_iconserver_isValid;

    bool m_is_ad_free;
    bool m_is_ad_free_isSet;
    bool m_is_ad_free_isValid;

    bool m_ispro;
    bool m_ispro_isSet;
    bool m_ispro_isValid;

    QString m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    bool m_noindexfollow;
    bool m_noindexfollow_isSet;
    bool m_noindexfollow_isValid;

    QString m_nsid;
    bool m_nsid_isSet;
    bool m_nsid_isValid;

    QString m_path_alias;
    bool m_path_alias_isSet;
    bool m_path_alias_isValid;

    QString m_realname;
    bool m_realname_isSet;
    bool m_realname_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOwner)

#endif // OAIOwner_H
