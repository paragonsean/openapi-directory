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

#include "OAIInvoiceDetailsApiModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInvoiceDetailsApiModel::OAIInvoiceDetailsApiModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInvoiceDetailsApiModel::OAIInvoiceDetailsApiModel() {
    this->initializeModel();
}

OAIInvoiceDetailsApiModel::~OAIInvoiceDetailsApiModel() {}

void OAIInvoiceDetailsApiModel::initializeModel() {

    m_access_token_isSet = false;
    m_access_token_isValid = false;

    m_client_isSet = false;
    m_client_isValid = false;

    m_cloned_from_id_isSet = false;
    m_cloned_from_id_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_discount_amount_isSet = false;
    m_discount_amount_isValid = false;

    m_duedate_isSet = false;
    m_duedate_isValid = false;

    m_enable_partial_payments_isSet = false;
    m_enable_partial_payments_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invoice_category_id_isSet = false;
    m_invoice_category_id_isValid = false;

    m_issued_on_isSet = false;
    m_issued_on_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_po_number_isSet = false;
    m_po_number_isValid = false;

    m_recurring_profile_isSet = false;
    m_recurring_profile_isValid = false;

    m_recurring_profile_id_isSet = false;
    m_recurring_profile_id_isValid = false;

    m_should_send_reminders_isSet = false;
    m_should_send_reminders_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_sub_total_amount_isSet = false;
    m_sub_total_amount_isValid = false;

    m_tax_amount_isSet = false;
    m_tax_amount_isValid = false;

    m_terms_isSet = false;
    m_terms_isValid = false;

    m_total_amount_isSet = false;
    m_total_amount_isValid = false;
}

void OAIInvoiceDetailsApiModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInvoiceDetailsApiModel::fromJsonObject(QJsonObject json) {

    m_access_token_isValid = ::OpenAPI::fromJsonValue(m_access_token, json[QString("AccessToken")]);
    m_access_token_isSet = !json[QString("AccessToken")].isNull() && m_access_token_isValid;

    m_client_isValid = ::OpenAPI::fromJsonValue(m_client, json[QString("Client")]);
    m_client_isSet = !json[QString("Client")].isNull() && m_client_isValid;

    m_cloned_from_id_isValid = ::OpenAPI::fromJsonValue(m_cloned_from_id, json[QString("ClonedFromId")]);
    m_cloned_from_id_isSet = !json[QString("ClonedFromId")].isNull() && m_cloned_from_id_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("Currency")]);
    m_currency_isSet = !json[QString("Currency")].isNull() && m_currency_isValid;

    m_discount_amount_isValid = ::OpenAPI::fromJsonValue(m_discount_amount, json[QString("DiscountAmount")]);
    m_discount_amount_isSet = !json[QString("DiscountAmount")].isNull() && m_discount_amount_isValid;

    m_duedate_isValid = ::OpenAPI::fromJsonValue(m_duedate, json[QString("Duedate")]);
    m_duedate_isSet = !json[QString("Duedate")].isNull() && m_duedate_isValid;

    m_enable_partial_payments_isValid = ::OpenAPI::fromJsonValue(m_enable_partial_payments, json[QString("EnablePartialPayments")]);
    m_enable_partial_payments_isSet = !json[QString("EnablePartialPayments")].isNull() && m_enable_partial_payments_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_invoice_category_id_isValid = ::OpenAPI::fromJsonValue(m_invoice_category_id, json[QString("InvoiceCategoryId")]);
    m_invoice_category_id_isSet = !json[QString("InvoiceCategoryId")].isNull() && m_invoice_category_id_isValid;

    m_issued_on_isValid = ::OpenAPI::fromJsonValue(m_issued_on, json[QString("IssuedOn")]);
    m_issued_on_isSet = !json[QString("IssuedOn")].isNull() && m_issued_on_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("Notes")]);
    m_notes_isSet = !json[QString("Notes")].isNull() && m_notes_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("Number")]);
    m_number_isSet = !json[QString("Number")].isNull() && m_number_isValid;

    m_po_number_isValid = ::OpenAPI::fromJsonValue(m_po_number, json[QString("PoNumber")]);
    m_po_number_isSet = !json[QString("PoNumber")].isNull() && m_po_number_isValid;

    m_recurring_profile_isValid = ::OpenAPI::fromJsonValue(m_recurring_profile, json[QString("RecurringProfile")]);
    m_recurring_profile_isSet = !json[QString("RecurringProfile")].isNull() && m_recurring_profile_isValid;

    m_recurring_profile_id_isValid = ::OpenAPI::fromJsonValue(m_recurring_profile_id, json[QString("RecurringProfileId")]);
    m_recurring_profile_id_isSet = !json[QString("RecurringProfileId")].isNull() && m_recurring_profile_id_isValid;

    m_should_send_reminders_isValid = ::OpenAPI::fromJsonValue(m_should_send_reminders, json[QString("ShouldSendReminders")]);
    m_should_send_reminders_isSet = !json[QString("ShouldSendReminders")].isNull() && m_should_send_reminders_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;

    m_sub_total_amount_isValid = ::OpenAPI::fromJsonValue(m_sub_total_amount, json[QString("SubTotalAmount")]);
    m_sub_total_amount_isSet = !json[QString("SubTotalAmount")].isNull() && m_sub_total_amount_isValid;

    m_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_tax_amount, json[QString("TaxAmount")]);
    m_tax_amount_isSet = !json[QString("TaxAmount")].isNull() && m_tax_amount_isValid;

    m_terms_isValid = ::OpenAPI::fromJsonValue(m_terms, json[QString("Terms")]);
    m_terms_isSet = !json[QString("Terms")].isNull() && m_terms_isValid;

    m_total_amount_isValid = ::OpenAPI::fromJsonValue(m_total_amount, json[QString("TotalAmount")]);
    m_total_amount_isSet = !json[QString("TotalAmount")].isNull() && m_total_amount_isValid;
}

QString OAIInvoiceDetailsApiModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInvoiceDetailsApiModel::asJsonObject() const {
    QJsonObject obj;
    if (m_access_token_isSet) {
        obj.insert(QString("AccessToken"), ::OpenAPI::toJsonValue(m_access_token));
    }
    if (m_client.isSet()) {
        obj.insert(QString("Client"), ::OpenAPI::toJsonValue(m_client));
    }
    if (m_cloned_from_id_isSet) {
        obj.insert(QString("ClonedFromId"), ::OpenAPI::toJsonValue(m_cloned_from_id));
    }
    if (m_currency.isSet()) {
        obj.insert(QString("Currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_discount_amount_isSet) {
        obj.insert(QString("DiscountAmount"), ::OpenAPI::toJsonValue(m_discount_amount));
    }
    if (m_duedate_isSet) {
        obj.insert(QString("Duedate"), ::OpenAPI::toJsonValue(m_duedate));
    }
    if (m_enable_partial_payments_isSet) {
        obj.insert(QString("EnablePartialPayments"), ::OpenAPI::toJsonValue(m_enable_partial_payments));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invoice_category_id_isSet) {
        obj.insert(QString("InvoiceCategoryId"), ::OpenAPI::toJsonValue(m_invoice_category_id));
    }
    if (m_issued_on_isSet) {
        obj.insert(QString("IssuedOn"), ::OpenAPI::toJsonValue(m_issued_on));
    }
    if (m_notes_isSet) {
        obj.insert(QString("Notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_number_isSet) {
        obj.insert(QString("Number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_po_number_isSet) {
        obj.insert(QString("PoNumber"), ::OpenAPI::toJsonValue(m_po_number));
    }
    if (m_recurring_profile.isSet()) {
        obj.insert(QString("RecurringProfile"), ::OpenAPI::toJsonValue(m_recurring_profile));
    }
    if (m_recurring_profile_id_isSet) {
        obj.insert(QString("RecurringProfileId"), ::OpenAPI::toJsonValue(m_recurring_profile_id));
    }
    if (m_should_send_reminders_isSet) {
        obj.insert(QString("ShouldSendReminders"), ::OpenAPI::toJsonValue(m_should_send_reminders));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_sub_total_amount_isSet) {
        obj.insert(QString("SubTotalAmount"), ::OpenAPI::toJsonValue(m_sub_total_amount));
    }
    if (m_tax_amount_isSet) {
        obj.insert(QString("TaxAmount"), ::OpenAPI::toJsonValue(m_tax_amount));
    }
    if (m_terms_isSet) {
        obj.insert(QString("Terms"), ::OpenAPI::toJsonValue(m_terms));
    }
    if (m_total_amount_isSet) {
        obj.insert(QString("TotalAmount"), ::OpenAPI::toJsonValue(m_total_amount));
    }
    return obj;
}

QString OAIInvoiceDetailsApiModel::getAccessToken() const {
    return m_access_token;
}
void OAIInvoiceDetailsApiModel::setAccessToken(const QString &access_token) {
    m_access_token = access_token;
    m_access_token_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_access_token_Set() const{
    return m_access_token_isSet;
}

bool OAIInvoiceDetailsApiModel::is_access_token_Valid() const{
    return m_access_token_isValid;
}

OAIClientDetailsApiModel OAIInvoiceDetailsApiModel::getClient() const {
    return m_client;
}
void OAIInvoiceDetailsApiModel::setClient(const OAIClientDetailsApiModel &client) {
    m_client = client;
    m_client_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_client_Set() const{
    return m_client_isSet;
}

bool OAIInvoiceDetailsApiModel::is_client_Valid() const{
    return m_client_isValid;
}

qint32 OAIInvoiceDetailsApiModel::getClonedFromId() const {
    return m_cloned_from_id;
}
void OAIInvoiceDetailsApiModel::setClonedFromId(const qint32 &cloned_from_id) {
    m_cloned_from_id = cloned_from_id;
    m_cloned_from_id_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_cloned_from_id_Set() const{
    return m_cloned_from_id_isSet;
}

bool OAIInvoiceDetailsApiModel::is_cloned_from_id_Valid() const{
    return m_cloned_from_id_isValid;
}

OAICurrencyDetailsApiModel OAIInvoiceDetailsApiModel::getCurrency() const {
    return m_currency;
}
void OAIInvoiceDetailsApiModel::setCurrency(const OAICurrencyDetailsApiModel &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIInvoiceDetailsApiModel::is_currency_Valid() const{
    return m_currency_isValid;
}

double OAIInvoiceDetailsApiModel::getDiscountAmount() const {
    return m_discount_amount;
}
void OAIInvoiceDetailsApiModel::setDiscountAmount(const double &discount_amount) {
    m_discount_amount = discount_amount;
    m_discount_amount_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_discount_amount_Set() const{
    return m_discount_amount_isSet;
}

bool OAIInvoiceDetailsApiModel::is_discount_amount_Valid() const{
    return m_discount_amount_isValid;
}

QDateTime OAIInvoiceDetailsApiModel::getDuedate() const {
    return m_duedate;
}
void OAIInvoiceDetailsApiModel::setDuedate(const QDateTime &duedate) {
    m_duedate = duedate;
    m_duedate_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_duedate_Set() const{
    return m_duedate_isSet;
}

bool OAIInvoiceDetailsApiModel::is_duedate_Valid() const{
    return m_duedate_isValid;
}

bool OAIInvoiceDetailsApiModel::isEnablePartialPayments() const {
    return m_enable_partial_payments;
}
void OAIInvoiceDetailsApiModel::setEnablePartialPayments(const bool &enable_partial_payments) {
    m_enable_partial_payments = enable_partial_payments;
    m_enable_partial_payments_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_enable_partial_payments_Set() const{
    return m_enable_partial_payments_isSet;
}

bool OAIInvoiceDetailsApiModel::is_enable_partial_payments_Valid() const{
    return m_enable_partial_payments_isValid;
}

qint32 OAIInvoiceDetailsApiModel::getId() const {
    return m_id;
}
void OAIInvoiceDetailsApiModel::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_id_Set() const{
    return m_id_isSet;
}

bool OAIInvoiceDetailsApiModel::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIInvoiceDetailsApiModel::getInvoiceCategoryId() const {
    return m_invoice_category_id;
}
void OAIInvoiceDetailsApiModel::setInvoiceCategoryId(const qint32 &invoice_category_id) {
    m_invoice_category_id = invoice_category_id;
    m_invoice_category_id_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_invoice_category_id_Set() const{
    return m_invoice_category_id_isSet;
}

bool OAIInvoiceDetailsApiModel::is_invoice_category_id_Valid() const{
    return m_invoice_category_id_isValid;
}

QDateTime OAIInvoiceDetailsApiModel::getIssuedOn() const {
    return m_issued_on;
}
void OAIInvoiceDetailsApiModel::setIssuedOn(const QDateTime &issued_on) {
    m_issued_on = issued_on;
    m_issued_on_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_issued_on_Set() const{
    return m_issued_on_isSet;
}

bool OAIInvoiceDetailsApiModel::is_issued_on_Valid() const{
    return m_issued_on_isValid;
}

QString OAIInvoiceDetailsApiModel::getNotes() const {
    return m_notes;
}
void OAIInvoiceDetailsApiModel::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIInvoiceDetailsApiModel::is_notes_Valid() const{
    return m_notes_isValid;
}

QString OAIInvoiceDetailsApiModel::getNumber() const {
    return m_number;
}
void OAIInvoiceDetailsApiModel::setNumber(const QString &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_number_Set() const{
    return m_number_isSet;
}

bool OAIInvoiceDetailsApiModel::is_number_Valid() const{
    return m_number_isValid;
}

QString OAIInvoiceDetailsApiModel::getPoNumber() const {
    return m_po_number;
}
void OAIInvoiceDetailsApiModel::setPoNumber(const QString &po_number) {
    m_po_number = po_number;
    m_po_number_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_po_number_Set() const{
    return m_po_number_isSet;
}

bool OAIInvoiceDetailsApiModel::is_po_number_Valid() const{
    return m_po_number_isValid;
}

OAIInvoiceRecurringApiModel OAIInvoiceDetailsApiModel::getRecurringProfile() const {
    return m_recurring_profile;
}
void OAIInvoiceDetailsApiModel::setRecurringProfile(const OAIInvoiceRecurringApiModel &recurring_profile) {
    m_recurring_profile = recurring_profile;
    m_recurring_profile_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_recurring_profile_Set() const{
    return m_recurring_profile_isSet;
}

bool OAIInvoiceDetailsApiModel::is_recurring_profile_Valid() const{
    return m_recurring_profile_isValid;
}

qint32 OAIInvoiceDetailsApiModel::getRecurringProfileId() const {
    return m_recurring_profile_id;
}
void OAIInvoiceDetailsApiModel::setRecurringProfileId(const qint32 &recurring_profile_id) {
    m_recurring_profile_id = recurring_profile_id;
    m_recurring_profile_id_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_recurring_profile_id_Set() const{
    return m_recurring_profile_id_isSet;
}

bool OAIInvoiceDetailsApiModel::is_recurring_profile_id_Valid() const{
    return m_recurring_profile_id_isValid;
}

bool OAIInvoiceDetailsApiModel::isShouldSendReminders() const {
    return m_should_send_reminders;
}
void OAIInvoiceDetailsApiModel::setShouldSendReminders(const bool &should_send_reminders) {
    m_should_send_reminders = should_send_reminders;
    m_should_send_reminders_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_should_send_reminders_Set() const{
    return m_should_send_reminders_isSet;
}

bool OAIInvoiceDetailsApiModel::is_should_send_reminders_Valid() const{
    return m_should_send_reminders_isValid;
}

QString OAIInvoiceDetailsApiModel::getStatus() const {
    return m_status;
}
void OAIInvoiceDetailsApiModel::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_status_Set() const{
    return m_status_isSet;
}

bool OAIInvoiceDetailsApiModel::is_status_Valid() const{
    return m_status_isValid;
}

double OAIInvoiceDetailsApiModel::getSubTotalAmount() const {
    return m_sub_total_amount;
}
void OAIInvoiceDetailsApiModel::setSubTotalAmount(const double &sub_total_amount) {
    m_sub_total_amount = sub_total_amount;
    m_sub_total_amount_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_sub_total_amount_Set() const{
    return m_sub_total_amount_isSet;
}

bool OAIInvoiceDetailsApiModel::is_sub_total_amount_Valid() const{
    return m_sub_total_amount_isValid;
}

double OAIInvoiceDetailsApiModel::getTaxAmount() const {
    return m_tax_amount;
}
void OAIInvoiceDetailsApiModel::setTaxAmount(const double &tax_amount) {
    m_tax_amount = tax_amount;
    m_tax_amount_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_tax_amount_Set() const{
    return m_tax_amount_isSet;
}

bool OAIInvoiceDetailsApiModel::is_tax_amount_Valid() const{
    return m_tax_amount_isValid;
}

QString OAIInvoiceDetailsApiModel::getTerms() const {
    return m_terms;
}
void OAIInvoiceDetailsApiModel::setTerms(const QString &terms) {
    m_terms = terms;
    m_terms_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_terms_Set() const{
    return m_terms_isSet;
}

bool OAIInvoiceDetailsApiModel::is_terms_Valid() const{
    return m_terms_isValid;
}

double OAIInvoiceDetailsApiModel::getTotalAmount() const {
    return m_total_amount;
}
void OAIInvoiceDetailsApiModel::setTotalAmount(const double &total_amount) {
    m_total_amount = total_amount;
    m_total_amount_isSet = true;
}

bool OAIInvoiceDetailsApiModel::is_total_amount_Set() const{
    return m_total_amount_isSet;
}

bool OAIInvoiceDetailsApiModel::is_total_amount_Valid() const{
    return m_total_amount_isValid;
}

bool OAIInvoiceDetailsApiModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cloned_from_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duedate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enable_partial_payments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_category_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_issued_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_po_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurring_profile.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurring_profile_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_should_send_reminders_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
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

        if (m_terms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_amount_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInvoiceDetailsApiModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
