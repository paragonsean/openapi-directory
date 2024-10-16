/**
 * Tradeworks
 * Authentication is required to access all methods of the API. Enter username and password.                 Credentials are automatically set as you type.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUserDTO.h
 *
 * 
 */

#ifndef OAIUserDTO_H
#define OAIUserDTO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUserDTO : public OAIObject {
public:
    OAIUserDTO();
    OAIUserDTO(QString json);
    ~OAIUserDTO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAffiliateId() const;
    void setAffiliateId(const QString &affiliate_id);
    bool is_affiliate_id_Set() const;
    bool is_affiliate_id_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getSubscriptionType() const;
    void setSubscriptionType(const QString &subscription_type);
    bool is_subscription_type_Set() const;
    bool is_subscription_type_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_affiliate_id;
    bool m_affiliate_id_isSet;
    bool m_affiliate_id_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_subscription_type;
    bool m_subscription_type_isSet;
    bool m_subscription_type_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUserDTO)

#endif // OAIUserDTO_H
