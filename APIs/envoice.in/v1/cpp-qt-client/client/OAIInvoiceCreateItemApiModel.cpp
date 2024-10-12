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

#include "OAIInvoiceCreateItemApiModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInvoiceCreateItemApiModel::OAIInvoiceCreateItemApiModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInvoiceCreateItemApiModel::OAIInvoiceCreateItemApiModel() {
    this->initializeModel();
}

OAIInvoiceCreateItemApiModel::~OAIInvoiceCreateItemApiModel() {}

void OAIInvoiceCreateItemApiModel::initializeModel() {

    m_cost_isSet = false;
    m_cost_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_discount_percentage_isSet = false;
    m_discount_percentage_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_tax_id_isSet = false;
    m_tax_id_isValid = false;

    m_tax_percentage_isSet = false;
    m_tax_percentage_isValid = false;

    m_work_type_id_isSet = false;
    m_work_type_id_isValid = false;
}

void OAIInvoiceCreateItemApiModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInvoiceCreateItemApiModel::fromJsonObject(QJsonObject json) {

    m_cost_isValid = ::OpenAPI::fromJsonValue(m_cost, json[QString("Cost")]);
    m_cost_isSet = !json[QString("Cost")].isNull() && m_cost_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_discount_percentage_isValid = ::OpenAPI::fromJsonValue(m_discount_percentage, json[QString("DiscountPercentage")]);
    m_discount_percentage_isSet = !json[QString("DiscountPercentage")].isNull() && m_discount_percentage_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("Quantity")]);
    m_quantity_isSet = !json[QString("Quantity")].isNull() && m_quantity_isValid;

    m_tax_id_isValid = ::OpenAPI::fromJsonValue(m_tax_id, json[QString("TaxId")]);
    m_tax_id_isSet = !json[QString("TaxId")].isNull() && m_tax_id_isValid;

    m_tax_percentage_isValid = ::OpenAPI::fromJsonValue(m_tax_percentage, json[QString("TaxPercentage")]);
    m_tax_percentage_isSet = !json[QString("TaxPercentage")].isNull() && m_tax_percentage_isValid;

    m_work_type_id_isValid = ::OpenAPI::fromJsonValue(m_work_type_id, json[QString("WorkTypeId")]);
    m_work_type_id_isSet = !json[QString("WorkTypeId")].isNull() && m_work_type_id_isValid;
}

QString OAIInvoiceCreateItemApiModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInvoiceCreateItemApiModel::asJsonObject() const {
    QJsonObject obj;
    if (m_cost_isSet) {
        obj.insert(QString("Cost"), ::OpenAPI::toJsonValue(m_cost));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_discount_percentage_isSet) {
        obj.insert(QString("DiscountPercentage"), ::OpenAPI::toJsonValue(m_discount_percentage));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("Quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_tax_id_isSet) {
        obj.insert(QString("TaxId"), ::OpenAPI::toJsonValue(m_tax_id));
    }
    if (m_tax_percentage_isSet) {
        obj.insert(QString("TaxPercentage"), ::OpenAPI::toJsonValue(m_tax_percentage));
    }
    if (m_work_type_id_isSet) {
        obj.insert(QString("WorkTypeId"), ::OpenAPI::toJsonValue(m_work_type_id));
    }
    return obj;
}

double OAIInvoiceCreateItemApiModel::getCost() const {
    return m_cost;
}
void OAIInvoiceCreateItemApiModel::setCost(const double &cost) {
    m_cost = cost;
    m_cost_isSet = true;
}

bool OAIInvoiceCreateItemApiModel::is_cost_Set() const{
    return m_cost_isSet;
}

bool OAIInvoiceCreateItemApiModel::is_cost_Valid() const{
    return m_cost_isValid;
}

QString OAIInvoiceCreateItemApiModel::getDescription() const {
    return m_description;
}
void OAIInvoiceCreateItemApiModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIInvoiceCreateItemApiModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAIInvoiceCreateItemApiModel::is_description_Valid() const{
    return m_description_isValid;
}

double OAIInvoiceCreateItemApiModel::getDiscountPercentage() const {
    return m_discount_percentage;
}
void OAIInvoiceCreateItemApiModel::setDiscountPercentage(const double &discount_percentage) {
    m_discount_percentage = discount_percentage;
    m_discount_percentage_isSet = true;
}

bool OAIInvoiceCreateItemApiModel::is_discount_percentage_Set() const{
    return m_discount_percentage_isSet;
}

bool OAIInvoiceCreateItemApiModel::is_discount_percentage_Valid() const{
    return m_discount_percentage_isValid;
}

double OAIInvoiceCreateItemApiModel::getQuantity() const {
    return m_quantity;
}
void OAIInvoiceCreateItemApiModel::setQuantity(const double &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIInvoiceCreateItemApiModel::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIInvoiceCreateItemApiModel::is_quantity_Valid() const{
    return m_quantity_isValid;
}

qint32 OAIInvoiceCreateItemApiModel::getTaxId() const {
    return m_tax_id;
}
void OAIInvoiceCreateItemApiModel::setTaxId(const qint32 &tax_id) {
    m_tax_id = tax_id;
    m_tax_id_isSet = true;
}

bool OAIInvoiceCreateItemApiModel::is_tax_id_Set() const{
    return m_tax_id_isSet;
}

bool OAIInvoiceCreateItemApiModel::is_tax_id_Valid() const{
    return m_tax_id_isValid;
}

double OAIInvoiceCreateItemApiModel::getTaxPercentage() const {
    return m_tax_percentage;
}
void OAIInvoiceCreateItemApiModel::setTaxPercentage(const double &tax_percentage) {
    m_tax_percentage = tax_percentage;
    m_tax_percentage_isSet = true;
}

bool OAIInvoiceCreateItemApiModel::is_tax_percentage_Set() const{
    return m_tax_percentage_isSet;
}

bool OAIInvoiceCreateItemApiModel::is_tax_percentage_Valid() const{
    return m_tax_percentage_isValid;
}

qint32 OAIInvoiceCreateItemApiModel::getWorkTypeId() const {
    return m_work_type_id;
}
void OAIInvoiceCreateItemApiModel::setWorkTypeId(const qint32 &work_type_id) {
    m_work_type_id = work_type_id;
    m_work_type_id_isSet = true;
}

bool OAIInvoiceCreateItemApiModel::is_work_type_id_Set() const{
    return m_work_type_id_isSet;
}

bool OAIInvoiceCreateItemApiModel::is_work_type_id_Valid() const{
    return m_work_type_id_isValid;
}

bool OAIInvoiceCreateItemApiModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cost_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInvoiceCreateItemApiModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
