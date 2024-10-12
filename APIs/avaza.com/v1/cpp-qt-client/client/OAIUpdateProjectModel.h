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
 * OAIUpdateProjectModel.h
 *
 * 
 */

#ifndef OAIUpdateProjectModel_H
#define OAIUpdateProjectModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateProjectModel : public OAIObject {
public:
    OAIUpdateProjectModel();
    OAIUpdateProjectModel(QString json);
    ~OAIUpdateProjectModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getBudgetAmount() const;
    void setBudgetAmount(const double &budget_amount);
    bool is_budget_amount_Set() const;
    bool is_budget_amount_Valid() const;

    double getBudgetHours() const;
    void setBudgetHours(const double &budget_hours);
    bool is_budget_hours_Set() const;
    bool is_budget_hours_Valid() const;

    QDateTime getEndDate() const;
    void setEndDate(const QDateTime &end_date);
    bool is_end_date_Set() const;
    bool is_end_date_Valid() const;

    QList<QString> getFieldsToUpdate() const;
    void setFieldsToUpdate(const QList<QString> &fields_to_update);
    bool is_fields_to_update_Set() const;
    bool is_fields_to_update_Valid() const;

    QString getProjectBillableTypeCode() const;
    void setProjectBillableTypeCode(const QString &project_billable_type_code);
    bool is_project_billable_type_code_Set() const;
    bool is_project_billable_type_code_Valid() const;

    QString getProjectBudgetTypeCode() const;
    void setProjectBudgetTypeCode(const QString &project_budget_type_code);
    bool is_project_budget_type_code_Set() const;
    bool is_project_budget_type_code_Valid() const;

    qint32 getProjectCategoryIdfk() const;
    void setProjectCategoryIdfk(const qint32 &project_category_idfk);
    bool is_project_category_idfk_Set() const;
    bool is_project_category_idfk_Valid() const;

    qint32 getProjectId() const;
    void setProjectId(const qint32 &project_id);
    bool is_project_id_Set() const;
    bool is_project_id_Valid() const;

    QString getProjectNotes() const;
    void setProjectNotes(const QString &project_notes);
    bool is_project_notes_Set() const;
    bool is_project_notes_Valid() const;

    QString getProjectStatusCode() const;
    void setProjectStatusCode(const QString &project_status_code);
    bool is_project_status_code_Set() const;
    bool is_project_status_code_Valid() const;

    QString getProjectTitle() const;
    void setProjectTitle(const QString &project_title);
    bool is_project_title_Set() const;
    bool is_project_title_Valid() const;

    QDateTime getStartDate() const;
    void setStartDate(const QDateTime &start_date);
    bool is_start_date_Set() const;
    bool is_start_date_Valid() const;

    bool isTimesheetApprovalRequiredbyDefault() const;
    void setTimesheetApprovalRequiredbyDefault(const bool &timesheet_approval_requiredby_default);
    bool is_timesheet_approval_requiredby_default_Set() const;
    bool is_timesheet_approval_requiredby_default_Valid() const;

    bool isIsTaskRequiredOnTimesheet() const;
    void setIsTaskRequiredOnTimesheet(const bool &is_task_required_on_timesheet);
    bool is_is_task_required_on_timesheet_Set() const;
    bool is_is_task_required_on_timesheet_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_budget_amount;
    bool m_budget_amount_isSet;
    bool m_budget_amount_isValid;

    double m_budget_hours;
    bool m_budget_hours_isSet;
    bool m_budget_hours_isValid;

    QDateTime m_end_date;
    bool m_end_date_isSet;
    bool m_end_date_isValid;

    QList<QString> m_fields_to_update;
    bool m_fields_to_update_isSet;
    bool m_fields_to_update_isValid;

    QString m_project_billable_type_code;
    bool m_project_billable_type_code_isSet;
    bool m_project_billable_type_code_isValid;

    QString m_project_budget_type_code;
    bool m_project_budget_type_code_isSet;
    bool m_project_budget_type_code_isValid;

    qint32 m_project_category_idfk;
    bool m_project_category_idfk_isSet;
    bool m_project_category_idfk_isValid;

    qint32 m_project_id;
    bool m_project_id_isSet;
    bool m_project_id_isValid;

    QString m_project_notes;
    bool m_project_notes_isSet;
    bool m_project_notes_isValid;

    QString m_project_status_code;
    bool m_project_status_code_isSet;
    bool m_project_status_code_isValid;

    QString m_project_title;
    bool m_project_title_isSet;
    bool m_project_title_isValid;

    QDateTime m_start_date;
    bool m_start_date_isSet;
    bool m_start_date_isValid;

    bool m_timesheet_approval_requiredby_default;
    bool m_timesheet_approval_requiredby_default_isSet;
    bool m_timesheet_approval_requiredby_default_isValid;

    bool m_is_task_required_on_timesheet;
    bool m_is_task_required_on_timesheet_isSet;
    bool m_is_task_required_on_timesheet_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateProjectModel)

#endif // OAIUpdateProjectModel_H
