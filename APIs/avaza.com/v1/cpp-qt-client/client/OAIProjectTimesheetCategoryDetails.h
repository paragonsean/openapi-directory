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
 * OAIProjectTimesheetCategoryDetails.h
 *
 * 
 */

#ifndef OAIProjectTimesheetCategoryDetails_H
#define OAIProjectTimesheetCategoryDetails_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProjectTimesheetCategoryDetails : public OAIObject {
public:
    OAIProjectTimesheetCategoryDetails();
    OAIProjectTimesheetCategoryDetails(QString json);
    ~OAIProjectTimesheetCategoryDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAccountIdfk() const;
    void setAccountIdfk(const qint32 &account_idfk);
    bool is_account_idfk_Set() const;
    bool is_account_idfk_Valid() const;

    double getBudgetHours() const;
    void setBudgetHours(const double &budget_hours);
    bool is_budget_hours_Set() const;
    bool is_budget_hours_Valid() const;

    double getCostAmount() const;
    void setCostAmount(const double &cost_amount);
    bool is_cost_amount_Set() const;
    bool is_cost_amount_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getProjectIdfk() const;
    void setProjectIdfk(const qint32 &project_idfk);
    bool is_project_idfk_Set() const;
    bool is_project_idfk_Valid() const;

    double getRateAmount() const;
    void setRateAmount(const double &rate_amount);
    bool is_rate_amount_Set() const;
    bool is_rate_amount_Valid() const;

    qint32 getTimeSheetCategoryIdfk() const;
    void setTimeSheetCategoryIdfk(const qint32 &time_sheet_category_idfk);
    bool is_time_sheet_category_idfk_Set() const;
    bool is_time_sheet_category_idfk_Valid() const;

    bool isIsBillable() const;
    void setIsBillable(const bool &is_billable);
    bool is_is_billable_Set() const;
    bool is_is_billable_Valid() const;

    bool isIsDisabled() const;
    void setIsDisabled(const bool &is_disabled);
    bool is_is_disabled_Set() const;
    bool is_is_disabled_Valid() const;

    bool isIsPayable() const;
    void setIsPayable(const bool &is_payable);
    bool is_is_payable_Set() const;
    bool is_is_payable_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_account_idfk;
    bool m_account_idfk_isSet;
    bool m_account_idfk_isValid;

    double m_budget_hours;
    bool m_budget_hours_isSet;
    bool m_budget_hours_isValid;

    double m_cost_amount;
    bool m_cost_amount_isSet;
    bool m_cost_amount_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_project_idfk;
    bool m_project_idfk_isSet;
    bool m_project_idfk_isValid;

    double m_rate_amount;
    bool m_rate_amount_isSet;
    bool m_rate_amount_isValid;

    qint32 m_time_sheet_category_idfk;
    bool m_time_sheet_category_idfk_isSet;
    bool m_time_sheet_category_idfk_isValid;

    bool m_is_billable;
    bool m_is_billable_isSet;
    bool m_is_billable_isValid;

    bool m_is_disabled;
    bool m_is_disabled_isSet;
    bool m_is_disabled_isValid;

    bool m_is_payable;
    bool m_is_payable_isSet;
    bool m_is_payable_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjectTimesheetCategoryDetails)

#endif // OAIProjectTimesheetCategoryDetails_H
