/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUser.h
 *
 * 
 */

#ifndef OAIUser_H
#define OAIUser_H

#include <QJsonObject>

#include "OAIMobileApplication.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMobileApplication;

class OAIUser : public OAIObject {
public:
    OAIUser();
    OAIUser(QString json);
    ~OAIUser() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEmailAddress() const;
    void setEmailAddress(const QString &email_address);
    bool is_email_address_Set() const;
    bool is_email_address_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QString getLastlogin() const;
    void setLastlogin(const QString &lastlogin);
    bool is_lastlogin_Set() const;
    bool is_lastlogin_Valid() const;

    OAIMobileApplication getMobileApplicationDetails() const;
    void setMobileApplicationDetails(const OAIMobileApplication &mobile_application_details);
    bool is_mobile_application_details_Set() const;
    bool is_mobile_application_details_Valid() const;

    QString getMobileNumber() const;
    void setMobileNumber(const QString &mobile_number);
    bool is_mobile_number_Set() const;
    bool is_mobile_number_Valid() const;

    QString getRole() const;
    void setRole(const QString &role);
    bool is_role_Set() const;
    bool is_role_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getUserCvl() const;
    void setUserCvl(const QString &user_cvl);
    bool is_user_cvl_Set() const;
    bool is_user_cvl_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_email_address;
    bool m_email_address_isSet;
    bool m_email_address_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QString m_lastlogin;
    bool m_lastlogin_isSet;
    bool m_lastlogin_isValid;

    OAIMobileApplication m_mobile_application_details;
    bool m_mobile_application_details_isSet;
    bool m_mobile_application_details_isValid;

    QString m_mobile_number;
    bool m_mobile_number_isSet;
    bool m_mobile_number_isValid;

    QString m_role;
    bool m_role_isSet;
    bool m_role_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_user_cvl;
    bool m_user_cvl_isSet;
    bool m_user_cvl_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUser)

#endif // OAIUser_H
