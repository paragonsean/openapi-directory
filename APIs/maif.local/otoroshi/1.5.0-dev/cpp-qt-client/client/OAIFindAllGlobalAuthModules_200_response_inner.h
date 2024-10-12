/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFindAllGlobalAuthModules_200_response_inner.h
 *
 * 
 */

#ifndef OAIFindAllGlobalAuthModules_200_response_inner_H
#define OAIFindAllGlobalAuthModules_200_response_inner_H

#include <QJsonObject>

#include "OAIGenericOauth2ModuleConfig.h"
#include "OAIGenericOauth2ModuleConfig_jwtVerifier.h"
#include "OAIInMemoryAuthModuleConfig.h"
#include "OAIInMemoryUser.h"
#include "OAILdapAuthModuleConfig.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIInMemoryUser;
class OAIGenericOauth2ModuleConfig_jwtVerifier;

class OAIFindAllGlobalAuthModules_200_response_inner : public OAIObject {
public:
    OAIFindAllGlobalAuthModules_200_response_inner();
    OAIFindAllGlobalAuthModules_200_response_inner(QString json);
    ~OAIFindAllGlobalAuthModules_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAdminPassword() const;
    void setAdminPassword(const QString &admin_password);
    bool is_admin_password_Set() const;
    bool is_admin_password_Valid() const;

    QString getAdminUsername() const;
    void setAdminUsername(const QString &admin_username);
    bool is_admin_username_Set() const;
    bool is_admin_username_Valid() const;

    QString getDesc() const;
    void setDesc(const QString &desc);
    bool is_desc_Set() const;
    bool is_desc_Valid() const;

    QString getEmailField() const;
    void setEmailField(const QString &email_field);
    bool is_email_field_Set() const;
    bool is_email_field_Valid() const;

    QString getGroupFilter() const;
    void setGroupFilter(const QString &group_filter);
    bool is_group_filter_Set() const;
    bool is_group_filter_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getNameField() const;
    void setNameField(const QString &name_field);
    bool is_name_field_Set() const;
    bool is_name_field_Valid() const;

    QString getOtoroshiDataField() const;
    void setOtoroshiDataField(const QString &otoroshi_data_field);
    bool is_otoroshi_data_field_Set() const;
    bool is_otoroshi_data_field_Valid() const;

    QString getSearchBase() const;
    void setSearchBase(const QString &search_base);
    bool is_search_base_Set() const;
    bool is_search_base_Valid() const;

    QString getSearchFilter() const;
    void setSearchFilter(const QString &search_filter);
    bool is_search_filter_Set() const;
    bool is_search_filter_Valid() const;

    QString getServerUrl() const;
    void setServerUrl(const QString &server_url);
    bool is_server_url_Set() const;
    bool is_server_url_Valid() const;

    qint32 getSessionMaxAge() const;
    void setSessionMaxAge(const qint32 &session_max_age);
    bool is_session_max_age_Set() const;
    bool is_session_max_age_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUserBase() const;
    void setUserBase(const QString &user_base);
    bool is_user_base_Set() const;
    bool is_user_base_Valid() const;

    QList<OAIInMemoryUser> getUsers() const;
    void setUsers(const QList<OAIInMemoryUser> &users);
    bool is_users_Set() const;
    bool is_users_Valid() const;

    QString getAccessTokenField() const;
    void setAccessTokenField(const QString &access_token_field);
    bool is_access_token_field_Set() const;
    bool is_access_token_field_Valid() const;

    QString getAuthorizeUrl() const;
    void setAuthorizeUrl(const QString &authorize_url);
    bool is_authorize_url_Set() const;
    bool is_authorize_url_Valid() const;

    QString getCallbackUrl() const;
    void setCallbackUrl(const QString &callback_url);
    bool is_callback_url_Set() const;
    bool is_callback_url_Valid() const;

    QString getClaims() const;
    void setClaims(const QString &claims);
    bool is_claims_Set() const;
    bool is_claims_Valid() const;

    QString getClientId() const;
    void setClientId(const QString &client_id);
    bool is_client_id_Set() const;
    bool is_client_id_Valid() const;

    QString getClientSecret() const;
    void setClientSecret(const QString &client_secret);
    bool is_client_secret_Set() const;
    bool is_client_secret_Valid() const;

    OAIGenericOauth2ModuleConfig_jwtVerifier getJwtVerifier() const;
    void setJwtVerifier(const OAIGenericOauth2ModuleConfig_jwtVerifier &jwt_verifier);
    bool is_jwt_verifier_Set() const;
    bool is_jwt_verifier_Valid() const;

    QString getLoginUrl() const;
    void setLoginUrl(const QString &login_url);
    bool is_login_url_Set() const;
    bool is_login_url_Valid() const;

    QString getLogoutUrl() const;
    void setLogoutUrl(const QString &logout_url);
    bool is_logout_url_Set() const;
    bool is_logout_url_Valid() const;

    QString getOidConfig() const;
    void setOidConfig(const QString &oid_config);
    bool is_oid_config_Set() const;
    bool is_oid_config_Valid() const;

    bool isReadProfileFromToken() const;
    void setReadProfileFromToken(const bool &read_profile_from_token);
    bool is_read_profile_from_token_Set() const;
    bool is_read_profile_from_token_Valid() const;

    QString getScope() const;
    void setScope(const QString &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    QString getTokenUrl() const;
    void setTokenUrl(const QString &token_url);
    bool is_token_url_Set() const;
    bool is_token_url_Valid() const;

    bool isUseCookies() const;
    void setUseCookies(const bool &use_cookies);
    bool is_use_cookies_Set() const;
    bool is_use_cookies_Valid() const;

    bool isUseJson() const;
    void setUseJson(const bool &use_json);
    bool is_use_json_Set() const;
    bool is_use_json_Valid() const;

    QString getUserInfoUrl() const;
    void setUserInfoUrl(const QString &user_info_url);
    bool is_user_info_url_Set() const;
    bool is_user_info_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_admin_password;
    bool m_admin_password_isSet;
    bool m_admin_password_isValid;

    QString m_admin_username;
    bool m_admin_username_isSet;
    bool m_admin_username_isValid;

    QString m_desc;
    bool m_desc_isSet;
    bool m_desc_isValid;

    QString m_email_field;
    bool m_email_field_isSet;
    bool m_email_field_isValid;

    QString m_group_filter;
    bool m_group_filter_isSet;
    bool m_group_filter_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_name_field;
    bool m_name_field_isSet;
    bool m_name_field_isValid;

    QString m_otoroshi_data_field;
    bool m_otoroshi_data_field_isSet;
    bool m_otoroshi_data_field_isValid;

    QString m_search_base;
    bool m_search_base_isSet;
    bool m_search_base_isValid;

    QString m_search_filter;
    bool m_search_filter_isSet;
    bool m_search_filter_isValid;

    QString m_server_url;
    bool m_server_url_isSet;
    bool m_server_url_isValid;

    qint32 m_session_max_age;
    bool m_session_max_age_isSet;
    bool m_session_max_age_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_user_base;
    bool m_user_base_isSet;
    bool m_user_base_isValid;

    QList<OAIInMemoryUser> m_users;
    bool m_users_isSet;
    bool m_users_isValid;

    QString m_access_token_field;
    bool m_access_token_field_isSet;
    bool m_access_token_field_isValid;

    QString m_authorize_url;
    bool m_authorize_url_isSet;
    bool m_authorize_url_isValid;

    QString m_callback_url;
    bool m_callback_url_isSet;
    bool m_callback_url_isValid;

    QString m_claims;
    bool m_claims_isSet;
    bool m_claims_isValid;

    QString m_client_id;
    bool m_client_id_isSet;
    bool m_client_id_isValid;

    QString m_client_secret;
    bool m_client_secret_isSet;
    bool m_client_secret_isValid;

    OAIGenericOauth2ModuleConfig_jwtVerifier m_jwt_verifier;
    bool m_jwt_verifier_isSet;
    bool m_jwt_verifier_isValid;

    QString m_login_url;
    bool m_login_url_isSet;
    bool m_login_url_isValid;

    QString m_logout_url;
    bool m_logout_url_isSet;
    bool m_logout_url_isValid;

    QString m_oid_config;
    bool m_oid_config_isSet;
    bool m_oid_config_isValid;

    bool m_read_profile_from_token;
    bool m_read_profile_from_token_isSet;
    bool m_read_profile_from_token_isValid;

    QString m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;

    QString m_token_url;
    bool m_token_url_isSet;
    bool m_token_url_isValid;

    bool m_use_cookies;
    bool m_use_cookies_isSet;
    bool m_use_cookies_isValid;

    bool m_use_json;
    bool m_use_json_isSet;
    bool m_use_json_isValid;

    QString m_user_info_url;
    bool m_user_info_url_isSet;
    bool m_user_info_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFindAllGlobalAuthModules_200_response_inner)

#endif // OAIFindAllGlobalAuthModules_200_response_inner_H
