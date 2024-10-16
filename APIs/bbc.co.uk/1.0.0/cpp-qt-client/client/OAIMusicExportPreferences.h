/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMusicExportPreferences.h
 *
 * 
 */

#ifndef OAIMusicExportPreferences_H
#define OAIMusicExportPreferences_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIMusicExportPreferences : public OAIObject {
public:
    OAIMusicExportPreferences();
    OAIMusicExportPreferences(QString json);
    ~OAIMusicExportPreferences() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccessExpiresAt() const;
    void setAccessExpiresAt(const QString &access_expires_at);
    bool is_access_expires_at_Set() const;
    bool is_access_expires_at_Valid() const;

    QString getAccessToken() const;
    void setAccessToken(const QString &access_token);
    bool is_access_token_Set() const;
    bool is_access_token_Valid() const;

    bool isAddPlusExport() const;
    void setAddPlusExport(const bool &add_plus_export);
    bool is_add_plus_export_Set() const;
    bool is_add_plus_export_Valid() const;

    QString getAuthorizationCode() const;
    void setAuthorizationCode(const QString &authorization_code);
    bool is_authorization_code_Set() const;
    bool is_authorization_code_Valid() const;

    QString getLastExport() const;
    void setLastExport(const QString &last_export);
    bool is_last_export_Set() const;
    bool is_last_export_Valid() const;

    QString getLegacyState() const;
    void setLegacyState(const QString &legacy_state);
    bool is_legacy_state_Set() const;
    bool is_legacy_state_Valid() const;

    QString getPartnerId() const;
    void setPartnerId(const QString &partner_id);
    bool is_partner_id_Set() const;
    bool is_partner_id_Valid() const;

    QString getRefreshToken() const;
    void setRefreshToken(const QString &refresh_token);
    bool is_refresh_token_Set() const;
    bool is_refresh_token_Valid() const;

    bool isTerms() const;
    void setTerms(const bool &terms);
    bool is_terms_Set() const;
    bool is_terms_Valid() const;

    QString getVendor() const;
    void setVendor(const QString &vendor);
    bool is_vendor_Set() const;
    bool is_vendor_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_access_expires_at;
    bool m_access_expires_at_isSet;
    bool m_access_expires_at_isValid;

    QString m_access_token;
    bool m_access_token_isSet;
    bool m_access_token_isValid;

    bool m_add_plus_export;
    bool m_add_plus_export_isSet;
    bool m_add_plus_export_isValid;

    QString m_authorization_code;
    bool m_authorization_code_isSet;
    bool m_authorization_code_isValid;

    QString m_last_export;
    bool m_last_export_isSet;
    bool m_last_export_isValid;

    QString m_legacy_state;
    bool m_legacy_state_isSet;
    bool m_legacy_state_isValid;

    QString m_partner_id;
    bool m_partner_id_isSet;
    bool m_partner_id_isValid;

    QString m_refresh_token;
    bool m_refresh_token_isSet;
    bool m_refresh_token_isValid;

    bool m_terms;
    bool m_terms_isSet;
    bool m_terms_isValid;

    QString m_vendor;
    bool m_vendor_isSet;
    bool m_vendor_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMusicExportPreferences)

#endif // OAIMusicExportPreferences_H
