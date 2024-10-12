/**
 * API v1.0.0
 * [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  <span style='margin-left: 0.5em;'>or</span>  <a href='https://documenter.getpostman.com/view/3559821/TVeqcn2L' class='openapi-button' _ngcontent-c6>View Postman docs</a>    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    <div class='postman-tutorial'>    # Tutorial for running the API in postman    Click on \"\"Run in Postman\"\" button  <br /><br />  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \"\"Postman for windows\"\" to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  <br /><br />  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \"\"Open Postman\"\".  <br /><br />  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \"\"Envoice api\"\"  <br /><br />  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice's endpoint so you don't really need to change that.    <sub>\\*Eye button in top right corner </sub>  <br /><br />   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  <br /><br />   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don't need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  <br /><br />  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  <br /><br />  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  </div>    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status `200` in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  ```  {      Signature: \"\"sha256 string\"\",      Timestamp: \"\"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"\",      Activity: {          Message: \"string\",          Link: \"share url\",          Type: int,                  InvoiceNumber: \"string\",          InvoiceId: int,                  OrderNumber: \"string\",          OrderId: int,          Id: int,          CreatedOn: \"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"      }  }  ```            
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIInvoiceRecurringApiModel.h
 *
 * Definition of invoice recurring profile
 */

#ifndef OAIInvoiceRecurringApiModel_H
#define OAIInvoiceRecurringApiModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInvoiceRecurringApiModel : public OAIObject {
public:
    OAIInvoiceRecurringApiModel();
    OAIInvoiceRecurringApiModel(QString json);
    ~OAIInvoiceRecurringApiModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getDayOfMonth() const;
    void setDayOfMonth(const qint32 &day_of_month);
    bool is_day_of_month_Set() const;
    bool is_day_of_month_Valid() const;

    QString getDayOfWeek() const;
    void setDayOfWeek(const QString &day_of_week);
    bool is_day_of_week_Set() const;
    bool is_day_of_week_Valid() const;

    qint32 getDueDateInDays() const;
    void setDueDateInDays(const qint32 &due_date_in_days);
    bool is_due_date_in_days_Set() const;
    bool is_due_date_in_days_Valid() const;

    QDateTime getEndOfRecurrance() const;
    void setEndOfRecurrance(const QDateTime &end_of_recurrance);
    bool is_end_of_recurrance_Set() const;
    bool is_end_of_recurrance_Valid() const;

    qint32 getMonth() const;
    void setMonth(const qint32 &month);
    bool is_month_Set() const;
    bool is_month_Valid() const;

    QString getRecurrancePattern() const;
    void setRecurrancePattern(const QString &recurrance_pattern);
    bool is_recurrance_pattern_Set() const;
    bool is_recurrance_pattern_Valid() const;

    qint32 getRecurranceValue() const;
    void setRecurranceValue(const qint32 &recurrance_value);
    bool is_recurrance_value_Set() const;
    bool is_recurrance_value_Valid() const;

    QDateTime getStartOfRecurrance() const;
    void setStartOfRecurrance(const QDateTime &start_of_recurrance);
    bool is_start_of_recurrance_Set() const;
    bool is_start_of_recurrance_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_day_of_month;
    bool m_day_of_month_isSet;
    bool m_day_of_month_isValid;

    QString m_day_of_week;
    bool m_day_of_week_isSet;
    bool m_day_of_week_isValid;

    qint32 m_due_date_in_days;
    bool m_due_date_in_days_isSet;
    bool m_due_date_in_days_isValid;

    QDateTime m_end_of_recurrance;
    bool m_end_of_recurrance_isSet;
    bool m_end_of_recurrance_isValid;

    qint32 m_month;
    bool m_month_isSet;
    bool m_month_isValid;

    QString m_recurrance_pattern;
    bool m_recurrance_pattern_isSet;
    bool m_recurrance_pattern_isValid;

    qint32 m_recurrance_value;
    bool m_recurrance_value_isSet;
    bool m_recurrance_value_isValid;

    QDateTime m_start_of_recurrance;
    bool m_start_of_recurrance_isSet;
    bool m_start_of_recurrance_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInvoiceRecurringApiModel)

#endif // OAIInvoiceRecurringApiModel_H
