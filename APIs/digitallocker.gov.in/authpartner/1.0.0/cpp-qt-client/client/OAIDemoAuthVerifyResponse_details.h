/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDemoAuthVerifyResponse_details.h
 *
 * 
 */

#ifndef OAIDemoAuthVerifyResponse_details_H
#define OAIDemoAuthVerifyResponse_details_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDemoAuthVerifyResponse_details : public OAIObject {
public:
    OAIDemoAuthVerifyResponse_details();
    OAIDemoAuthVerifyResponse_details(QString json);
    ~OAIDemoAuthVerifyResponse_details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccessToken() const;
    void setAccessToken(const QString &access_token);
    bool is_access_token_Set() const;
    bool is_access_token_Valid() const;

    QString getExpiresIn() const;
    void setExpiresIn(const QString &expires_in);
    bool is_expires_in_Set() const;
    bool is_expires_in_Valid() const;

    QString getRefreshToken() const;
    void setRefreshToken(const QString &refresh_token);
    bool is_refresh_token_Set() const;
    bool is_refresh_token_Valid() const;

    QString getScope() const;
    void setScope(const QString &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    QString getTokenType() const;
    void setTokenType(const QString &token_type);
    bool is_token_type_Set() const;
    bool is_token_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_access_token;
    bool m_access_token_isSet;
    bool m_access_token_isValid;

    QString m_expires_in;
    bool m_expires_in_isSet;
    bool m_expires_in_isValid;

    QString m_refresh_token;
    bool m_refresh_token_isSet;
    bool m_refresh_token_isValid;

    QString m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;

    QString m_token_type;
    bool m_token_type_isSet;
    bool m_token_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDemoAuthVerifyResponse_details)

#endif // OAIDemoAuthVerifyResponse_details_H
