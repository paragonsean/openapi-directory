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

#include "OAISubscriptionPlan.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscriptionPlan::OAISubscriptionPlan(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscriptionPlan::OAISubscriptionPlan() {
    this->initializeModel();
}

OAISubscriptionPlan::~OAISubscriptionPlan() {}

void OAISubscriptionPlan::initializeModel() {

    m_cancellated_on_isSet = false;
    m_cancellated_on_isValid = false;

    m_coupon_code_isSet = false;
    m_coupon_code_isValid = false;

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_external_identifier_isSet = false;
    m_external_identifier_isValid = false;

    m_features_isSet = false;
    m_features_isValid = false;

    m_has_due_payment_isSet = false;
    m_has_due_payment_isValid = false;

    m_has_due_payment_since_isSet = false;
    m_has_due_payment_since_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_identifier_isSet = false;
    m_identifier_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_lifetime_isSet = false;
    m_is_lifetime_isValid = false;

    m_last_payment_on_isSet = false;
    m_last_payment_on_isValid = false;

    m_max_clients_isSet = false;
    m_max_clients_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_on_hold_isSet = false;
    m_on_hold_isValid = false;

    m_order_identifier_isSet = false;
    m_order_identifier_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_recurrence_isSet = false;
    m_recurrence_isValid = false;

    m_sale_id_isSet = false;
    m_sale_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_system_cancelation_reason_isSet = false;
    m_system_cancelation_reason_isValid = false;

    m_trial_ends_on_isSet = false;
    m_trial_ends_on_isValid = false;

    m_trial_number_of_days_isSet = false;
    m_trial_number_of_days_isValid = false;

    m_trial_starts_on_isSet = false;
    m_trial_starts_on_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAISubscriptionPlan::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubscriptionPlan::fromJsonObject(QJsonObject json) {

    m_cancellated_on_isValid = ::OpenAPI::fromJsonValue(m_cancellated_on, json[QString("CancellatedOn")]);
    m_cancellated_on_isSet = !json[QString("CancellatedOn")].isNull() && m_cancellated_on_isValid;

    m_coupon_code_isValid = ::OpenAPI::fromJsonValue(m_coupon_code, json[QString("CouponCode")]);
    m_coupon_code_isSet = !json[QString("CouponCode")].isNull() && m_coupon_code_isValid;

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("CurrencyCode")]);
    m_currency_code_isSet = !json[QString("CurrencyCode")].isNull() && m_currency_code_isValid;

    m_external_identifier_isValid = ::OpenAPI::fromJsonValue(m_external_identifier, json[QString("ExternalIdentifier")]);
    m_external_identifier_isSet = !json[QString("ExternalIdentifier")].isNull() && m_external_identifier_isValid;

    m_features_isValid = ::OpenAPI::fromJsonValue(m_features, json[QString("Features")]);
    m_features_isSet = !json[QString("Features")].isNull() && m_features_isValid;

    m_has_due_payment_isValid = ::OpenAPI::fromJsonValue(m_has_due_payment, json[QString("HasDuePayment")]);
    m_has_due_payment_isSet = !json[QString("HasDuePayment")].isNull() && m_has_due_payment_isValid;

    m_has_due_payment_since_isValid = ::OpenAPI::fromJsonValue(m_has_due_payment_since, json[QString("HasDuePaymentSince")]);
    m_has_due_payment_since_isSet = !json[QString("HasDuePaymentSince")].isNull() && m_has_due_payment_since_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_identifier_isValid = ::OpenAPI::fromJsonValue(m_identifier, json[QString("Identifier")]);
    m_identifier_isSet = !json[QString("Identifier")].isNull() && m_identifier_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_is_lifetime_isValid = ::OpenAPI::fromJsonValue(m_is_lifetime, json[QString("IsLifetime")]);
    m_is_lifetime_isSet = !json[QString("IsLifetime")].isNull() && m_is_lifetime_isValid;

    m_last_payment_on_isValid = ::OpenAPI::fromJsonValue(m_last_payment_on, json[QString("LastPaymentOn")]);
    m_last_payment_on_isSet = !json[QString("LastPaymentOn")].isNull() && m_last_payment_on_isValid;

    m_max_clients_isValid = ::OpenAPI::fromJsonValue(m_max_clients, json[QString("MaxClients")]);
    m_max_clients_isSet = !json[QString("MaxClients")].isNull() && m_max_clients_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_on_hold_isValid = ::OpenAPI::fromJsonValue(m_on_hold, json[QString("OnHold")]);
    m_on_hold_isSet = !json[QString("OnHold")].isNull() && m_on_hold_isValid;

    m_order_identifier_isValid = ::OpenAPI::fromJsonValue(m_order_identifier, json[QString("OrderIdentifier")]);
    m_order_identifier_isSet = !json[QString("OrderIdentifier")].isNull() && m_order_identifier_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("Price")]);
    m_price_isSet = !json[QString("Price")].isNull() && m_price_isValid;

    m_recurrence_isValid = ::OpenAPI::fromJsonValue(m_recurrence, json[QString("Recurrence")]);
    m_recurrence_isSet = !json[QString("Recurrence")].isNull() && m_recurrence_isValid;

    m_sale_id_isValid = ::OpenAPI::fromJsonValue(m_sale_id, json[QString("SaleId")]);
    m_sale_id_isSet = !json[QString("SaleId")].isNull() && m_sale_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;

    m_system_cancelation_reason_isValid = ::OpenAPI::fromJsonValue(m_system_cancelation_reason, json[QString("SystemCancelationReason")]);
    m_system_cancelation_reason_isSet = !json[QString("SystemCancelationReason")].isNull() && m_system_cancelation_reason_isValid;

    m_trial_ends_on_isValid = ::OpenAPI::fromJsonValue(m_trial_ends_on, json[QString("TrialEndsOn")]);
    m_trial_ends_on_isSet = !json[QString("TrialEndsOn")].isNull() && m_trial_ends_on_isValid;

    m_trial_number_of_days_isValid = ::OpenAPI::fromJsonValue(m_trial_number_of_days, json[QString("TrialNumberOfDays")]);
    m_trial_number_of_days_isSet = !json[QString("TrialNumberOfDays")].isNull() && m_trial_number_of_days_isValid;

    m_trial_starts_on_isValid = ::OpenAPI::fromJsonValue(m_trial_starts_on, json[QString("TrialStartsOn")]);
    m_trial_starts_on_isSet = !json[QString("TrialStartsOn")].isNull() && m_trial_starts_on_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("UserId")]);
    m_user_id_isSet = !json[QString("UserId")].isNull() && m_user_id_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("Version")]);
    m_version_isSet = !json[QString("Version")].isNull() && m_version_isValid;
}

QString OAISubscriptionPlan::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubscriptionPlan::asJsonObject() const {
    QJsonObject obj;
    if (m_cancellated_on_isSet) {
        obj.insert(QString("CancellatedOn"), ::OpenAPI::toJsonValue(m_cancellated_on));
    }
    if (m_coupon_code_isSet) {
        obj.insert(QString("CouponCode"), ::OpenAPI::toJsonValue(m_coupon_code));
    }
    if (m_currency_code_isSet) {
        obj.insert(QString("CurrencyCode"), ::OpenAPI::toJsonValue(m_currency_code));
    }
    if (m_external_identifier_isSet) {
        obj.insert(QString("ExternalIdentifier"), ::OpenAPI::toJsonValue(m_external_identifier));
    }
    if (m_features.size() > 0) {
        obj.insert(QString("Features"), ::OpenAPI::toJsonValue(m_features));
    }
    if (m_has_due_payment_isSet) {
        obj.insert(QString("HasDuePayment"), ::OpenAPI::toJsonValue(m_has_due_payment));
    }
    if (m_has_due_payment_since_isSet) {
        obj.insert(QString("HasDuePaymentSince"), ::OpenAPI::toJsonValue(m_has_due_payment_since));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_identifier_isSet) {
        obj.insert(QString("Identifier"), ::OpenAPI::toJsonValue(m_identifier));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_lifetime_isSet) {
        obj.insert(QString("IsLifetime"), ::OpenAPI::toJsonValue(m_is_lifetime));
    }
    if (m_last_payment_on_isSet) {
        obj.insert(QString("LastPaymentOn"), ::OpenAPI::toJsonValue(m_last_payment_on));
    }
    if (m_max_clients_isSet) {
        obj.insert(QString("MaxClients"), ::OpenAPI::toJsonValue(m_max_clients));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_on_hold_isSet) {
        obj.insert(QString("OnHold"), ::OpenAPI::toJsonValue(m_on_hold));
    }
    if (m_order_identifier_isSet) {
        obj.insert(QString("OrderIdentifier"), ::OpenAPI::toJsonValue(m_order_identifier));
    }
    if (m_price_isSet) {
        obj.insert(QString("Price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_recurrence_isSet) {
        obj.insert(QString("Recurrence"), ::OpenAPI::toJsonValue(m_recurrence));
    }
    if (m_sale_id_isSet) {
        obj.insert(QString("SaleId"), ::OpenAPI::toJsonValue(m_sale_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_system_cancelation_reason_isSet) {
        obj.insert(QString("SystemCancelationReason"), ::OpenAPI::toJsonValue(m_system_cancelation_reason));
    }
    if (m_trial_ends_on_isSet) {
        obj.insert(QString("TrialEndsOn"), ::OpenAPI::toJsonValue(m_trial_ends_on));
    }
    if (m_trial_number_of_days_isSet) {
        obj.insert(QString("TrialNumberOfDays"), ::OpenAPI::toJsonValue(m_trial_number_of_days));
    }
    if (m_trial_starts_on_isSet) {
        obj.insert(QString("TrialStartsOn"), ::OpenAPI::toJsonValue(m_trial_starts_on));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("UserId"), ::OpenAPI::toJsonValue(m_user_id));
    }
    if (m_version_isSet) {
        obj.insert(QString("Version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QDateTime OAISubscriptionPlan::getCancellatedOn() const {
    return m_cancellated_on;
}
void OAISubscriptionPlan::setCancellatedOn(const QDateTime &cancellated_on) {
    m_cancellated_on = cancellated_on;
    m_cancellated_on_isSet = true;
}

bool OAISubscriptionPlan::is_cancellated_on_Set() const{
    return m_cancellated_on_isSet;
}

bool OAISubscriptionPlan::is_cancellated_on_Valid() const{
    return m_cancellated_on_isValid;
}

QString OAISubscriptionPlan::getCouponCode() const {
    return m_coupon_code;
}
void OAISubscriptionPlan::setCouponCode(const QString &coupon_code) {
    m_coupon_code = coupon_code;
    m_coupon_code_isSet = true;
}

bool OAISubscriptionPlan::is_coupon_code_Set() const{
    return m_coupon_code_isSet;
}

bool OAISubscriptionPlan::is_coupon_code_Valid() const{
    return m_coupon_code_isValid;
}

QString OAISubscriptionPlan::getCurrencyCode() const {
    return m_currency_code;
}
void OAISubscriptionPlan::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAISubscriptionPlan::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAISubscriptionPlan::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

QString OAISubscriptionPlan::getExternalIdentifier() const {
    return m_external_identifier;
}
void OAISubscriptionPlan::setExternalIdentifier(const QString &external_identifier) {
    m_external_identifier = external_identifier;
    m_external_identifier_isSet = true;
}

bool OAISubscriptionPlan::is_external_identifier_Set() const{
    return m_external_identifier_isSet;
}

bool OAISubscriptionPlan::is_external_identifier_Valid() const{
    return m_external_identifier_isValid;
}

QList<QString> OAISubscriptionPlan::getFeatures() const {
    return m_features;
}
void OAISubscriptionPlan::setFeatures(const QList<QString> &features) {
    m_features = features;
    m_features_isSet = true;
}

bool OAISubscriptionPlan::is_features_Set() const{
    return m_features_isSet;
}

bool OAISubscriptionPlan::is_features_Valid() const{
    return m_features_isValid;
}

bool OAISubscriptionPlan::isHasDuePayment() const {
    return m_has_due_payment;
}
void OAISubscriptionPlan::setHasDuePayment(const bool &has_due_payment) {
    m_has_due_payment = has_due_payment;
    m_has_due_payment_isSet = true;
}

bool OAISubscriptionPlan::is_has_due_payment_Set() const{
    return m_has_due_payment_isSet;
}

bool OAISubscriptionPlan::is_has_due_payment_Valid() const{
    return m_has_due_payment_isValid;
}

QDateTime OAISubscriptionPlan::getHasDuePaymentSince() const {
    return m_has_due_payment_since;
}
void OAISubscriptionPlan::setHasDuePaymentSince(const QDateTime &has_due_payment_since) {
    m_has_due_payment_since = has_due_payment_since;
    m_has_due_payment_since_isSet = true;
}

bool OAISubscriptionPlan::is_has_due_payment_since_Set() const{
    return m_has_due_payment_since_isSet;
}

bool OAISubscriptionPlan::is_has_due_payment_since_Valid() const{
    return m_has_due_payment_since_isValid;
}

qint32 OAISubscriptionPlan::getId() const {
    return m_id;
}
void OAISubscriptionPlan::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISubscriptionPlan::is_id_Set() const{
    return m_id_isSet;
}

bool OAISubscriptionPlan::is_id_Valid() const{
    return m_id_isValid;
}

QString OAISubscriptionPlan::getIdentifier() const {
    return m_identifier;
}
void OAISubscriptionPlan::setIdentifier(const QString &identifier) {
    m_identifier = identifier;
    m_identifier_isSet = true;
}

bool OAISubscriptionPlan::is_identifier_Set() const{
    return m_identifier_isSet;
}

bool OAISubscriptionPlan::is_identifier_Valid() const{
    return m_identifier_isValid;
}

bool OAISubscriptionPlan::isIsActive() const {
    return m_is_active;
}
void OAISubscriptionPlan::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAISubscriptionPlan::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAISubscriptionPlan::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAISubscriptionPlan::isIsLifetime() const {
    return m_is_lifetime;
}
void OAISubscriptionPlan::setIsLifetime(const bool &is_lifetime) {
    m_is_lifetime = is_lifetime;
    m_is_lifetime_isSet = true;
}

bool OAISubscriptionPlan::is_is_lifetime_Set() const{
    return m_is_lifetime_isSet;
}

bool OAISubscriptionPlan::is_is_lifetime_Valid() const{
    return m_is_lifetime_isValid;
}

QDateTime OAISubscriptionPlan::getLastPaymentOn() const {
    return m_last_payment_on;
}
void OAISubscriptionPlan::setLastPaymentOn(const QDateTime &last_payment_on) {
    m_last_payment_on = last_payment_on;
    m_last_payment_on_isSet = true;
}

bool OAISubscriptionPlan::is_last_payment_on_Set() const{
    return m_last_payment_on_isSet;
}

bool OAISubscriptionPlan::is_last_payment_on_Valid() const{
    return m_last_payment_on_isValid;
}

qint32 OAISubscriptionPlan::getMaxClients() const {
    return m_max_clients;
}
void OAISubscriptionPlan::setMaxClients(const qint32 &max_clients) {
    m_max_clients = max_clients;
    m_max_clients_isSet = true;
}

bool OAISubscriptionPlan::is_max_clients_Set() const{
    return m_max_clients_isSet;
}

bool OAISubscriptionPlan::is_max_clients_Valid() const{
    return m_max_clients_isValid;
}

QString OAISubscriptionPlan::getName() const {
    return m_name;
}
void OAISubscriptionPlan::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISubscriptionPlan::is_name_Set() const{
    return m_name_isSet;
}

bool OAISubscriptionPlan::is_name_Valid() const{
    return m_name_isValid;
}

bool OAISubscriptionPlan::isOnHold() const {
    return m_on_hold;
}
void OAISubscriptionPlan::setOnHold(const bool &on_hold) {
    m_on_hold = on_hold;
    m_on_hold_isSet = true;
}

bool OAISubscriptionPlan::is_on_hold_Set() const{
    return m_on_hold_isSet;
}

bool OAISubscriptionPlan::is_on_hold_Valid() const{
    return m_on_hold_isValid;
}

QString OAISubscriptionPlan::getOrderIdentifier() const {
    return m_order_identifier;
}
void OAISubscriptionPlan::setOrderIdentifier(const QString &order_identifier) {
    m_order_identifier = order_identifier;
    m_order_identifier_isSet = true;
}

bool OAISubscriptionPlan::is_order_identifier_Set() const{
    return m_order_identifier_isSet;
}

bool OAISubscriptionPlan::is_order_identifier_Valid() const{
    return m_order_identifier_isValid;
}

double OAISubscriptionPlan::getPrice() const {
    return m_price;
}
void OAISubscriptionPlan::setPrice(const double &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAISubscriptionPlan::is_price_Set() const{
    return m_price_isSet;
}

bool OAISubscriptionPlan::is_price_Valid() const{
    return m_price_isValid;
}

QString OAISubscriptionPlan::getRecurrence() const {
    return m_recurrence;
}
void OAISubscriptionPlan::setRecurrence(const QString &recurrence) {
    m_recurrence = recurrence;
    m_recurrence_isSet = true;
}

bool OAISubscriptionPlan::is_recurrence_Set() const{
    return m_recurrence_isSet;
}

bool OAISubscriptionPlan::is_recurrence_Valid() const{
    return m_recurrence_isValid;
}

qint64 OAISubscriptionPlan::getSaleId() const {
    return m_sale_id;
}
void OAISubscriptionPlan::setSaleId(const qint64 &sale_id) {
    m_sale_id = sale_id;
    m_sale_id_isSet = true;
}

bool OAISubscriptionPlan::is_sale_id_Set() const{
    return m_sale_id_isSet;
}

bool OAISubscriptionPlan::is_sale_id_Valid() const{
    return m_sale_id_isValid;
}

QString OAISubscriptionPlan::getStatus() const {
    return m_status;
}
void OAISubscriptionPlan::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAISubscriptionPlan::is_status_Set() const{
    return m_status_isSet;
}

bool OAISubscriptionPlan::is_status_Valid() const{
    return m_status_isValid;
}

QString OAISubscriptionPlan::getSystemCancelationReason() const {
    return m_system_cancelation_reason;
}
void OAISubscriptionPlan::setSystemCancelationReason(const QString &system_cancelation_reason) {
    m_system_cancelation_reason = system_cancelation_reason;
    m_system_cancelation_reason_isSet = true;
}

bool OAISubscriptionPlan::is_system_cancelation_reason_Set() const{
    return m_system_cancelation_reason_isSet;
}

bool OAISubscriptionPlan::is_system_cancelation_reason_Valid() const{
    return m_system_cancelation_reason_isValid;
}

QDateTime OAISubscriptionPlan::getTrialEndsOn() const {
    return m_trial_ends_on;
}
void OAISubscriptionPlan::setTrialEndsOn(const QDateTime &trial_ends_on) {
    m_trial_ends_on = trial_ends_on;
    m_trial_ends_on_isSet = true;
}

bool OAISubscriptionPlan::is_trial_ends_on_Set() const{
    return m_trial_ends_on_isSet;
}

bool OAISubscriptionPlan::is_trial_ends_on_Valid() const{
    return m_trial_ends_on_isValid;
}

qint32 OAISubscriptionPlan::getTrialNumberOfDays() const {
    return m_trial_number_of_days;
}
void OAISubscriptionPlan::setTrialNumberOfDays(const qint32 &trial_number_of_days) {
    m_trial_number_of_days = trial_number_of_days;
    m_trial_number_of_days_isSet = true;
}

bool OAISubscriptionPlan::is_trial_number_of_days_Set() const{
    return m_trial_number_of_days_isSet;
}

bool OAISubscriptionPlan::is_trial_number_of_days_Valid() const{
    return m_trial_number_of_days_isValid;
}

QDateTime OAISubscriptionPlan::getTrialStartsOn() const {
    return m_trial_starts_on;
}
void OAISubscriptionPlan::setTrialStartsOn(const QDateTime &trial_starts_on) {
    m_trial_starts_on = trial_starts_on;
    m_trial_starts_on_isSet = true;
}

bool OAISubscriptionPlan::is_trial_starts_on_Set() const{
    return m_trial_starts_on_isSet;
}

bool OAISubscriptionPlan::is_trial_starts_on_Valid() const{
    return m_trial_starts_on_isValid;
}

qint32 OAISubscriptionPlan::getUserId() const {
    return m_user_id;
}
void OAISubscriptionPlan::setUserId(const qint32 &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAISubscriptionPlan::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAISubscriptionPlan::is_user_id_Valid() const{
    return m_user_id_isValid;
}

qint32 OAISubscriptionPlan::getVersion() const {
    return m_version;
}
void OAISubscriptionPlan::setVersion(const qint32 &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAISubscriptionPlan::is_version_Set() const{
    return m_version_isSet;
}

bool OAISubscriptionPlan::is_version_Valid() const{
    return m_version_isValid;
}

bool OAISubscriptionPlan::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cancellated_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coupon_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_features.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_due_payment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_due_payment_since_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_lifetime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_payment_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_clients_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_on_hold_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurrence_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sale_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_system_cancelation_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trial_ends_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trial_number_of_days_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trial_starts_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISubscriptionPlan::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
