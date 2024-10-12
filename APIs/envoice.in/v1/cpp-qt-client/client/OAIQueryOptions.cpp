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

#include "OAIQueryOptions.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQueryOptions::OAIQueryOptions(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQueryOptions::OAIQueryOptions() {
    this->initializeModel();
}

OAIQueryOptions::~OAIQueryOptions() {}

void OAIQueryOptions::initializeModel() {

    m_page_isSet = false;
    m_page_isValid = false;

    m_page_size_isSet = false;
    m_page_size_isValid = false;
}

void OAIQueryOptions::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQueryOptions::fromJsonObject(QJsonObject json) {

    m_page_isValid = ::OpenAPI::fromJsonValue(m_page, json[QString("Page")]);
    m_page_isSet = !json[QString("Page")].isNull() && m_page_isValid;

    m_page_size_isValid = ::OpenAPI::fromJsonValue(m_page_size, json[QString("PageSize")]);
    m_page_size_isSet = !json[QString("PageSize")].isNull() && m_page_size_isValid;
}

QString OAIQueryOptions::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQueryOptions::asJsonObject() const {
    QJsonObject obj;
    if (m_page_isSet) {
        obj.insert(QString("Page"), ::OpenAPI::toJsonValue(m_page));
    }
    if (m_page_size_isSet) {
        obj.insert(QString("PageSize"), ::OpenAPI::toJsonValue(m_page_size));
    }
    return obj;
}

qint32 OAIQueryOptions::getPage() const {
    return m_page;
}
void OAIQueryOptions::setPage(const qint32 &page) {
    m_page = page;
    m_page_isSet = true;
}

bool OAIQueryOptions::is_page_Set() const{
    return m_page_isSet;
}

bool OAIQueryOptions::is_page_Valid() const{
    return m_page_isValid;
}

qint32 OAIQueryOptions::getPageSize() const {
    return m_page_size;
}
void OAIQueryOptions::setPageSize(const qint32 &page_size) {
    m_page_size = page_size;
    m_page_size_isSet = true;
}

bool OAIQueryOptions::is_page_size_Set() const{
    return m_page_size_isSet;
}

bool OAIQueryOptions::is_page_size_Valid() const{
    return m_page_size_isValid;
}

bool OAIQueryOptions::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_size_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQueryOptions::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
