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

#include "OAIProductDiscountApiModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductDiscountApiModel::OAIProductDiscountApiModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductDiscountApiModel::OAIProductDiscountApiModel() {
    this->initializeModel();
}

OAIProductDiscountApiModel::~OAIProductDiscountApiModel() {}

void OAIProductDiscountApiModel::initializeModel() {

    m_discount_amount_isSet = false;
    m_discount_amount_isValid = false;

    m_discount_percentage_isSet = false;
    m_discount_percentage_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_valid_from_isSet = false;
    m_valid_from_isValid = false;

    m_valid_to_isSet = false;
    m_valid_to_isValid = false;
}

void OAIProductDiscountApiModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductDiscountApiModel::fromJsonObject(QJsonObject json) {

    m_discount_amount_isValid = ::OpenAPI::fromJsonValue(m_discount_amount, json[QString("DiscountAmount")]);
    m_discount_amount_isSet = !json[QString("DiscountAmount")].isNull() && m_discount_amount_isValid;

    m_discount_percentage_isValid = ::OpenAPI::fromJsonValue(m_discount_percentage, json[QString("DiscountPercentage")]);
    m_discount_percentage_isSet = !json[QString("DiscountPercentage")].isNull() && m_discount_percentage_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_valid_from_isValid = ::OpenAPI::fromJsonValue(m_valid_from, json[QString("ValidFrom")]);
    m_valid_from_isSet = !json[QString("ValidFrom")].isNull() && m_valid_from_isValid;

    m_valid_to_isValid = ::OpenAPI::fromJsonValue(m_valid_to, json[QString("ValidTo")]);
    m_valid_to_isSet = !json[QString("ValidTo")].isNull() && m_valid_to_isValid;
}

QString OAIProductDiscountApiModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductDiscountApiModel::asJsonObject() const {
    QJsonObject obj;
    if (m_discount_amount_isSet) {
        obj.insert(QString("DiscountAmount"), ::OpenAPI::toJsonValue(m_discount_amount));
    }
    if (m_discount_percentage_isSet) {
        obj.insert(QString("DiscountPercentage"), ::OpenAPI::toJsonValue(m_discount_percentage));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_valid_from_isSet) {
        obj.insert(QString("ValidFrom"), ::OpenAPI::toJsonValue(m_valid_from));
    }
    if (m_valid_to_isSet) {
        obj.insert(QString("ValidTo"), ::OpenAPI::toJsonValue(m_valid_to));
    }
    return obj;
}

double OAIProductDiscountApiModel::getDiscountAmount() const {
    return m_discount_amount;
}
void OAIProductDiscountApiModel::setDiscountAmount(const double &discount_amount) {
    m_discount_amount = discount_amount;
    m_discount_amount_isSet = true;
}

bool OAIProductDiscountApiModel::is_discount_amount_Set() const{
    return m_discount_amount_isSet;
}

bool OAIProductDiscountApiModel::is_discount_amount_Valid() const{
    return m_discount_amount_isValid;
}

double OAIProductDiscountApiModel::getDiscountPercentage() const {
    return m_discount_percentage;
}
void OAIProductDiscountApiModel::setDiscountPercentage(const double &discount_percentage) {
    m_discount_percentage = discount_percentage;
    m_discount_percentage_isSet = true;
}

bool OAIProductDiscountApiModel::is_discount_percentage_Set() const{
    return m_discount_percentage_isSet;
}

bool OAIProductDiscountApiModel::is_discount_percentage_Valid() const{
    return m_discount_percentage_isValid;
}

qint32 OAIProductDiscountApiModel::getId() const {
    return m_id;
}
void OAIProductDiscountApiModel::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProductDiscountApiModel::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProductDiscountApiModel::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIProductDiscountApiModel::getName() const {
    return m_name;
}
void OAIProductDiscountApiModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProductDiscountApiModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProductDiscountApiModel::is_name_Valid() const{
    return m_name_isValid;
}

QDateTime OAIProductDiscountApiModel::getValidFrom() const {
    return m_valid_from;
}
void OAIProductDiscountApiModel::setValidFrom(const QDateTime &valid_from) {
    m_valid_from = valid_from;
    m_valid_from_isSet = true;
}

bool OAIProductDiscountApiModel::is_valid_from_Set() const{
    return m_valid_from_isSet;
}

bool OAIProductDiscountApiModel::is_valid_from_Valid() const{
    return m_valid_from_isValid;
}

QDateTime OAIProductDiscountApiModel::getValidTo() const {
    return m_valid_to;
}
void OAIProductDiscountApiModel::setValidTo(const QDateTime &valid_to) {
    m_valid_to = valid_to;
    m_valid_to_isSet = true;
}

bool OAIProductDiscountApiModel::is_valid_to_Set() const{
    return m_valid_to_isSet;
}

bool OAIProductDiscountApiModel::is_valid_to_Valid() const{
    return m_valid_to_isValid;
}

bool OAIProductDiscountApiModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_discount_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_valid_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_valid_to_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductDiscountApiModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
