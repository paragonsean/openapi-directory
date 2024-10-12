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
 * OAIInvoiceUpdateItemApiModel.h
 *
 * 
 */

#ifndef OAIInvoiceUpdateItemApiModel_H
#define OAIInvoiceUpdateItemApiModel_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInvoiceUpdateItemApiModel : public OAIObject {
public:
    OAIInvoiceUpdateItemApiModel();
    OAIInvoiceUpdateItemApiModel(QString json);
    ~OAIInvoiceUpdateItemApiModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getCost() const;
    void setCost(const double &cost);
    bool is_cost_Set() const;
    bool is_cost_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    double getDiscountPercentage() const;
    void setDiscountPercentage(const double &discount_percentage);
    bool is_discount_percentage_Set() const;
    bool is_discount_percentage_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    double getQuantity() const;
    void setQuantity(const double &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    qint32 getTaxId() const;
    void setTaxId(const qint32 &tax_id);
    bool is_tax_id_Set() const;
    bool is_tax_id_Valid() const;

    double getTaxPercentage() const;
    void setTaxPercentage(const double &tax_percentage);
    bool is_tax_percentage_Set() const;
    bool is_tax_percentage_Valid() const;

    qint32 getWorkTypeId() const;
    void setWorkTypeId(const qint32 &work_type_id);
    bool is_work_type_id_Set() const;
    bool is_work_type_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_cost;
    bool m_cost_isSet;
    bool m_cost_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    double m_discount_percentage;
    bool m_discount_percentage_isSet;
    bool m_discount_percentage_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    double m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    qint32 m_tax_id;
    bool m_tax_id_isSet;
    bool m_tax_id_isValid;

    double m_tax_percentage;
    bool m_tax_percentage_isSet;
    bool m_tax_percentage_isValid;

    qint32 m_work_type_id;
    bool m_work_type_id_isSet;
    bool m_work_type_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInvoiceUpdateItemApiModel)

#endif // OAIInvoiceUpdateItemApiModel_H
