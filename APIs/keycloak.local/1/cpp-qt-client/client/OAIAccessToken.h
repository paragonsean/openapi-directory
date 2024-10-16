/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAccessToken.h
 *
 * 
 */

#ifndef OAIAccessToken_H
#define OAIAccessToken_H

#include <QJsonObject>

#include "OAIAccessToken_Access.h"
#include "OAIAccessToken_Authorization.h"
#include "OAIAccessToken_CertConf.h"
#include "OAIAddressClaimSet.h"
#include <QJsonValue>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddressClaimSet;
class OAIAccessToken_Authorization;
class OAIAccessToken_CertConf;
class OAIAccessToken_Access;

class OAIAccessToken : public OAIObject {
public:
    OAIAccessToken();
    OAIAccessToken(QString json);
    ~OAIAccessToken() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAcr() const;
    void setAcr(const QString &acr);
    bool is_acr_Set() const;
    bool is_acr_Valid() const;

    OAIAddressClaimSet getAddress() const;
    void setAddress(const OAIAddressClaimSet &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QList<QString> getAllowedOrigins() const;
    void setAllowedOrigins(const QList<QString> &allowed_origins);
    bool is_allowed_origins_Set() const;
    bool is_allowed_origins_Valid() const;

    QString getAtHash() const;
    void setAtHash(const QString &at_hash);
    bool is_at_hash_Set() const;
    bool is_at_hash_Valid() const;

    qint64 getAuthTime() const;
    void setAuthTime(const qint64 &auth_time);
    bool is_auth_time_Set() const;
    bool is_auth_time_Valid() const;

    OAIAccessToken_Authorization getAuthorization() const;
    void setAuthorization(const OAIAccessToken_Authorization &authorization);
    bool is_authorization_Set() const;
    bool is_authorization_Valid() const;

    QString getAzp() const;
    void setAzp(const QString &azp);
    bool is_azp_Set() const;
    bool is_azp_Valid() const;

    QString getBirthdate() const;
    void setBirthdate(const QString &birthdate);
    bool is_birthdate_Set() const;
    bool is_birthdate_Valid() const;

    QString getCHash() const;
    void setCHash(const QString &c_hash);
    bool is_c_hash_Set() const;
    bool is_c_hash_Valid() const;

    QString getCategory() const;
    void setCategory(const QString &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QString getClaimsLocales() const;
    void setClaimsLocales(const QString &claims_locales);
    bool is_claims_locales_Set() const;
    bool is_claims_locales_Valid() const;

    OAIAccessToken_CertConf getCnf() const;
    void setCnf(const OAIAccessToken_CertConf &cnf);
    bool is_cnf_Set() const;
    bool is_cnf_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    bool isEmailVerified() const;
    void setEmailVerified(const bool &email_verified);
    bool is_email_verified_Set() const;
    bool is_email_verified_Valid() const;

    qint64 getExp() const;
    void setExp(const qint64 &exp);
    bool is_exp_Set() const;
    bool is_exp_Valid() const;

    QString getFamilyName() const;
    void setFamilyName(const QString &family_name);
    bool is_family_name_Set() const;
    bool is_family_name_Valid() const;

    QString getGender() const;
    void setGender(const QString &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    QString getGivenName() const;
    void setGivenName(const QString &given_name);
    bool is_given_name_Set() const;
    bool is_given_name_Valid() const;

    qint64 getIat() const;
    void setIat(const qint64 &iat);
    bool is_iat_Set() const;
    bool is_iat_Valid() const;

    QString getIss() const;
    void setIss(const QString &iss);
    bool is_iss_Set() const;
    bool is_iss_Valid() const;

    QString getJti() const;
    void setJti(const QString &jti);
    bool is_jti_Set() const;
    bool is_jti_Valid() const;

    QString getLocale() const;
    void setLocale(const QString &locale);
    bool is_locale_Set() const;
    bool is_locale_Valid() const;

    QString getMiddleName() const;
    void setMiddleName(const QString &middle_name);
    bool is_middle_name_Set() const;
    bool is_middle_name_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint64 getNbf() const;
    void setNbf(const qint64 &nbf);
    bool is_nbf_Set() const;
    bool is_nbf_Valid() const;

    QString getNickname() const;
    void setNickname(const QString &nickname);
    bool is_nickname_Set() const;
    bool is_nickname_Valid() const;

    QString getNonce() const;
    void setNonce(const QString &nonce);
    bool is_nonce_Set() const;
    bool is_nonce_Valid() const;

    QMap<QString, QJsonValue> getOtherClaims() const;
    void setOtherClaims(const QMap<QString, QJsonValue> &other_claims);
    bool is_other_claims_Set() const;
    bool is_other_claims_Valid() const;

    QString getPhoneNumber() const;
    void setPhoneNumber(const QString &phone_number);
    bool is_phone_number_Set() const;
    bool is_phone_number_Valid() const;

    bool isPhoneNumberVerified() const;
    void setPhoneNumberVerified(const bool &phone_number_verified);
    bool is_phone_number_verified_Set() const;
    bool is_phone_number_verified_Valid() const;

    QString getPicture() const;
    void setPicture(const QString &picture);
    bool is_picture_Set() const;
    bool is_picture_Valid() const;

    QString getPreferredUsername() const;
    void setPreferredUsername(const QString &preferred_username);
    bool is_preferred_username_Set() const;
    bool is_preferred_username_Valid() const;

    QString getProfile() const;
    void setProfile(const QString &profile);
    bool is_profile_Set() const;
    bool is_profile_Valid() const;

    OAIAccessToken_Access getRealmAccess() const;
    void setRealmAccess(const OAIAccessToken_Access &realm_access);
    bool is_realm_access_Set() const;
    bool is_realm_access_Valid() const;

    QString getSHash() const;
    void setSHash(const QString &s_hash);
    bool is_s_hash_Set() const;
    bool is_s_hash_Valid() const;

    QString getScope() const;
    void setScope(const QString &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    QString getSessionState() const;
    void setSessionState(const QString &session_state);
    bool is_session_state_Set() const;
    bool is_session_state_Valid() const;

    QString getSub() const;
    void setSub(const QString &sub);
    bool is_sub_Set() const;
    bool is_sub_Valid() const;

    QList<QString> getTrustedCerts() const;
    void setTrustedCerts(const QList<QString> &trusted_certs);
    bool is_trusted_certs_Set() const;
    bool is_trusted_certs_Valid() const;

    QString getTyp() const;
    void setTyp(const QString &typ);
    bool is_typ_Set() const;
    bool is_typ_Valid() const;

    qint64 getUpdatedAt() const;
    void setUpdatedAt(const qint64 &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    QString getWebsite() const;
    void setWebsite(const QString &website);
    bool is_website_Set() const;
    bool is_website_Valid() const;

    QString getZoneinfo() const;
    void setZoneinfo(const QString &zoneinfo);
    bool is_zoneinfo_Set() const;
    bool is_zoneinfo_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_acr;
    bool m_acr_isSet;
    bool m_acr_isValid;

    OAIAddressClaimSet m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QList<QString> m_allowed_origins;
    bool m_allowed_origins_isSet;
    bool m_allowed_origins_isValid;

    QString m_at_hash;
    bool m_at_hash_isSet;
    bool m_at_hash_isValid;

    qint64 m_auth_time;
    bool m_auth_time_isSet;
    bool m_auth_time_isValid;

    OAIAccessToken_Authorization m_authorization;
    bool m_authorization_isSet;
    bool m_authorization_isValid;

    QString m_azp;
    bool m_azp_isSet;
    bool m_azp_isValid;

    QString m_birthdate;
    bool m_birthdate_isSet;
    bool m_birthdate_isValid;

    QString m_c_hash;
    bool m_c_hash_isSet;
    bool m_c_hash_isValid;

    QString m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QString m_claims_locales;
    bool m_claims_locales_isSet;
    bool m_claims_locales_isValid;

    OAIAccessToken_CertConf m_cnf;
    bool m_cnf_isSet;
    bool m_cnf_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    bool m_email_verified;
    bool m_email_verified_isSet;
    bool m_email_verified_isValid;

    qint64 m_exp;
    bool m_exp_isSet;
    bool m_exp_isValid;

    QString m_family_name;
    bool m_family_name_isSet;
    bool m_family_name_isValid;

    QString m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    QString m_given_name;
    bool m_given_name_isSet;
    bool m_given_name_isValid;

    qint64 m_iat;
    bool m_iat_isSet;
    bool m_iat_isValid;

    QString m_iss;
    bool m_iss_isSet;
    bool m_iss_isValid;

    QString m_jti;
    bool m_jti_isSet;
    bool m_jti_isValid;

    QString m_locale;
    bool m_locale_isSet;
    bool m_locale_isValid;

    QString m_middle_name;
    bool m_middle_name_isSet;
    bool m_middle_name_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint64 m_nbf;
    bool m_nbf_isSet;
    bool m_nbf_isValid;

    QString m_nickname;
    bool m_nickname_isSet;
    bool m_nickname_isValid;

    QString m_nonce;
    bool m_nonce_isSet;
    bool m_nonce_isValid;

    QMap<QString, QJsonValue> m_other_claims;
    bool m_other_claims_isSet;
    bool m_other_claims_isValid;

    QString m_phone_number;
    bool m_phone_number_isSet;
    bool m_phone_number_isValid;

    bool m_phone_number_verified;
    bool m_phone_number_verified_isSet;
    bool m_phone_number_verified_isValid;

    QString m_picture;
    bool m_picture_isSet;
    bool m_picture_isValid;

    QString m_preferred_username;
    bool m_preferred_username_isSet;
    bool m_preferred_username_isValid;

    QString m_profile;
    bool m_profile_isSet;
    bool m_profile_isValid;

    OAIAccessToken_Access m_realm_access;
    bool m_realm_access_isSet;
    bool m_realm_access_isValid;

    QString m_s_hash;
    bool m_s_hash_isSet;
    bool m_s_hash_isValid;

    QString m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;

    QString m_session_state;
    bool m_session_state_isSet;
    bool m_session_state_isValid;

    QString m_sub;
    bool m_sub_isSet;
    bool m_sub_isValid;

    QList<QString> m_trusted_certs;
    bool m_trusted_certs_isSet;
    bool m_trusted_certs_isValid;

    QString m_typ;
    bool m_typ_isSet;
    bool m_typ_isValid;

    qint64 m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    QString m_website;
    bool m_website_isSet;
    bool m_website_isValid;

    QString m_zoneinfo;
    bool m_zoneinfo_isSet;
    bool m_zoneinfo_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAccessToken)

#endif // OAIAccessToken_H
