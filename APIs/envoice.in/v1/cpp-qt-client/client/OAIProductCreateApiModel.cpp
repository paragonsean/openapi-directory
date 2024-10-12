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

#include "OAIProductCreateApiModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductCreateApiModel::OAIProductCreateApiModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductCreateApiModel::OAIProductCreateApiModel() {
    this->initializeModel();
}

OAIProductCreateApiModel::~OAIProductCreateApiModel() {}

void OAIProductCreateApiModel::initializeModel() {

    m_after_payment_description_isSet = false;
    m_after_payment_description_isValid = false;

    m_attachments_isSet = false;
    m_attachments_isValid = false;

    m_button_call_to_action_isSet = false;
    m_button_call_to_action_isValid = false;

    m_coupons_isSet = false;
    m_coupons_isValid = false;

    m_currency_id_isSet = false;
    m_currency_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_discounts_isSet = false;
    m_discounts_isValid = false;

    m_is_featured_isSet = false;
    m_is_featured_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_payment_gateways_isSet = false;
    m_payment_gateways_isValid = false;

    m_shipping_amount_isSet = false;
    m_shipping_amount_isValid = false;

    m_shipping_description_isSet = false;
    m_shipping_description_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_what_happens_next_description_isSet = false;
    m_what_happens_next_description_isValid = false;
}

void OAIProductCreateApiModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductCreateApiModel::fromJsonObject(QJsonObject json) {

    m_after_payment_description_isValid = ::OpenAPI::fromJsonValue(m_after_payment_description, json[QString("AfterPaymentDescription")]);
    m_after_payment_description_isSet = !json[QString("AfterPaymentDescription")].isNull() && m_after_payment_description_isValid;

    m_attachments_isValid = ::OpenAPI::fromJsonValue(m_attachments, json[QString("Attachments")]);
    m_attachments_isSet = !json[QString("Attachments")].isNull() && m_attachments_isValid;

    m_button_call_to_action_isValid = ::OpenAPI::fromJsonValue(m_button_call_to_action, json[QString("ButtonCallToAction")]);
    m_button_call_to_action_isSet = !json[QString("ButtonCallToAction")].isNull() && m_button_call_to_action_isValid;

    m_coupons_isValid = ::OpenAPI::fromJsonValue(m_coupons, json[QString("Coupons")]);
    m_coupons_isSet = !json[QString("Coupons")].isNull() && m_coupons_isValid;

    m_currency_id_isValid = ::OpenAPI::fromJsonValue(m_currency_id, json[QString("CurrencyId")]);
    m_currency_id_isSet = !json[QString("CurrencyId")].isNull() && m_currency_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_discounts_isValid = ::OpenAPI::fromJsonValue(m_discounts, json[QString("Discounts")]);
    m_discounts_isSet = !json[QString("Discounts")].isNull() && m_discounts_isValid;

    m_is_featured_isValid = ::OpenAPI::fromJsonValue(m_is_featured, json[QString("IsFeatured")]);
    m_is_featured_isSet = !json[QString("IsFeatured")].isNull() && m_is_featured_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("Items")]);
    m_items_isSet = !json[QString("Items")].isNull() && m_items_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_payment_gateways_isValid = ::OpenAPI::fromJsonValue(m_payment_gateways, json[QString("PaymentGateways")]);
    m_payment_gateways_isSet = !json[QString("PaymentGateways")].isNull() && m_payment_gateways_isValid;

    m_shipping_amount_isValid = ::OpenAPI::fromJsonValue(m_shipping_amount, json[QString("ShippingAmount")]);
    m_shipping_amount_isSet = !json[QString("ShippingAmount")].isNull() && m_shipping_amount_isValid;

    m_shipping_description_isValid = ::OpenAPI::fromJsonValue(m_shipping_description, json[QString("ShippingDescription")]);
    m_shipping_description_isSet = !json[QString("ShippingDescription")].isNull() && m_shipping_description_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;

    m_what_happens_next_description_isValid = ::OpenAPI::fromJsonValue(m_what_happens_next_description, json[QString("WhatHappensNextDescription")]);
    m_what_happens_next_description_isSet = !json[QString("WhatHappensNextDescription")].isNull() && m_what_happens_next_description_isValid;
}

QString OAIProductCreateApiModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductCreateApiModel::asJsonObject() const {
    QJsonObject obj;
    if (m_after_payment_description_isSet) {
        obj.insert(QString("AfterPaymentDescription"), ::OpenAPI::toJsonValue(m_after_payment_description));
    }
    if (m_attachments.size() > 0) {
        obj.insert(QString("Attachments"), ::OpenAPI::toJsonValue(m_attachments));
    }
    if (m_button_call_to_action_isSet) {
        obj.insert(QString("ButtonCallToAction"), ::OpenAPI::toJsonValue(m_button_call_to_action));
    }
    if (m_coupons.size() > 0) {
        obj.insert(QString("Coupons"), ::OpenAPI::toJsonValue(m_coupons));
    }
    if (m_currency_id_isSet) {
        obj.insert(QString("CurrencyId"), ::OpenAPI::toJsonValue(m_currency_id));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_discounts.size() > 0) {
        obj.insert(QString("Discounts"), ::OpenAPI::toJsonValue(m_discounts));
    }
    if (m_is_featured_isSet) {
        obj.insert(QString("IsFeatured"), ::OpenAPI::toJsonValue(m_is_featured));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("Items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_payment_gateways.size() > 0) {
        obj.insert(QString("PaymentGateways"), ::OpenAPI::toJsonValue(m_payment_gateways));
    }
    if (m_shipping_amount_isSet) {
        obj.insert(QString("ShippingAmount"), ::OpenAPI::toJsonValue(m_shipping_amount));
    }
    if (m_shipping_description_isSet) {
        obj.insert(QString("ShippingDescription"), ::OpenAPI::toJsonValue(m_shipping_description));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_what_happens_next_description_isSet) {
        obj.insert(QString("WhatHappensNextDescription"), ::OpenAPI::toJsonValue(m_what_happens_next_description));
    }
    return obj;
}

QString OAIProductCreateApiModel::getAfterPaymentDescription() const {
    return m_after_payment_description;
}
void OAIProductCreateApiModel::setAfterPaymentDescription(const QString &after_payment_description) {
    m_after_payment_description = after_payment_description;
    m_after_payment_description_isSet = true;
}

bool OAIProductCreateApiModel::is_after_payment_description_Set() const{
    return m_after_payment_description_isSet;
}

bool OAIProductCreateApiModel::is_after_payment_description_Valid() const{
    return m_after_payment_description_isValid;
}

QList<OAIProductAttachmentApiModel> OAIProductCreateApiModel::getAttachments() const {
    return m_attachments;
}
void OAIProductCreateApiModel::setAttachments(const QList<OAIProductAttachmentApiModel> &attachments) {
    m_attachments = attachments;
    m_attachments_isSet = true;
}

bool OAIProductCreateApiModel::is_attachments_Set() const{
    return m_attachments_isSet;
}

bool OAIProductCreateApiModel::is_attachments_Valid() const{
    return m_attachments_isValid;
}

QString OAIProductCreateApiModel::getButtonCallToAction() const {
    return m_button_call_to_action;
}
void OAIProductCreateApiModel::setButtonCallToAction(const QString &button_call_to_action) {
    m_button_call_to_action = button_call_to_action;
    m_button_call_to_action_isSet = true;
}

bool OAIProductCreateApiModel::is_button_call_to_action_Set() const{
    return m_button_call_to_action_isSet;
}

bool OAIProductCreateApiModel::is_button_call_to_action_Valid() const{
    return m_button_call_to_action_isValid;
}

QList<OAIProductCouponApiModel> OAIProductCreateApiModel::getCoupons() const {
    return m_coupons;
}
void OAIProductCreateApiModel::setCoupons(const QList<OAIProductCouponApiModel> &coupons) {
    m_coupons = coupons;
    m_coupons_isSet = true;
}

bool OAIProductCreateApiModel::is_coupons_Set() const{
    return m_coupons_isSet;
}

bool OAIProductCreateApiModel::is_coupons_Valid() const{
    return m_coupons_isValid;
}

qint32 OAIProductCreateApiModel::getCurrencyId() const {
    return m_currency_id;
}
void OAIProductCreateApiModel::setCurrencyId(const qint32 &currency_id) {
    m_currency_id = currency_id;
    m_currency_id_isSet = true;
}

bool OAIProductCreateApiModel::is_currency_id_Set() const{
    return m_currency_id_isSet;
}

bool OAIProductCreateApiModel::is_currency_id_Valid() const{
    return m_currency_id_isValid;
}

QString OAIProductCreateApiModel::getDescription() const {
    return m_description;
}
void OAIProductCreateApiModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIProductCreateApiModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAIProductCreateApiModel::is_description_Valid() const{
    return m_description_isValid;
}

QList<OAIProductDiscountApiModel> OAIProductCreateApiModel::getDiscounts() const {
    return m_discounts;
}
void OAIProductCreateApiModel::setDiscounts(const QList<OAIProductDiscountApiModel> &discounts) {
    m_discounts = discounts;
    m_discounts_isSet = true;
}

bool OAIProductCreateApiModel::is_discounts_Set() const{
    return m_discounts_isSet;
}

bool OAIProductCreateApiModel::is_discounts_Valid() const{
    return m_discounts_isValid;
}

bool OAIProductCreateApiModel::isIsFeatured() const {
    return m_is_featured;
}
void OAIProductCreateApiModel::setIsFeatured(const bool &is_featured) {
    m_is_featured = is_featured;
    m_is_featured_isSet = true;
}

bool OAIProductCreateApiModel::is_is_featured_Set() const{
    return m_is_featured_isSet;
}

bool OAIProductCreateApiModel::is_is_featured_Valid() const{
    return m_is_featured_isValid;
}

QList<OAIProductItemApiModel> OAIProductCreateApiModel::getItems() const {
    return m_items;
}
void OAIProductCreateApiModel::setItems(const QList<OAIProductItemApiModel> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIProductCreateApiModel::is_items_Set() const{
    return m_items_isSet;
}

bool OAIProductCreateApiModel::is_items_Valid() const{
    return m_items_isValid;
}

QString OAIProductCreateApiModel::getName() const {
    return m_name;
}
void OAIProductCreateApiModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProductCreateApiModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProductCreateApiModel::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIProductGatewayApiModel> OAIProductCreateApiModel::getPaymentGateways() const {
    return m_payment_gateways;
}
void OAIProductCreateApiModel::setPaymentGateways(const QList<OAIProductGatewayApiModel> &payment_gateways) {
    m_payment_gateways = payment_gateways;
    m_payment_gateways_isSet = true;
}

bool OAIProductCreateApiModel::is_payment_gateways_Set() const{
    return m_payment_gateways_isSet;
}

bool OAIProductCreateApiModel::is_payment_gateways_Valid() const{
    return m_payment_gateways_isValid;
}

double OAIProductCreateApiModel::getShippingAmount() const {
    return m_shipping_amount;
}
void OAIProductCreateApiModel::setShippingAmount(const double &shipping_amount) {
    m_shipping_amount = shipping_amount;
    m_shipping_amount_isSet = true;
}

bool OAIProductCreateApiModel::is_shipping_amount_Set() const{
    return m_shipping_amount_isSet;
}

bool OAIProductCreateApiModel::is_shipping_amount_Valid() const{
    return m_shipping_amount_isValid;
}

QString OAIProductCreateApiModel::getShippingDescription() const {
    return m_shipping_description;
}
void OAIProductCreateApiModel::setShippingDescription(const QString &shipping_description) {
    m_shipping_description = shipping_description;
    m_shipping_description_isSet = true;
}

bool OAIProductCreateApiModel::is_shipping_description_Set() const{
    return m_shipping_description_isSet;
}

bool OAIProductCreateApiModel::is_shipping_description_Valid() const{
    return m_shipping_description_isValid;
}

QString OAIProductCreateApiModel::getStatus() const {
    return m_status;
}
void OAIProductCreateApiModel::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIProductCreateApiModel::is_status_Set() const{
    return m_status_isSet;
}

bool OAIProductCreateApiModel::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIProductCreateApiModel::getWhatHappensNextDescription() const {
    return m_what_happens_next_description;
}
void OAIProductCreateApiModel::setWhatHappensNextDescription(const QString &what_happens_next_description) {
    m_what_happens_next_description = what_happens_next_description;
    m_what_happens_next_description_isSet = true;
}

bool OAIProductCreateApiModel::is_what_happens_next_description_Set() const{
    return m_what_happens_next_description_isSet;
}

bool OAIProductCreateApiModel::is_what_happens_next_description_Valid() const{
    return m_what_happens_next_description_isValid;
}

bool OAIProductCreateApiModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_after_payment_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_attachments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_button_call_to_action_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coupons.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_featured_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_gateways.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_what_happens_next_description_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductCreateApiModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
