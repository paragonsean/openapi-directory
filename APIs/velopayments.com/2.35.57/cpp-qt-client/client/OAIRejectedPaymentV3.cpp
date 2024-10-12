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

#include "OAIRejectedPaymentV3.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRejectedPaymentV3::OAIRejectedPaymentV3(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRejectedPaymentV3::OAIRejectedPaymentV3() {
    this->initializeModel();
}

OAIRejectedPaymentV3::~OAIRejectedPaymentV3() {}

void OAIRejectedPaymentV3::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_currency_type_isSet = false;
    m_currency_type_isValid = false;

    m_line_number_isSet = false;
    m_line_number_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_payment_metadata_isSet = false;
    m_payment_metadata_isValid = false;

    m_payor_payment_id_isSet = false;
    m_payor_payment_id_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_reason_code_isSet = false;
    m_reason_code_isValid = false;

    m_remote_id_isSet = false;
    m_remote_id_isValid = false;

    m_remote_system_id_isSet = false;
    m_remote_system_id_isValid = false;

    m_source_account_name_isSet = false;
    m_source_account_name_isValid = false;
}

void OAIRejectedPaymentV3::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRejectedPaymentV3::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_currency_type_isValid = ::OpenAPI::fromJsonValue(m_currency_type, json[QString("currencyType")]);
    m_currency_type_isSet = !json[QString("currencyType")].isNull() && m_currency_type_isValid;

    m_line_number_isValid = ::OpenAPI::fromJsonValue(m_line_number, json[QString("lineNumber")]);
    m_line_number_isSet = !json[QString("lineNumber")].isNull() && m_line_number_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_payment_metadata_isValid = ::OpenAPI::fromJsonValue(m_payment_metadata, json[QString("paymentMetadata")]);
    m_payment_metadata_isSet = !json[QString("paymentMetadata")].isNull() && m_payment_metadata_isValid;

    m_payor_payment_id_isValid = ::OpenAPI::fromJsonValue(m_payor_payment_id, json[QString("payorPaymentId")]);
    m_payor_payment_id_isSet = !json[QString("payorPaymentId")].isNull() && m_payor_payment_id_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_reason_code_isValid = ::OpenAPI::fromJsonValue(m_reason_code, json[QString("reasonCode")]);
    m_reason_code_isSet = !json[QString("reasonCode")].isNull() && m_reason_code_isValid;

    m_remote_id_isValid = ::OpenAPI::fromJsonValue(m_remote_id, json[QString("remoteId")]);
    m_remote_id_isSet = !json[QString("remoteId")].isNull() && m_remote_id_isValid;

    m_remote_system_id_isValid = ::OpenAPI::fromJsonValue(m_remote_system_id, json[QString("remoteSystemId")]);
    m_remote_system_id_isSet = !json[QString("remoteSystemId")].isNull() && m_remote_system_id_isValid;

    m_source_account_name_isValid = ::OpenAPI::fromJsonValue(m_source_account_name, json[QString("sourceAccountName")]);
    m_source_account_name_isSet = !json[QString("sourceAccountName")].isNull() && m_source_account_name_isValid;
}

QString OAIRejectedPaymentV3::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRejectedPaymentV3::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_currency_type_isSet) {
        obj.insert(QString("currencyType"), ::OpenAPI::toJsonValue(m_currency_type));
    }
    if (m_line_number_isSet) {
        obj.insert(QString("lineNumber"), ::OpenAPI::toJsonValue(m_line_number));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_payment_metadata_isSet) {
        obj.insert(QString("paymentMetadata"), ::OpenAPI::toJsonValue(m_payment_metadata));
    }
    if (m_payor_payment_id_isSet) {
        obj.insert(QString("payorPaymentId"), ::OpenAPI::toJsonValue(m_payor_payment_id));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_reason_code_isSet) {
        obj.insert(QString("reasonCode"), ::OpenAPI::toJsonValue(m_reason_code));
    }
    if (m_remote_id_isSet) {
        obj.insert(QString("remoteId"), ::OpenAPI::toJsonValue(m_remote_id));
    }
    if (m_remote_system_id_isSet) {
        obj.insert(QString("remoteSystemId"), ::OpenAPI::toJsonValue(m_remote_system_id));
    }
    if (m_source_account_name_isSet) {
        obj.insert(QString("sourceAccountName"), ::OpenAPI::toJsonValue(m_source_account_name));
    }
    return obj;
}

qint32 OAIRejectedPaymentV3::getAmount() const {
    return m_amount;
}
void OAIRejectedPaymentV3::setAmount(const qint32 &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIRejectedPaymentV3::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIRejectedPaymentV3::is_amount_Valid() const{
    return m_amount_isValid;
}

QString OAIRejectedPaymentV3::getCurrencyType() const {
    return m_currency_type;
}
void OAIRejectedPaymentV3::setCurrencyType(const QString &currency_type) {
    m_currency_type = currency_type;
    m_currency_type_isSet = true;
}

bool OAIRejectedPaymentV3::is_currency_type_Set() const{
    return m_currency_type_isSet;
}

bool OAIRejectedPaymentV3::is_currency_type_Valid() const{
    return m_currency_type_isValid;
}

qint32 OAIRejectedPaymentV3::getLineNumber() const {
    return m_line_number;
}
void OAIRejectedPaymentV3::setLineNumber(const qint32 &line_number) {
    m_line_number = line_number;
    m_line_number_isSet = true;
}

bool OAIRejectedPaymentV3::is_line_number_Set() const{
    return m_line_number_isSet;
}

bool OAIRejectedPaymentV3::is_line_number_Valid() const{
    return m_line_number_isValid;
}

QString OAIRejectedPaymentV3::getMessage() const {
    return m_message;
}
void OAIRejectedPaymentV3::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIRejectedPaymentV3::is_message_Set() const{
    return m_message_isSet;
}

bool OAIRejectedPaymentV3::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIRejectedPaymentV3::getPaymentMetadata() const {
    return m_payment_metadata;
}
void OAIRejectedPaymentV3::setPaymentMetadata(const QString &payment_metadata) {
    m_payment_metadata = payment_metadata;
    m_payment_metadata_isSet = true;
}

bool OAIRejectedPaymentV3::is_payment_metadata_Set() const{
    return m_payment_metadata_isSet;
}

bool OAIRejectedPaymentV3::is_payment_metadata_Valid() const{
    return m_payment_metadata_isValid;
}

QString OAIRejectedPaymentV3::getPayorPaymentId() const {
    return m_payor_payment_id;
}
void OAIRejectedPaymentV3::setPayorPaymentId(const QString &payor_payment_id) {
    m_payor_payment_id = payor_payment_id;
    m_payor_payment_id_isSet = true;
}

bool OAIRejectedPaymentV3::is_payor_payment_id_Set() const{
    return m_payor_payment_id_isSet;
}

bool OAIRejectedPaymentV3::is_payor_payment_id_Valid() const{
    return m_payor_payment_id_isValid;
}

QString OAIRejectedPaymentV3::getReason() const {
    return m_reason;
}
void OAIRejectedPaymentV3::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIRejectedPaymentV3::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIRejectedPaymentV3::is_reason_Valid() const{
    return m_reason_isValid;
}

QString OAIRejectedPaymentV3::getReasonCode() const {
    return m_reason_code;
}
void OAIRejectedPaymentV3::setReasonCode(const QString &reason_code) {
    m_reason_code = reason_code;
    m_reason_code_isSet = true;
}

bool OAIRejectedPaymentV3::is_reason_code_Set() const{
    return m_reason_code_isSet;
}

bool OAIRejectedPaymentV3::is_reason_code_Valid() const{
    return m_reason_code_isValid;
}

QString OAIRejectedPaymentV3::getRemoteId() const {
    return m_remote_id;
}
void OAIRejectedPaymentV3::setRemoteId(const QString &remote_id) {
    m_remote_id = remote_id;
    m_remote_id_isSet = true;
}

bool OAIRejectedPaymentV3::is_remote_id_Set() const{
    return m_remote_id_isSet;
}

bool OAIRejectedPaymentV3::is_remote_id_Valid() const{
    return m_remote_id_isValid;
}

QString OAIRejectedPaymentV3::getRemoteSystemId() const {
    return m_remote_system_id;
}
void OAIRejectedPaymentV3::setRemoteSystemId(const QString &remote_system_id) {
    m_remote_system_id = remote_system_id;
    m_remote_system_id_isSet = true;
}

bool OAIRejectedPaymentV3::is_remote_system_id_Set() const{
    return m_remote_system_id_isSet;
}

bool OAIRejectedPaymentV3::is_remote_system_id_Valid() const{
    return m_remote_system_id_isValid;
}

QString OAIRejectedPaymentV3::getSourceAccountName() const {
    return m_source_account_name;
}
void OAIRejectedPaymentV3::setSourceAccountName(const QString &source_account_name) {
    m_source_account_name = source_account_name;
    m_source_account_name_isSet = true;
}

bool OAIRejectedPaymentV3::is_source_account_name_Set() const{
    return m_source_account_name_isSet;
}

bool OAIRejectedPaymentV3::is_source_account_name_Valid() const{
    return m_source_account_name_isValid;
}

bool OAIRejectedPaymentV3::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_metadata_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payor_payment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_remote_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_remote_system_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_account_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRejectedPaymentV3::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_amount_isValid && m_currency_type_isValid && m_payor_payment_id_isValid && m_reason_isValid && m_remote_id_isValid && m_source_account_name_isValid && true;
}

} // namespace OpenAPI
