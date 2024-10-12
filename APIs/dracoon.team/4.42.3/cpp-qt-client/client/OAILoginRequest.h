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
 * OAILoginRequest.h
 *
 * User credentials
 */

#ifndef OAILoginRequest_H
#define OAILoginRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAILoginRequest : public OAIObject {
public:
    OAILoginRequest();
    OAILoginRequest(QString json);
    ~OAILoginRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAuthType() const;
    void setAuthType(const QString &auth_type);
    bool is_auth_type_Set() const;
    bool is_auth_type_Valid() const;

    Q_DECL_DEPRECATED QString getLanguage() const;
    Q_DECL_DEPRECATED void setLanguage(const QString &language);
    Q_DECL_DEPRECATED bool is_language_Set() const;
    Q_DECL_DEPRECATED bool is_language_Valid() const;

    Q_DECL_DEPRECATED QString getLogin() const;
    Q_DECL_DEPRECATED void setLogin(const QString &login);
    Q_DECL_DEPRECATED bool is_login_Set() const;
    Q_DECL_DEPRECATED bool is_login_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getToken() const;
    void setToken(const QString &token);
    bool is_token_Set() const;
    bool is_token_Valid() const;

    QString getUserName() const;
    void setUserName(const QString &user_name);
    bool is_user_name_Set() const;
    bool is_user_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_auth_type;
    bool m_auth_type_isSet;
    bool m_auth_type_isValid;

    QString m_language;
    bool m_language_isSet;
    bool m_language_isValid;

    QString m_login;
    bool m_login_isSet;
    bool m_login_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_token;
    bool m_token_isSet;
    bool m_token_isValid;

    QString m_user_name;
    bool m_user_name_isSet;
    bool m_user_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILoginRequest)

#endif // OAILoginRequest_H
