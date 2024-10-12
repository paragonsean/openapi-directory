/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIActiveDirectoryConfig.h
 *
 * Active Directory configuration
 */

#ifndef OAIActiveDirectoryConfig_H
#define OAIActiveDirectoryConfig_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIActiveDirectoryConfig : public OAIObject {
public:
    OAIActiveDirectoryConfig();
    OAIActiveDirectoryConfig(QString json);
    ~OAIActiveDirectoryConfig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAdExportGroup() const;
    void setAdExportGroup(const QString &ad_export_group);
    bool is_ad_export_group_Set() const;
    bool is_ad_export_group_Valid() const;

    QString getAlias() const;
    void setAlias(const QString &alias);
    bool is_alias_Set() const;
    bool is_alias_Valid() const;

    Q_DECL_DEPRECATED bool isCreateHomeFolder() const;
    Q_DECL_DEPRECATED void setCreateHomeFolder(const bool &create_home_folder);
    Q_DECL_DEPRECATED bool is_create_home_folder_Set() const;
    Q_DECL_DEPRECATED bool is_create_home_folder_Valid() const;

    Q_DECL_DEPRECATED qint64 getHomeFolderParent() const;
    Q_DECL_DEPRECATED void setHomeFolderParent(const qint64 &home_folder_parent);
    Q_DECL_DEPRECATED bool is_home_folder_parent_Set() const;
    Q_DECL_DEPRECATED bool is_home_folder_parent_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLdapUsersDomain() const;
    void setLdapUsersDomain(const QString &ldap_users_domain);
    bool is_ldap_users_domain_Set() const;
    bool is_ldap_users_domain_Valid() const;

    qint64 getSdsImportGroup() const;
    void setSdsImportGroup(const qint64 &sds_import_group);
    bool is_sds_import_group_Set() const;
    bool is_sds_import_group_Valid() const;

    QString getServerAdminName() const;
    void setServerAdminName(const QString &server_admin_name);
    bool is_server_admin_name_Set() const;
    bool is_server_admin_name_Valid() const;

    QString getServerIp() const;
    void setServerIp(const QString &server_ip);
    bool is_server_ip_Set() const;
    bool is_server_ip_Valid() const;

    qint32 getServerPort() const;
    void setServerPort(const qint32 &server_port);
    bool is_server_port_Set() const;
    bool is_server_port_Valid() const;

    QString getSslFingerPrint() const;
    void setSslFingerPrint(const QString &ssl_finger_print);
    bool is_ssl_finger_print_Set() const;
    bool is_ssl_finger_print_Valid() const;

    bool isUseLdaps() const;
    void setUseLdaps(const bool &use_ldaps);
    bool is_use_ldaps_Set() const;
    bool is_use_ldaps_Valid() const;

    QString getUserFilter() const;
    void setUserFilter(const QString &user_filter);
    bool is_user_filter_Set() const;
    bool is_user_filter_Valid() const;

    bool isUserImport() const;
    void setUserImport(const bool &user_import);
    bool is_user_import_Set() const;
    bool is_user_import_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_ad_export_group;
    bool m_ad_export_group_isSet;
    bool m_ad_export_group_isValid;

    QString m_alias;
    bool m_alias_isSet;
    bool m_alias_isValid;

    bool m_create_home_folder;
    bool m_create_home_folder_isSet;
    bool m_create_home_folder_isValid;

    qint64 m_home_folder_parent;
    bool m_home_folder_parent_isSet;
    bool m_home_folder_parent_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_ldap_users_domain;
    bool m_ldap_users_domain_isSet;
    bool m_ldap_users_domain_isValid;

    qint64 m_sds_import_group;
    bool m_sds_import_group_isSet;
    bool m_sds_import_group_isValid;

    QString m_server_admin_name;
    bool m_server_admin_name_isSet;
    bool m_server_admin_name_isValid;

    QString m_server_ip;
    bool m_server_ip_isSet;
    bool m_server_ip_isValid;

    qint32 m_server_port;
    bool m_server_port_isSet;
    bool m_server_port_isValid;

    QString m_ssl_finger_print;
    bool m_ssl_finger_print_isSet;
    bool m_ssl_finger_print_isValid;

    bool m_use_ldaps;
    bool m_use_ldaps_isSet;
    bool m_use_ldaps_isValid;

    QString m_user_filter;
    bool m_user_filter_isSet;
    bool m_user_filter_isValid;

    bool m_user_import;
    bool m_user_import_isSet;
    bool m_user_import_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIActiveDirectoryConfig)

#endif // OAIActiveDirectoryConfig_H
