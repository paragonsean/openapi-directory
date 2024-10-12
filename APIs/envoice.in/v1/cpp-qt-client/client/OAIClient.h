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
 * OAIClient.h
 *
 * 
 */

#ifndef OAIClient_H
#define OAIClient_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIClient : public OAIObject {
public:
    OAIClient();
    OAIClient(QString json);
    ~OAIClient() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddress() const;
    void setAddress(const QString &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    qint32 getClientCountryId() const;
    void setClientCountryId(const qint32 &client_country_id);
    bool is_client_country_id_Set() const;
    bool is_client_country_id_Valid() const;

    qint32 getClientCurrencyId() const;
    void setClientCurrencyId(const qint32 &client_currency_id);
    bool is_client_currency_id_Set() const;
    bool is_client_currency_id_Valid() const;

    QString getCompanyRegistrationNumber() const;
    void setCompanyRegistrationNumber(const QString &company_registration_number);
    bool is_company_registration_number_Set() const;
    bool is_company_registration_number_Valid() const;

    qint32 getDefaultDueDateInDays() const;
    void setDefaultDueDateInDays(const qint32 &default_due_date_in_days);
    bool is_default_due_date_in_days_Set() const;
    bool is_default_due_date_in_days_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPhoneNumber() const;
    void setPhoneNumber(const QString &phone_number);
    bool is_phone_number_Set() const;
    bool is_phone_number_Valid() const;

    qint32 getUiLanguageId() const;
    void setUiLanguageId(const qint32 &ui_language_id);
    bool is_ui_language_id_Set() const;
    bool is_ui_language_id_Valid() const;

    qint32 getUserId() const;
    void setUserId(const qint32 &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    QString getVat() const;
    void setVat(const QString &vat);
    bool is_vat_Set() const;
    bool is_vat_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    qint32 m_client_country_id;
    bool m_client_country_id_isSet;
    bool m_client_country_id_isValid;

    qint32 m_client_currency_id;
    bool m_client_currency_id_isSet;
    bool m_client_currency_id_isValid;

    QString m_company_registration_number;
    bool m_company_registration_number_isSet;
    bool m_company_registration_number_isValid;

    qint32 m_default_due_date_in_days;
    bool m_default_due_date_in_days_isSet;
    bool m_default_due_date_in_days_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_phone_number;
    bool m_phone_number_isSet;
    bool m_phone_number_isValid;

    qint32 m_ui_language_id;
    bool m_ui_language_id_isSet;
    bool m_ui_language_id_isValid;

    qint32 m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;

    QString m_vat;
    bool m_vat_isSet;
    bool m_vat_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIClient)

#endif // OAIClient_H
