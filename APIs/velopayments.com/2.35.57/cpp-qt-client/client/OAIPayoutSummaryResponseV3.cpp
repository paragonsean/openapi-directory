/**
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPayoutSummaryResponseV3.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPayoutSummaryResponseV3::OAIPayoutSummaryResponseV3(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPayoutSummaryResponseV3::OAIPayoutSummaryResponseV3() {
    this->initializeModel();
}

OAIPayoutSummaryResponseV3::~OAIPayoutSummaryResponseV3() {}

void OAIPayoutSummaryResponseV3::initializeModel() {

    m_accepted_payments_isSet = false;
    m_accepted_payments_isValid = false;

    m_accounts_isSet = false;
    m_accounts_isValid = false;

    m_fx_summaries_isSet = false;
    m_fx_summaries_isValid = false;

    m_payments_accepted_isSet = false;
    m_payments_accepted_isValid = false;

    m_payments_rejected_isSet = false;
    m_payments_rejected_isValid = false;

    m_payments_submitted_isSet = false;
    m_payments_submitted_isValid = false;

    m_payments_withdrawn_isSet = false;
    m_payments_withdrawn_isValid = false;

    m_payout_id_isSet = false;
    m_payout_id_isValid = false;

    m_rejected_payments_isSet = false;
    m_rejected_payments_isValid = false;

    m_schedule_isSet = false;
    m_schedule_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIPayoutSummaryResponseV3::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPayoutSummaryResponseV3::fromJsonObject(QJsonObject json) {

    m_accepted_payments_isValid = ::OpenAPI::fromJsonValue(m_accepted_payments, json[QString("acceptedPayments")]);
    m_accepted_payments_isSet = !json[QString("acceptedPayments")].isNull() && m_accepted_payments_isValid;

    m_accounts_isValid = ::OpenAPI::fromJsonValue(m_accounts, json[QString("accounts")]);
    m_accounts_isSet = !json[QString("accounts")].isNull() && m_accounts_isValid;

    m_fx_summaries_isValid = ::OpenAPI::fromJsonValue(m_fx_summaries, json[QString("fxSummaries")]);
    m_fx_summaries_isSet = !json[QString("fxSummaries")].isNull() && m_fx_summaries_isValid;

    m_payments_accepted_isValid = ::OpenAPI::fromJsonValue(m_payments_accepted, json[QString("paymentsAccepted")]);
    m_payments_accepted_isSet = !json[QString("paymentsAccepted")].isNull() && m_payments_accepted_isValid;

    m_payments_rejected_isValid = ::OpenAPI::fromJsonValue(m_payments_rejected, json[QString("paymentsRejected")]);
    m_payments_rejected_isSet = !json[QString("paymentsRejected")].isNull() && m_payments_rejected_isValid;

    m_payments_submitted_isValid = ::OpenAPI::fromJsonValue(m_payments_submitted, json[QString("paymentsSubmitted")]);
    m_payments_submitted_isSet = !json[QString("paymentsSubmitted")].isNull() && m_payments_submitted_isValid;

    m_payments_withdrawn_isValid = ::OpenAPI::fromJsonValue(m_payments_withdrawn, json[QString("paymentsWithdrawn")]);
    m_payments_withdrawn_isSet = !json[QString("paymentsWithdrawn")].isNull() && m_payments_withdrawn_isValid;

    m_payout_id_isValid = ::OpenAPI::fromJsonValue(m_payout_id, json[QString("payoutId")]);
    m_payout_id_isSet = !json[QString("payoutId")].isNull() && m_payout_id_isValid;

    m_rejected_payments_isValid = ::OpenAPI::fromJsonValue(m_rejected_payments, json[QString("rejectedPayments")]);
    m_rejected_payments_isSet = !json[QString("rejectedPayments")].isNull() && m_rejected_payments_isValid;

    m_schedule_isValid = ::OpenAPI::fromJsonValue(m_schedule, json[QString("schedule")]);
    m_schedule_isSet = !json[QString("schedule")].isNull() && m_schedule_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIPayoutSummaryResponseV3::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPayoutSummaryResponseV3::asJsonObject() const {
    QJsonObject obj;
    if (m_accepted_payments.size() > 0) {
        obj.insert(QString("acceptedPayments"), ::OpenAPI::toJsonValue(m_accepted_payments));
    }
    if (m_accounts.size() > 0) {
        obj.insert(QString("accounts"), ::OpenAPI::toJsonValue(m_accounts));
    }
    if (m_fx_summaries.size() > 0) {
        obj.insert(QString("fxSummaries"), ::OpenAPI::toJsonValue(m_fx_summaries));
    }
    if (m_payments_accepted_isSet) {
        obj.insert(QString("paymentsAccepted"), ::OpenAPI::toJsonValue(m_payments_accepted));
    }
    if (m_payments_rejected_isSet) {
        obj.insert(QString("paymentsRejected"), ::OpenAPI::toJsonValue(m_payments_rejected));
    }
    if (m_payments_submitted_isSet) {
        obj.insert(QString("paymentsSubmitted"), ::OpenAPI::toJsonValue(m_payments_submitted));
    }
    if (m_payments_withdrawn_isSet) {
        obj.insert(QString("paymentsWithdrawn"), ::OpenAPI::toJsonValue(m_payments_withdrawn));
    }
    if (m_payout_id_isSet) {
        obj.insert(QString("payoutId"), ::OpenAPI::toJsonValue(m_payout_id));
    }
    if (m_rejected_payments.size() > 0) {
        obj.insert(QString("rejectedPayments"), ::OpenAPI::toJsonValue(m_rejected_payments));
    }
    if (m_schedule.isSet()) {
        obj.insert(QString("schedule"), ::OpenAPI::toJsonValue(m_schedule));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QList<OAIAcceptedPaymentV3> OAIPayoutSummaryResponseV3::getAcceptedPayments() const {
    return m_accepted_payments;
}
void OAIPayoutSummaryResponseV3::setAcceptedPayments(const QList<OAIAcceptedPaymentV3> &accepted_payments) {
    m_accepted_payments = accepted_payments;
    m_accepted_payments_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_accepted_payments_Set() const{
    return m_accepted_payments_isSet;
}

bool OAIPayoutSummaryResponseV3::is_accepted_payments_Valid() const{
    return m_accepted_payments_isValid;
}

QList<OAISourceAccountV3> OAIPayoutSummaryResponseV3::getAccounts() const {
    return m_accounts;
}
void OAIPayoutSummaryResponseV3::setAccounts(const QList<OAISourceAccountV3> &accounts) {
    m_accounts = accounts;
    m_accounts_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_accounts_Set() const{
    return m_accounts_isSet;
}

bool OAIPayoutSummaryResponseV3::is_accounts_Valid() const{
    return m_accounts_isValid;
}

QList<OAIQuoteFxSummaryV3> OAIPayoutSummaryResponseV3::getFxSummaries() const {
    return m_fx_summaries;
}
void OAIPayoutSummaryResponseV3::setFxSummaries(const QList<OAIQuoteFxSummaryV3> &fx_summaries) {
    m_fx_summaries = fx_summaries;
    m_fx_summaries_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_fx_summaries_Set() const{
    return m_fx_summaries_isSet;
}

bool OAIPayoutSummaryResponseV3::is_fx_summaries_Valid() const{
    return m_fx_summaries_isValid;
}

qint32 OAIPayoutSummaryResponseV3::getPaymentsAccepted() const {
    return m_payments_accepted;
}
void OAIPayoutSummaryResponseV3::setPaymentsAccepted(const qint32 &payments_accepted) {
    m_payments_accepted = payments_accepted;
    m_payments_accepted_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_payments_accepted_Set() const{
    return m_payments_accepted_isSet;
}

bool OAIPayoutSummaryResponseV3::is_payments_accepted_Valid() const{
    return m_payments_accepted_isValid;
}

qint32 OAIPayoutSummaryResponseV3::getPaymentsRejected() const {
    return m_payments_rejected;
}
void OAIPayoutSummaryResponseV3::setPaymentsRejected(const qint32 &payments_rejected) {
    m_payments_rejected = payments_rejected;
    m_payments_rejected_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_payments_rejected_Set() const{
    return m_payments_rejected_isSet;
}

bool OAIPayoutSummaryResponseV3::is_payments_rejected_Valid() const{
    return m_payments_rejected_isValid;
}

qint32 OAIPayoutSummaryResponseV3::getPaymentsSubmitted() const {
    return m_payments_submitted;
}
void OAIPayoutSummaryResponseV3::setPaymentsSubmitted(const qint32 &payments_submitted) {
    m_payments_submitted = payments_submitted;
    m_payments_submitted_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_payments_submitted_Set() const{
    return m_payments_submitted_isSet;
}

bool OAIPayoutSummaryResponseV3::is_payments_submitted_Valid() const{
    return m_payments_submitted_isValid;
}

qint32 OAIPayoutSummaryResponseV3::getPaymentsWithdrawn() const {
    return m_payments_withdrawn;
}
void OAIPayoutSummaryResponseV3::setPaymentsWithdrawn(const qint32 &payments_withdrawn) {
    m_payments_withdrawn = payments_withdrawn;
    m_payments_withdrawn_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_payments_withdrawn_Set() const{
    return m_payments_withdrawn_isSet;
}

bool OAIPayoutSummaryResponseV3::is_payments_withdrawn_Valid() const{
    return m_payments_withdrawn_isValid;
}

QString OAIPayoutSummaryResponseV3::getPayoutId() const {
    return m_payout_id;
}
void OAIPayoutSummaryResponseV3::setPayoutId(const QString &payout_id) {
    m_payout_id = payout_id;
    m_payout_id_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_payout_id_Set() const{
    return m_payout_id_isSet;
}

bool OAIPayoutSummaryResponseV3::is_payout_id_Valid() const{
    return m_payout_id_isValid;
}

QList<OAIRejectedPaymentV3> OAIPayoutSummaryResponseV3::getRejectedPayments() const {
    return m_rejected_payments;
}
void OAIPayoutSummaryResponseV3::setRejectedPayments(const QList<OAIRejectedPaymentV3> &rejected_payments) {
    m_rejected_payments = rejected_payments;
    m_rejected_payments_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_rejected_payments_Set() const{
    return m_rejected_payments_isSet;
}

bool OAIPayoutSummaryResponseV3::is_rejected_payments_Valid() const{
    return m_rejected_payments_isValid;
}

OAIPayoutScheduleV3 OAIPayoutSummaryResponseV3::getSchedule() const {
    return m_schedule;
}
void OAIPayoutSummaryResponseV3::setSchedule(const OAIPayoutScheduleV3 &schedule) {
    m_schedule = schedule;
    m_schedule_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_schedule_Set() const{
    return m_schedule_isSet;
}

bool OAIPayoutSummaryResponseV3::is_schedule_Valid() const{
    return m_schedule_isValid;
}

QString OAIPayoutSummaryResponseV3::getStatus() const {
    return m_status;
}
void OAIPayoutSummaryResponseV3::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPayoutSummaryResponseV3::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPayoutSummaryResponseV3::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIPayoutSummaryResponseV3::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_accepted_payments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_fx_summaries.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_payments_accepted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payments_rejected_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payments_submitted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payments_withdrawn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payout_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rejected_payments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPayoutSummaryResponseV3::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_accepted_payments_isValid && m_accounts_isValid && m_fx_summaries_isValid && m_payments_withdrawn_isValid && m_rejected_payments_isValid && true;
}

} // namespace OpenAPI
