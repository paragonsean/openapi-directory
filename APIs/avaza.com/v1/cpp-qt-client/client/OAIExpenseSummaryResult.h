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
 * OAIExpenseSummaryResult.h
 *
 * 
 */

#ifndef OAIExpenseSummaryResult_H
#define OAIExpenseSummaryResult_H

#include <QJsonObject>

#include "OAIExpenseSummaryGroup.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIExpenseSummaryGroup;

class OAIExpenseSummaryResult : public OAIObject {
public:
    OAIExpenseSummaryResult();
    OAIExpenseSummaryResult(QString json);
    ~OAIExpenseSummaryResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getExpenseDateFrom() const;
    void setExpenseDateFrom(const QDateTime &expense_date_from);
    bool is_expense_date_from_Set() const;
    bool is_expense_date_from_Valid() const;

    QDateTime getExpenseDateTo() const;
    void setExpenseDateTo(const QDateTime &expense_date_to);
    bool is_expense_date_to_Set() const;
    bool is_expense_date_to_Valid() const;

    QList<OAIExpenseSummaryGroup> getGroupData() const;
    void setGroupData(const QList<OAIExpenseSummaryGroup> &group_data);
    bool is_group_data_Set() const;
    bool is_group_data_Valid() const;

    QList<QString> getGroupingLevels() const;
    void setGroupingLevels(const QList<QString> &grouping_levels);
    bool is_grouping_levels_Set() const;
    bool is_grouping_levels_Valid() const;

    double getTotalAmount() const;
    void setTotalAmount(const double &total_amount);
    bool is_total_amount_Set() const;
    bool is_total_amount_Valid() const;

    QList<qint32> getUserId() const;
    void setUserId(const QList<qint32> &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_expense_date_from;
    bool m_expense_date_from_isSet;
    bool m_expense_date_from_isValid;

    QDateTime m_expense_date_to;
    bool m_expense_date_to_isSet;
    bool m_expense_date_to_isValid;

    QList<OAIExpenseSummaryGroup> m_group_data;
    bool m_group_data_isSet;
    bool m_group_data_isValid;

    QList<QString> m_grouping_levels;
    bool m_grouping_levels_isSet;
    bool m_grouping_levels_isValid;

    double m_total_amount;
    bool m_total_amount_isSet;
    bool m_total_amount_isValid;

    QList<qint32> m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExpenseSummaryResult)

#endif // OAIExpenseSummaryResult_H
