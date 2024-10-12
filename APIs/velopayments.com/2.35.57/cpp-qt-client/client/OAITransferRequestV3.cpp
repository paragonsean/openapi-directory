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

#include "OAITransferRequestV3.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITransferRequestV3::OAITransferRequestV3(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITransferRequestV3::OAITransferRequestV3() {
    this->initializeModel();
}

OAITransferRequestV3::~OAITransferRequestV3() {}

void OAITransferRequestV3::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_to_source_account_id_isSet = false;
    m_to_source_account_id_isValid = false;
}

void OAITransferRequestV3::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITransferRequestV3::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_to_source_account_id_isValid = ::OpenAPI::fromJsonValue(m_to_source_account_id, json[QString("toSourceAccountId")]);
    m_to_source_account_id_isSet = !json[QString("toSourceAccountId")].isNull() && m_to_source_account_id_isValid;
}

QString OAITransferRequestV3::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITransferRequestV3::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_to_source_account_id_isSet) {
        obj.insert(QString("toSourceAccountId"), ::OpenAPI::toJsonValue(m_to_source_account_id));
    }
    return obj;
}

qint64 OAITransferRequestV3::getAmount() const {
    return m_amount;
}
void OAITransferRequestV3::setAmount(const qint64 &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAITransferRequestV3::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAITransferRequestV3::is_amount_Valid() const{
    return m_amount_isValid;
}

QString OAITransferRequestV3::getCurrency() const {
    return m_currency;
}
void OAITransferRequestV3::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAITransferRequestV3::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAITransferRequestV3::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAITransferRequestV3::getToSourceAccountId() const {
    return m_to_source_account_id;
}
void OAITransferRequestV3::setToSourceAccountId(const QString &to_source_account_id) {
    m_to_source_account_id = to_source_account_id;
    m_to_source_account_id_isSet = true;
}

bool OAITransferRequestV3::is_to_source_account_id_Set() const{
    return m_to_source_account_id_isSet;
}

bool OAITransferRequestV3::is_to_source_account_id_Valid() const{
    return m_to_source_account_id_isValid;
}

bool OAITransferRequestV3::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_to_source_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITransferRequestV3::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_amount_isValid && m_currency_isValid && m_to_source_account_id_isValid && true;
}

} // namespace OpenAPI
