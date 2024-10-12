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

#include "OAIProductItemApiModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductItemApiModel::OAIProductItemApiModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductItemApiModel::OAIProductItemApiModel() {
    this->initializeModel();
}

OAIProductItemApiModel::~OAIProductItemApiModel() {}

void OAIProductItemApiModel::initializeModel() {

    m_cost_isSet = false;
    m_cost_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_minimum_quantity_isSet = false;
    m_minimum_quantity_isValid = false;

    m_reference_id_isSet = false;
    m_reference_id_isValid = false;

    m_sub_total_amount_isSet = false;
    m_sub_total_amount_isValid = false;

    m_tax_amount_isSet = false;
    m_tax_amount_isValid = false;

    m_tax_id_isSet = false;
    m_tax_id_isValid = false;

    m_tax_percentage_isSet = false;
    m_tax_percentage_isValid = false;

    m_total_amount_isSet = false;
    m_total_amount_isValid = false;

    m_work_type_id_isSet = false;
    m_work_type_id_isValid = false;
}

void OAIProductItemApiModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductItemApiModel::fromJsonObject(QJsonObject json) {

    m_cost_isValid = ::OpenAPI::fromJsonValue(m_cost, json[QString("Cost")]);
    m_cost_isSet = !json[QString("Cost")].isNull() && m_cost_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_minimum_quantity_isValid = ::OpenAPI::fromJsonValue(m_minimum_quantity, json[QString("MinimumQuantity")]);
    m_minimum_quantity_isSet = !json[QString("MinimumQuantity")].isNull() && m_minimum_quantity_isValid;

    m_reference_id_isValid = ::OpenAPI::fromJsonValue(m_reference_id, json[QString("ReferenceId")]);
    m_reference_id_isSet = !json[QString("ReferenceId")].isNull() && m_reference_id_isValid;

    m_sub_total_amount_isValid = ::OpenAPI::fromJsonValue(m_sub_total_amount, json[QString("SubTotalAmount")]);
    m_sub_total_amount_isSet = !json[QString("SubTotalAmount")].isNull() && m_sub_total_amount_isValid;

    m_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_tax_amount, json[QString("TaxAmount")]);
    m_tax_amount_isSet = !json[QString("TaxAmount")].isNull() && m_tax_amount_isValid;

    m_tax_id_isValid = ::OpenAPI::fromJsonValue(m_tax_id, json[QString("TaxId")]);
    m_tax_id_isSet = !json[QString("TaxId")].isNull() && m_tax_id_isValid;

    m_tax_percentage_isValid = ::OpenAPI::fromJsonValue(m_tax_percentage, json[QString("TaxPercentage")]);
    m_tax_percentage_isSet = !json[QString("TaxPercentage")].isNull() && m_tax_percentage_isValid;

    m_total_amount_isValid = ::OpenAPI::fromJsonValue(m_total_amount, json[QString("TotalAmount")]);
    m_total_amount_isSet = !json[QString("TotalAmount")].isNull() && m_total_amount_isValid;

    m_work_type_id_isValid = ::OpenAPI::fromJsonValue(m_work_type_id, json[QString("WorkTypeId")]);
    m_work_type_id_isSet = !json[QString("WorkTypeId")].isNull() && m_work_type_id_isValid;
}

QString OAIProductItemApiModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductItemApiModel::asJsonObject() const {
    QJsonObject obj;
    if (m_cost_isSet) {
        obj.insert(QString("Cost"), ::OpenAPI::toJsonValue(m_cost));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_minimum_quantity_isSet) {
        obj.insert(QString("MinimumQuantity"), ::OpenAPI::toJsonValue(m_minimum_quantity));
    }
    if (m_reference_id_isSet) {
        obj.insert(QString("ReferenceId"), ::OpenAPI::toJsonValue(m_reference_id));
    }
    if (m_sub_total_amount_isSet) {
        obj.insert(QString("SubTotalAmount"), ::OpenAPI::toJsonValue(m_sub_total_amount));
    }
    if (m_tax_amount_isSet) {
        obj.insert(QString("TaxAmount"), ::OpenAPI::toJsonValue(m_tax_amount));
    }
    if (m_tax_id_isSet) {
        obj.insert(QString("TaxId"), ::OpenAPI::toJsonValue(m_tax_id));
    }
    if (m_tax_percentage_isSet) {
        obj.insert(QString("TaxPercentage"), ::OpenAPI::toJsonValue(m_tax_percentage));
    }
    if (m_total_amount_isSet) {
        obj.insert(QString("TotalAmount"), ::OpenAPI::toJsonValue(m_total_amount));
    }
    if (m_work_type_id_isSet) {
        obj.insert(QString("WorkTypeId"), ::OpenAPI::toJsonValue(m_work_type_id));
    }
    return obj;
}

double OAIProductItemApiModel::getCost() const {
    return m_cost;
}
void OAIProductItemApiModel::setCost(const double &cost) {
    m_cost = cost;
    m_cost_isSet = true;
}

bool OAIProductItemApiModel::is_cost_Set() const{
    return m_cost_isSet;
}

bool OAIProductItemApiModel::is_cost_Valid() const{
    return m_cost_isValid;
}

QString OAIProductItemApiModel::getDescription() const {
    return m_description;
}
void OAIProductItemApiModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIProductItemApiModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAIProductItemApiModel::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIProductItemApiModel::getId() const {
    return m_id;
}
void OAIProductItemApiModel::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProductItemApiModel::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProductItemApiModel::is_id_Valid() const{
    return m_id_isValid;
}

double OAIProductItemApiModel::getMinimumQuantity() const {
    return m_minimum_quantity;
}
void OAIProductItemApiModel::setMinimumQuantity(const double &minimum_quantity) {
    m_minimum_quantity = minimum_quantity;
    m_minimum_quantity_isSet = true;
}

bool OAIProductItemApiModel::is_minimum_quantity_Set() const{
    return m_minimum_quantity_isSet;
}

bool OAIProductItemApiModel::is_minimum_quantity_Valid() const{
    return m_minimum_quantity_isValid;
}

QString OAIProductItemApiModel::getReferenceId() const {
    return m_reference_id;
}
void OAIProductItemApiModel::setReferenceId(const QString &reference_id) {
    m_reference_id = reference_id;
    m_reference_id_isSet = true;
}

bool OAIProductItemApiModel::is_reference_id_Set() const{
    return m_reference_id_isSet;
}

bool OAIProductItemApiModel::is_reference_id_Valid() const{
    return m_reference_id_isValid;
}

double OAIProductItemApiModel::getSubTotalAmount() const {
    return m_sub_total_amount;
}
void OAIProductItemApiModel::setSubTotalAmount(const double &sub_total_amount) {
    m_sub_total_amount = sub_total_amount;
    m_sub_total_amount_isSet = true;
}

bool OAIProductItemApiModel::is_sub_total_amount_Set() const{
    return m_sub_total_amount_isSet;
}

bool OAIProductItemApiModel::is_sub_total_amount_Valid() const{
    return m_sub_total_amount_isValid;
}

double OAIProductItemApiModel::getTaxAmount() const {
    return m_tax_amount;
}
void OAIProductItemApiModel::setTaxAmount(const double &tax_amount) {
    m_tax_amount = tax_amount;
    m_tax_amount_isSet = true;
}

bool OAIProductItemApiModel::is_tax_amount_Set() const{
    return m_tax_amount_isSet;
}

bool OAIProductItemApiModel::is_tax_amount_Valid() const{
    return m_tax_amount_isValid;
}

qint32 OAIProductItemApiModel::getTaxId() const {
    return m_tax_id;
}
void OAIProductItemApiModel::setTaxId(const qint32 &tax_id) {
    m_tax_id = tax_id;
    m_tax_id_isSet = true;
}

bool OAIProductItemApiModel::is_tax_id_Set() const{
    return m_tax_id_isSet;
}

bool OAIProductItemApiModel::is_tax_id_Valid() const{
    return m_tax_id_isValid;
}

double OAIProductItemApiModel::getTaxPercentage() const {
    return m_tax_percentage;
}
void OAIProductItemApiModel::setTaxPercentage(const double &tax_percentage) {
    m_tax_percentage = tax_percentage;
    m_tax_percentage_isSet = true;
}

bool OAIProductItemApiModel::is_tax_percentage_Set() const{
    return m_tax_percentage_isSet;
}

bool OAIProductItemApiModel::is_tax_percentage_Valid() const{
    return m_tax_percentage_isValid;
}

double OAIProductItemApiModel::getTotalAmount() const {
    return m_total_amount;
}
void OAIProductItemApiModel::setTotalAmount(const double &total_amount) {
    m_total_amount = total_amount;
    m_total_amount_isSet = true;
}

bool OAIProductItemApiModel::is_total_amount_Set() const{
    return m_total_amount_isSet;
}

bool OAIProductItemApiModel::is_total_amount_Valid() const{
    return m_total_amount_isValid;
}

qint32 OAIProductItemApiModel::getWorkTypeId() const {
    return m_work_type_id;
}
void OAIProductItemApiModel::setWorkTypeId(const qint32 &work_type_id) {
    m_work_type_id = work_type_id;
    m_work_type_id_isSet = true;
}

bool OAIProductItemApiModel::is_work_type_id_Set() const{
    return m_work_type_id_isSet;
}

bool OAIProductItemApiModel::is_work_type_id_Valid() const{
    return m_work_type_id_isValid;
}

bool OAIProductItemApiModel::isSet() const {
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

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minimum_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_total_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_amount_isSet) {
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

        if (m_total_amount_isSet) {
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

bool OAIProductItemApiModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
