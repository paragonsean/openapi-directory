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

#include "OAIFindAllGlobalAuthModules_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFindAllGlobalAuthModules_200_response_inner::OAIFindAllGlobalAuthModules_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFindAllGlobalAuthModules_200_response_inner::OAIFindAllGlobalAuthModules_200_response_inner() {
    this->initializeModel();
}

OAIFindAllGlobalAuthModules_200_response_inner::~OAIFindAllGlobalAuthModules_200_response_inner() {}

void OAIFindAllGlobalAuthModules_200_response_inner::initializeModel() {

    m_admin_password_isSet = false;
    m_admin_password_isValid = false;

    m_admin_username_isSet = false;
    m_admin_username_isValid = false;

    m_desc_isSet = false;
    m_desc_isValid = false;

    m_email_field_isSet = false;
    m_email_field_isValid = false;

    m_group_filter_isSet = false;
    m_group_filter_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_name_field_isSet = false;
    m_name_field_isValid = false;

    m_otoroshi_data_field_isSet = false;
    m_otoroshi_data_field_isValid = false;

    m_search_base_isSet = false;
    m_search_base_isValid = false;

    m_search_filter_isSet = false;
    m_search_filter_isValid = false;

    m_server_url_isSet = false;
    m_server_url_isValid = false;

    m_session_max_age_isSet = false;
    m_session_max_age_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_user_base_isSet = false;
    m_user_base_isValid = false;

    m_users_isSet = false;
    m_users_isValid = false;

    m_access_token_field_isSet = false;
    m_access_token_field_isValid = false;

    m_authorize_url_isSet = false;
    m_authorize_url_isValid = false;

    m_callback_url_isSet = false;
    m_callback_url_isValid = false;

    m_claims_isSet = false;
    m_claims_isValid = false;

    m_client_id_isSet = false;
    m_client_id_isValid = false;

    m_client_secret_isSet = false;
    m_client_secret_isValid = false;

    m_jwt_verifier_isSet = false;
    m_jwt_verifier_isValid = false;

    m_login_url_isSet = false;
    m_login_url_isValid = false;

    m_logout_url_isSet = false;
    m_logout_url_isValid = false;

    m_oid_config_isSet = false;
    m_oid_config_isValid = false;

    m_read_profile_from_token_isSet = false;
    m_read_profile_from_token_isValid = false;

    m_scope_isSet = false;
    m_scope_isValid = false;

    m_token_url_isSet = false;
    m_token_url_isValid = false;

    m_use_cookies_isSet = false;
    m_use_cookies_isValid = false;

    m_use_json_isSet = false;
    m_use_json_isValid = false;

    m_user_info_url_isSet = false;
    m_user_info_url_isValid = false;
}

void OAIFindAllGlobalAuthModules_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFindAllGlobalAuthModules_200_response_inner::fromJsonObject(QJsonObject json) {

    m_admin_password_isValid = ::OpenAPI::fromJsonValue(m_admin_password, json[QString("adminPassword")]);
    m_admin_password_isSet = !json[QString("adminPassword")].isNull() && m_admin_password_isValid;

    m_admin_username_isValid = ::OpenAPI::fromJsonValue(m_admin_username, json[QString("adminUsername")]);
    m_admin_username_isSet = !json[QString("adminUsername")].isNull() && m_admin_username_isValid;

    m_desc_isValid = ::OpenAPI::fromJsonValue(m_desc, json[QString("desc")]);
    m_desc_isSet = !json[QString("desc")].isNull() && m_desc_isValid;

    m_email_field_isValid = ::OpenAPI::fromJsonValue(m_email_field, json[QString("emailField")]);
    m_email_field_isSet = !json[QString("emailField")].isNull() && m_email_field_isValid;

    m_group_filter_isValid = ::OpenAPI::fromJsonValue(m_group_filter, json[QString("groupFilter")]);
    m_group_filter_isSet = !json[QString("groupFilter")].isNull() && m_group_filter_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_name_field_isValid = ::OpenAPI::fromJsonValue(m_name_field, json[QString("nameField")]);
    m_name_field_isSet = !json[QString("nameField")].isNull() && m_name_field_isValid;

    m_otoroshi_data_field_isValid = ::OpenAPI::fromJsonValue(m_otoroshi_data_field, json[QString("otoroshiDataField")]);
    m_otoroshi_data_field_isSet = !json[QString("otoroshiDataField")].isNull() && m_otoroshi_data_field_isValid;

    m_search_base_isValid = ::OpenAPI::fromJsonValue(m_search_base, json[QString("searchBase")]);
    m_search_base_isSet = !json[QString("searchBase")].isNull() && m_search_base_isValid;

    m_search_filter_isValid = ::OpenAPI::fromJsonValue(m_search_filter, json[QString("searchFilter")]);
    m_search_filter_isSet = !json[QString("searchFilter")].isNull() && m_search_filter_isValid;

    m_server_url_isValid = ::OpenAPI::fromJsonValue(m_server_url, json[QString("serverUrl")]);
    m_server_url_isSet = !json[QString("serverUrl")].isNull() && m_server_url_isValid;

    m_session_max_age_isValid = ::OpenAPI::fromJsonValue(m_session_max_age, json[QString("sessionMaxAge")]);
    m_session_max_age_isSet = !json[QString("sessionMaxAge")].isNull() && m_session_max_age_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_user_base_isValid = ::OpenAPI::fromJsonValue(m_user_base, json[QString("userBase")]);
    m_user_base_isSet = !json[QString("userBase")].isNull() && m_user_base_isValid;

    m_users_isValid = ::OpenAPI::fromJsonValue(m_users, json[QString("users")]);
    m_users_isSet = !json[QString("users")].isNull() && m_users_isValid;

    m_access_token_field_isValid = ::OpenAPI::fromJsonValue(m_access_token_field, json[QString("accessTokenField")]);
    m_access_token_field_isSet = !json[QString("accessTokenField")].isNull() && m_access_token_field_isValid;

    m_authorize_url_isValid = ::OpenAPI::fromJsonValue(m_authorize_url, json[QString("authorizeUrl")]);
    m_authorize_url_isSet = !json[QString("authorizeUrl")].isNull() && m_authorize_url_isValid;

    m_callback_url_isValid = ::OpenAPI::fromJsonValue(m_callback_url, json[QString("callbackUrl")]);
    m_callback_url_isSet = !json[QString("callbackUrl")].isNull() && m_callback_url_isValid;

    m_claims_isValid = ::OpenAPI::fromJsonValue(m_claims, json[QString("claims")]);
    m_claims_isSet = !json[QString("claims")].isNull() && m_claims_isValid;

    m_client_id_isValid = ::OpenAPI::fromJsonValue(m_client_id, json[QString("clientId")]);
    m_client_id_isSet = !json[QString("clientId")].isNull() && m_client_id_isValid;

    m_client_secret_isValid = ::OpenAPI::fromJsonValue(m_client_secret, json[QString("clientSecret")]);
    m_client_secret_isSet = !json[QString("clientSecret")].isNull() && m_client_secret_isValid;

    m_jwt_verifier_isValid = ::OpenAPI::fromJsonValue(m_jwt_verifier, json[QString("jwtVerifier")]);
    m_jwt_verifier_isSet = !json[QString("jwtVerifier")].isNull() && m_jwt_verifier_isValid;

    m_login_url_isValid = ::OpenAPI::fromJsonValue(m_login_url, json[QString("loginUrl")]);
    m_login_url_isSet = !json[QString("loginUrl")].isNull() && m_login_url_isValid;

    m_logout_url_isValid = ::OpenAPI::fromJsonValue(m_logout_url, json[QString("logoutUrl")]);
    m_logout_url_isSet = !json[QString("logoutUrl")].isNull() && m_logout_url_isValid;

    m_oid_config_isValid = ::OpenAPI::fromJsonValue(m_oid_config, json[QString("oidConfig")]);
    m_oid_config_isSet = !json[QString("oidConfig")].isNull() && m_oid_config_isValid;

    m_read_profile_from_token_isValid = ::OpenAPI::fromJsonValue(m_read_profile_from_token, json[QString("readProfileFromToken")]);
    m_read_profile_from_token_isSet = !json[QString("readProfileFromToken")].isNull() && m_read_profile_from_token_isValid;

    m_scope_isValid = ::OpenAPI::fromJsonValue(m_scope, json[QString("scope")]);
    m_scope_isSet = !json[QString("scope")].isNull() && m_scope_isValid;

    m_token_url_isValid = ::OpenAPI::fromJsonValue(m_token_url, json[QString("tokenUrl")]);
    m_token_url_isSet = !json[QString("tokenUrl")].isNull() && m_token_url_isValid;

    m_use_cookies_isValid = ::OpenAPI::fromJsonValue(m_use_cookies, json[QString("useCookies")]);
    m_use_cookies_isSet = !json[QString("useCookies")].isNull() && m_use_cookies_isValid;

    m_use_json_isValid = ::OpenAPI::fromJsonValue(m_use_json, json[QString("useJson")]);
    m_use_json_isSet = !json[QString("useJson")].isNull() && m_use_json_isValid;

    m_user_info_url_isValid = ::OpenAPI::fromJsonValue(m_user_info_url, json[QString("userInfoUrl")]);
    m_user_info_url_isSet = !json[QString("userInfoUrl")].isNull() && m_user_info_url_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFindAllGlobalAuthModules_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_admin_password_isSet) {
        obj.insert(QString("adminPassword"), ::OpenAPI::toJsonValue(m_admin_password));
    }
    if (m_admin_username_isSet) {
        obj.insert(QString("adminUsername"), ::OpenAPI::toJsonValue(m_admin_username));
    }
    if (m_desc_isSet) {
        obj.insert(QString("desc"), ::OpenAPI::toJsonValue(m_desc));
    }
    if (m_email_field_isSet) {
        obj.insert(QString("emailField"), ::OpenAPI::toJsonValue(m_email_field));
    }
    if (m_group_filter_isSet) {
        obj.insert(QString("groupFilter"), ::OpenAPI::toJsonValue(m_group_filter));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_name_field_isSet) {
        obj.insert(QString("nameField"), ::OpenAPI::toJsonValue(m_name_field));
    }
    if (m_otoroshi_data_field_isSet) {
        obj.insert(QString("otoroshiDataField"), ::OpenAPI::toJsonValue(m_otoroshi_data_field));
    }
    if (m_search_base_isSet) {
        obj.insert(QString("searchBase"), ::OpenAPI::toJsonValue(m_search_base));
    }
    if (m_search_filter_isSet) {
        obj.insert(QString("searchFilter"), ::OpenAPI::toJsonValue(m_search_filter));
    }
    if (m_server_url_isSet) {
        obj.insert(QString("serverUrl"), ::OpenAPI::toJsonValue(m_server_url));
    }
    if (m_session_max_age_isSet) {
        obj.insert(QString("sessionMaxAge"), ::OpenAPI::toJsonValue(m_session_max_age));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_user_base_isSet) {
        obj.insert(QString("userBase"), ::OpenAPI::toJsonValue(m_user_base));
    }
    if (m_users.size() > 0) {
        obj.insert(QString("users"), ::OpenAPI::toJsonValue(m_users));
    }
    if (m_access_token_field_isSet) {
        obj.insert(QString("accessTokenField"), ::OpenAPI::toJsonValue(m_access_token_field));
    }
    if (m_authorize_url_isSet) {
        obj.insert(QString("authorizeUrl"), ::OpenAPI::toJsonValue(m_authorize_url));
    }
    if (m_callback_url_isSet) {
        obj.insert(QString("callbackUrl"), ::OpenAPI::toJsonValue(m_callback_url));
    }
    if (m_claims_isSet) {
        obj.insert(QString("claims"), ::OpenAPI::toJsonValue(m_claims));
    }
    if (m_client_id_isSet) {
        obj.insert(QString("clientId"), ::OpenAPI::toJsonValue(m_client_id));
    }
    if (m_client_secret_isSet) {
        obj.insert(QString("clientSecret"), ::OpenAPI::toJsonValue(m_client_secret));
    }
    if (m_jwt_verifier.isSet()) {
        obj.insert(QString("jwtVerifier"), ::OpenAPI::toJsonValue(m_jwt_verifier));
    }
    if (m_login_url_isSet) {
        obj.insert(QString("loginUrl"), ::OpenAPI::toJsonValue(m_login_url));
    }
    if (m_logout_url_isSet) {
        obj.insert(QString("logoutUrl"), ::OpenAPI::toJsonValue(m_logout_url));
    }
    if (m_oid_config_isSet) {
        obj.insert(QString("oidConfig"), ::OpenAPI::toJsonValue(m_oid_config));
    }
    if (m_read_profile_from_token_isSet) {
        obj.insert(QString("readProfileFromToken"), ::OpenAPI::toJsonValue(m_read_profile_from_token));
    }
    if (m_scope_isSet) {
        obj.insert(QString("scope"), ::OpenAPI::toJsonValue(m_scope));
    }
    if (m_token_url_isSet) {
        obj.insert(QString("tokenUrl"), ::OpenAPI::toJsonValue(m_token_url));
    }
    if (m_use_cookies_isSet) {
        obj.insert(QString("useCookies"), ::OpenAPI::toJsonValue(m_use_cookies));
    }
    if (m_use_json_isSet) {
        obj.insert(QString("useJson"), ::OpenAPI::toJsonValue(m_use_json));
    }
    if (m_user_info_url_isSet) {
        obj.insert(QString("userInfoUrl"), ::OpenAPI::toJsonValue(m_user_info_url));
    }
    return obj;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getAdminPassword() const {
    return m_admin_password;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setAdminPassword(const QString &admin_password) {
    m_admin_password = admin_password;
    m_admin_password_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_admin_password_Set() const{
    return m_admin_password_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_admin_password_Valid() const{
    return m_admin_password_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getAdminUsername() const {
    return m_admin_username;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setAdminUsername(const QString &admin_username) {
    m_admin_username = admin_username;
    m_admin_username_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_admin_username_Set() const{
    return m_admin_username_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_admin_username_Valid() const{
    return m_admin_username_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getDesc() const {
    return m_desc;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setDesc(const QString &desc) {
    m_desc = desc;
    m_desc_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_desc_Set() const{
    return m_desc_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_desc_Valid() const{
    return m_desc_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getEmailField() const {
    return m_email_field;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setEmailField(const QString &email_field) {
    m_email_field = email_field;
    m_email_field_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_email_field_Set() const{
    return m_email_field_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_email_field_Valid() const{
    return m_email_field_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getGroupFilter() const {
    return m_group_filter;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setGroupFilter(const QString &group_filter) {
    m_group_filter = group_filter;
    m_group_filter_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_group_filter_Set() const{
    return m_group_filter_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_group_filter_Valid() const{
    return m_group_filter_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getId() const {
    return m_id;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getName() const {
    return m_name;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getNameField() const {
    return m_name_field;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setNameField(const QString &name_field) {
    m_name_field = name_field;
    m_name_field_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_name_field_Set() const{
    return m_name_field_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_name_field_Valid() const{
    return m_name_field_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getOtoroshiDataField() const {
    return m_otoroshi_data_field;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setOtoroshiDataField(const QString &otoroshi_data_field) {
    m_otoroshi_data_field = otoroshi_data_field;
    m_otoroshi_data_field_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_otoroshi_data_field_Set() const{
    return m_otoroshi_data_field_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_otoroshi_data_field_Valid() const{
    return m_otoroshi_data_field_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getSearchBase() const {
    return m_search_base;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setSearchBase(const QString &search_base) {
    m_search_base = search_base;
    m_search_base_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_search_base_Set() const{
    return m_search_base_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_search_base_Valid() const{
    return m_search_base_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getSearchFilter() const {
    return m_search_filter;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setSearchFilter(const QString &search_filter) {
    m_search_filter = search_filter;
    m_search_filter_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_search_filter_Set() const{
    return m_search_filter_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_search_filter_Valid() const{
    return m_search_filter_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getServerUrl() const {
    return m_server_url;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setServerUrl(const QString &server_url) {
    m_server_url = server_url;
    m_server_url_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_server_url_Set() const{
    return m_server_url_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_server_url_Valid() const{
    return m_server_url_isValid;
}

qint32 OAIFindAllGlobalAuthModules_200_response_inner::getSessionMaxAge() const {
    return m_session_max_age;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setSessionMaxAge(const qint32 &session_max_age) {
    m_session_max_age = session_max_age;
    m_session_max_age_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_session_max_age_Set() const{
    return m_session_max_age_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_session_max_age_Valid() const{
    return m_session_max_age_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getType() const {
    return m_type;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getUserBase() const {
    return m_user_base;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setUserBase(const QString &user_base) {
    m_user_base = user_base;
    m_user_base_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_user_base_Set() const{
    return m_user_base_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_user_base_Valid() const{
    return m_user_base_isValid;
}

QList<OAIInMemoryUser> OAIFindAllGlobalAuthModules_200_response_inner::getUsers() const {
    return m_users;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setUsers(const QList<OAIInMemoryUser> &users) {
    m_users = users;
    m_users_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_users_Set() const{
    return m_users_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_users_Valid() const{
    return m_users_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getAccessTokenField() const {
    return m_access_token_field;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setAccessTokenField(const QString &access_token_field) {
    m_access_token_field = access_token_field;
    m_access_token_field_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_access_token_field_Set() const{
    return m_access_token_field_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_access_token_field_Valid() const{
    return m_access_token_field_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getAuthorizeUrl() const {
    return m_authorize_url;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setAuthorizeUrl(const QString &authorize_url) {
    m_authorize_url = authorize_url;
    m_authorize_url_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_authorize_url_Set() const{
    return m_authorize_url_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_authorize_url_Valid() const{
    return m_authorize_url_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getCallbackUrl() const {
    return m_callback_url;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setCallbackUrl(const QString &callback_url) {
    m_callback_url = callback_url;
    m_callback_url_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_callback_url_Set() const{
    return m_callback_url_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_callback_url_Valid() const{
    return m_callback_url_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getClaims() const {
    return m_claims;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setClaims(const QString &claims) {
    m_claims = claims;
    m_claims_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_claims_Set() const{
    return m_claims_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_claims_Valid() const{
    return m_claims_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getClientId() const {
    return m_client_id;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setClientId(const QString &client_id) {
    m_client_id = client_id;
    m_client_id_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_client_id_Set() const{
    return m_client_id_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_client_id_Valid() const{
    return m_client_id_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getClientSecret() const {
    return m_client_secret;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setClientSecret(const QString &client_secret) {
    m_client_secret = client_secret;
    m_client_secret_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_client_secret_Set() const{
    return m_client_secret_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_client_secret_Valid() const{
    return m_client_secret_isValid;
}

OAIGenericOauth2ModuleConfig_jwtVerifier OAIFindAllGlobalAuthModules_200_response_inner::getJwtVerifier() const {
    return m_jwt_verifier;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setJwtVerifier(const OAIGenericOauth2ModuleConfig_jwtVerifier &jwt_verifier) {
    m_jwt_verifier = jwt_verifier;
    m_jwt_verifier_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_jwt_verifier_Set() const{
    return m_jwt_verifier_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_jwt_verifier_Valid() const{
    return m_jwt_verifier_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getLoginUrl() const {
    return m_login_url;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setLoginUrl(const QString &login_url) {
    m_login_url = login_url;
    m_login_url_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_login_url_Set() const{
    return m_login_url_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_login_url_Valid() const{
    return m_login_url_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getLogoutUrl() const {
    return m_logout_url;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setLogoutUrl(const QString &logout_url) {
    m_logout_url = logout_url;
    m_logout_url_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_logout_url_Set() const{
    return m_logout_url_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_logout_url_Valid() const{
    return m_logout_url_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getOidConfig() const {
    return m_oid_config;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setOidConfig(const QString &oid_config) {
    m_oid_config = oid_config;
    m_oid_config_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_oid_config_Set() const{
    return m_oid_config_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_oid_config_Valid() const{
    return m_oid_config_isValid;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::isReadProfileFromToken() const {
    return m_read_profile_from_token;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setReadProfileFromToken(const bool &read_profile_from_token) {
    m_read_profile_from_token = read_profile_from_token;
    m_read_profile_from_token_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_read_profile_from_token_Set() const{
    return m_read_profile_from_token_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_read_profile_from_token_Valid() const{
    return m_read_profile_from_token_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getScope() const {
    return m_scope;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setScope(const QString &scope) {
    m_scope = scope;
    m_scope_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_scope_Set() const{
    return m_scope_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_scope_Valid() const{
    return m_scope_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getTokenUrl() const {
    return m_token_url;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setTokenUrl(const QString &token_url) {
    m_token_url = token_url;
    m_token_url_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_token_url_Set() const{
    return m_token_url_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_token_url_Valid() const{
    return m_token_url_isValid;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::isUseCookies() const {
    return m_use_cookies;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setUseCookies(const bool &use_cookies) {
    m_use_cookies = use_cookies;
    m_use_cookies_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_use_cookies_Set() const{
    return m_use_cookies_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_use_cookies_Valid() const{
    return m_use_cookies_isValid;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::isUseJson() const {
    return m_use_json;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setUseJson(const bool &use_json) {
    m_use_json = use_json;
    m_use_json_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_use_json_Set() const{
    return m_use_json_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_use_json_Valid() const{
    return m_use_json_isValid;
}

QString OAIFindAllGlobalAuthModules_200_response_inner::getUserInfoUrl() const {
    return m_user_info_url;
}
void OAIFindAllGlobalAuthModules_200_response_inner::setUserInfoUrl(const QString &user_info_url) {
    m_user_info_url = user_info_url;
    m_user_info_url_isSet = true;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_user_info_url_Set() const{
    return m_user_info_url_isSet;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::is_user_info_url_Valid() const{
    return m_user_info_url_isValid;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_admin_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_admin_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_desc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_field_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_filter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_field_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_otoroshi_data_field_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_search_base_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_search_filter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_session_max_age_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_base_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_users.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_access_token_field_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_authorize_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_callback_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_claims_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_secret_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_jwt_verifier.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_login_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_logout_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oid_config_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_read_profile_from_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scope_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_cookies_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_json_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_info_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFindAllGlobalAuthModules_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_admin_password_isValid && m_admin_username_isValid && m_desc_isValid && m_email_field_isValid && m_group_filter_isValid && m_id_isValid && m_name_isValid && m_name_field_isValid && m_otoroshi_data_field_isValid && m_search_base_isValid && m_search_filter_isValid && m_server_url_isValid && m_session_max_age_isValid && m_type_isValid && m_user_base_isValid && m_users_isValid && m_access_token_field_isValid && m_authorize_url_isValid && m_callback_url_isValid && m_client_id_isValid && m_client_secret_isValid && m_login_url_isValid && m_logout_url_isValid && m_token_url_isValid && m_user_info_url_isValid && true;
}

} // namespace OpenAPI
