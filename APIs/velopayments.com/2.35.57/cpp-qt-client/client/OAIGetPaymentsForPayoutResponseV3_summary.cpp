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

#include "OAIGetPaymentsForPayoutResponseV3_summary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetPaymentsForPayoutResponseV3_summary::OAIGetPaymentsForPayoutResponseV3_summary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetPaymentsForPayoutResponseV3_summary::OAIGetPaymentsForPayoutResponseV3_summary() {
    this->initializeModel();
}

OAIGetPaymentsForPayoutResponseV3_summary::~OAIGetPaymentsForPayoutResponseV3_summary() {}

void OAIGetPaymentsForPayoutResponseV3_summary::initializeModel() {

    m_confirmed_payments_isSet = false;
    m_confirmed_payments_isValid = false;

    m_failed_payments_isSet = false;
    m_failed_payments_isValid = false;

    m_incomplete_payments_isSet = false;
    m_incomplete_payments_isValid = false;

    m_instructed_date_time_isSet = false;
    m_instructed_date_time_isValid = false;

    m_payout_memo_isSet = false;
    m_payout_memo_isValid = false;

    m_payout_status_isSet = false;
    m_payout_status_isValid = false;

    m_released_payments_isSet = false;
    m_released_payments_isValid = false;

    m_submitted_date_time_isSet = false;
    m_submitted_date_time_isValid = false;

    m_total_payments_isSet = false;
    m_total_payments_isValid = false;

    m_withdrawn_date_time_isSet = false;
    m_withdrawn_date_time_isValid = false;
}

void OAIGetPaymentsForPayoutResponseV3_summary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetPaymentsForPayoutResponseV3_summary::fromJsonObject(QJsonObject json) {

    m_confirmed_payments_isValid = ::OpenAPI::fromJsonValue(m_confirmed_payments, json[QString("confirmedPayments")]);
    m_confirmed_payments_isSet = !json[QString("confirmedPayments")].isNull() && m_confirmed_payments_isValid;

    m_failed_payments_isValid = ::OpenAPI::fromJsonValue(m_failed_payments, json[QString("failedPayments")]);
    m_failed_payments_isSet = !json[QString("failedPayments")].isNull() && m_failed_payments_isValid;

    m_incomplete_payments_isValid = ::OpenAPI::fromJsonValue(m_incomplete_payments, json[QString("incompletePayments")]);
    m_incomplete_payments_isSet = !json[QString("incompletePayments")].isNull() && m_incomplete_payments_isValid;

    m_instructed_date_time_isValid = ::OpenAPI::fromJsonValue(m_instructed_date_time, json[QString("instructedDateTime")]);
    m_instructed_date_time_isSet = !json[QString("instructedDateTime")].isNull() && m_instructed_date_time_isValid;

    m_payout_memo_isValid = ::OpenAPI::fromJsonValue(m_payout_memo, json[QString("payoutMemo")]);
    m_payout_memo_isSet = !json[QString("payoutMemo")].isNull() && m_payout_memo_isValid;

    m_payout_status_isValid = ::OpenAPI::fromJsonValue(m_payout_status, json[QString("payoutStatus")]);
    m_payout_status_isSet = !json[QString("payoutStatus")].isNull() && m_payout_status_isValid;

    m_released_payments_isValid = ::OpenAPI::fromJsonValue(m_released_payments, json[QString("releasedPayments")]);
    m_released_payments_isSet = !json[QString("releasedPayments")].isNull() && m_released_payments_isValid;

    m_submitted_date_time_isValid = ::OpenAPI::fromJsonValue(m_submitted_date_time, json[QString("submittedDateTime")]);
    m_submitted_date_time_isSet = !json[QString("submittedDateTime")].isNull() && m_submitted_date_time_isValid;

    m_total_payments_isValid = ::OpenAPI::fromJsonValue(m_total_payments, json[QString("totalPayments")]);
    m_total_payments_isSet = !json[QString("totalPayments")].isNull() && m_total_payments_isValid;

    m_withdrawn_date_time_isValid = ::OpenAPI::fromJsonValue(m_withdrawn_date_time, json[QString("withdrawnDateTime")]);
    m_withdrawn_date_time_isSet = !json[QString("withdrawnDateTime")].isNull() && m_withdrawn_date_time_isValid;
}

QString OAIGetPaymentsForPayoutResponseV3_summary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetPaymentsForPayoutResponseV3_summary::asJsonObject() const {
    QJsonObject obj;
    if (m_confirmed_payments_isSet) {
        obj.insert(QString("confirmedPayments"), ::OpenAPI::toJsonValue(m_confirmed_payments));
    }
    if (m_failed_payments_isSet) {
        obj.insert(QString("failedPayments"), ::OpenAPI::toJsonValue(m_failed_payments));
    }
    if (m_incomplete_payments_isSet) {
        obj.insert(QString("incompletePayments"), ::OpenAPI::toJsonValue(m_incomplete_payments));
    }
    if (m_instructed_date_time_isSet) {
        obj.insert(QString("instructedDateTime"), ::OpenAPI::toJsonValue(m_instructed_date_time));
    }
    if (m_payout_memo_isSet) {
        obj.insert(QString("payoutMemo"), ::OpenAPI::toJsonValue(m_payout_memo));
    }
    if (m_payout_status_isSet) {
        obj.insert(QString("payoutStatus"), ::OpenAPI::toJsonValue(m_payout_status));
    }
    if (m_released_payments_isSet) {
        obj.insert(QString("releasedPayments"), ::OpenAPI::toJsonValue(m_released_payments));
    }
    if (m_submitted_date_time_isSet) {
        obj.insert(QString("submittedDateTime"), ::OpenAPI::toJsonValue(m_submitted_date_time));
    }
    if (m_total_payments_isSet) {
        obj.insert(QString("totalPayments"), ::OpenAPI::toJsonValue(m_total_payments));
    }
    if (m_withdrawn_date_time_isSet) {
        obj.insert(QString("withdrawnDateTime"), ::OpenAPI::toJsonValue(m_withdrawn_date_time));
    }
    return obj;
}

qint32 OAIGetPaymentsForPayoutResponseV3_summary::getConfirmedPayments() const {
    return m_confirmed_payments;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setConfirmedPayments(const qint32 &confirmed_payments) {
    m_confirmed_payments = confirmed_payments;
    m_confirmed_payments_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_confirmed_payments_Set() const{
    return m_confirmed_payments_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_confirmed_payments_Valid() const{
    return m_confirmed_payments_isValid;
}

qint32 OAIGetPaymentsForPayoutResponseV3_summary::getFailedPayments() const {
    return m_failed_payments;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setFailedPayments(const qint32 &failed_payments) {
    m_failed_payments = failed_payments;
    m_failed_payments_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_failed_payments_Set() const{
    return m_failed_payments_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_failed_payments_Valid() const{
    return m_failed_payments_isValid;
}

qint32 OAIGetPaymentsForPayoutResponseV3_summary::getIncompletePayments() const {
    return m_incomplete_payments;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setIncompletePayments(const qint32 &incomplete_payments) {
    m_incomplete_payments = incomplete_payments;
    m_incomplete_payments_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_incomplete_payments_Set() const{
    return m_incomplete_payments_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_incomplete_payments_Valid() const{
    return m_incomplete_payments_isValid;
}

QDateTime OAIGetPaymentsForPayoutResponseV3_summary::getInstructedDateTime() const {
    return m_instructed_date_time;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setInstructedDateTime(const QDateTime &instructed_date_time) {
    m_instructed_date_time = instructed_date_time;
    m_instructed_date_time_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_instructed_date_time_Set() const{
    return m_instructed_date_time_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_instructed_date_time_Valid() const{
    return m_instructed_date_time_isValid;
}

QString OAIGetPaymentsForPayoutResponseV3_summary::getPayoutMemo() const {
    return m_payout_memo;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setPayoutMemo(const QString &payout_memo) {
    m_payout_memo = payout_memo;
    m_payout_memo_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_payout_memo_Set() const{
    return m_payout_memo_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_payout_memo_Valid() const{
    return m_payout_memo_isValid;
}

QString OAIGetPaymentsForPayoutResponseV3_summary::getPayoutStatus() const {
    return m_payout_status;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setPayoutStatus(const QString &payout_status) {
    m_payout_status = payout_status;
    m_payout_status_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_payout_status_Set() const{
    return m_payout_status_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_payout_status_Valid() const{
    return m_payout_status_isValid;
}

qint32 OAIGetPaymentsForPayoutResponseV3_summary::getReleasedPayments() const {
    return m_released_payments;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setReleasedPayments(const qint32 &released_payments) {
    m_released_payments = released_payments;
    m_released_payments_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_released_payments_Set() const{
    return m_released_payments_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_released_payments_Valid() const{
    return m_released_payments_isValid;
}

QDateTime OAIGetPaymentsForPayoutResponseV3_summary::getSubmittedDateTime() const {
    return m_submitted_date_time;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setSubmittedDateTime(const QDateTime &submitted_date_time) {
    m_submitted_date_time = submitted_date_time;
    m_submitted_date_time_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_submitted_date_time_Set() const{
    return m_submitted_date_time_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_submitted_date_time_Valid() const{
    return m_submitted_date_time_isValid;
}

qint32 OAIGetPaymentsForPayoutResponseV3_summary::getTotalPayments() const {
    return m_total_payments;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setTotalPayments(const qint32 &total_payments) {
    m_total_payments = total_payments;
    m_total_payments_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_total_payments_Set() const{
    return m_total_payments_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_total_payments_Valid() const{
    return m_total_payments_isValid;
}

QDateTime OAIGetPaymentsForPayoutResponseV3_summary::getWithdrawnDateTime() const {
    return m_withdrawn_date_time;
}
void OAIGetPaymentsForPayoutResponseV3_summary::setWithdrawnDateTime(const QDateTime &withdrawn_date_time) {
    m_withdrawn_date_time = withdrawn_date_time;
    m_withdrawn_date_time_isSet = true;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_withdrawn_date_time_Set() const{
    return m_withdrawn_date_time_isSet;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::is_withdrawn_date_time_Valid() const{
    return m_withdrawn_date_time_isValid;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_confirmed_payments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_failed_payments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_incomplete_payments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_instructed_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payout_memo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payout_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_released_payments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_submitted_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_payments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_withdrawn_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetPaymentsForPayoutResponseV3_summary::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
