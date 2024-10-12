/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIExpenseCategoryDetails.h
 *
 * 
 */

#ifndef OAIExpenseCategoryDetails_H
#define OAIExpenseCategoryDetails_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIExpenseCategoryDetails : public OAIObject {
public:
    OAIExpenseCategoryDetails();
    OAIExpenseCategoryDetails(QString json);
    ~OAIExpenseCategoryDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    qint32 getExpenseCategoryId() const;
    void setExpenseCategoryId(const qint32 &expense_category_id);
    bool is_expense_category_id_Set() const;
    bool is_expense_category_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getUnitName() const;
    void setUnitName(const QString &unit_name);
    bool is_unit_name_Set() const;
    bool is_unit_name_Valid() const;

    double getUnitPrice() const;
    void setUnitPrice(const double &unit_price);
    bool is_unit_price_Set() const;
    bool is_unit_price_Valid() const;

    bool isHasUnitPrice() const;
    void setHasUnitPrice(const bool &has_unit_price);
    bool is_has_unit_price_Set() const;
    bool is_has_unit_price_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    qint32 m_expense_category_id;
    bool m_expense_category_id_isSet;
    bool m_expense_category_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_unit_name;
    bool m_unit_name_isSet;
    bool m_unit_name_isValid;

    double m_unit_price;
    bool m_unit_price_isSet;
    bool m_unit_price_isValid;

    bool m_has_unit_price;
    bool m_has_unit_price_isSet;
    bool m_has_unit_price_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExpenseCategoryDetails)

#endif // OAIExpenseCategoryDetails_H
