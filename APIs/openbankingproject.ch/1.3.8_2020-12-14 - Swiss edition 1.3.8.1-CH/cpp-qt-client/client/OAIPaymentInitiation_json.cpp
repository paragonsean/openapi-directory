/**
 * Swiss NextGen Banking API-Framework
 * # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples.  The possible Approaches are:   * Redirect SCA Approach   * *(Not recommended by obp.ch community) OAuth SCA Approach*   * *(Not recommended by obp.ch community) Decoupled SCA Approach*   * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method*   * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available*   * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method*    Not every message defined in this API definition is necessary for all approaches.   Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional   Therefore for a particular implementation of a compliant API it is only necessary to support   a certain subset of the methods defined in this API definition.    **Please have a look at the implementation guidelines if you are not sure   which message has to be used for the approach you are going to use.**  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).**   It is not a replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]      \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"    The element \"Accept\" will not be defined in this file at any place.    The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".  * There are several predefined types which might occur in payment initiation messages,   but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which needs these fields, one can easily use the predefined types.   But the ASPSP need not to accept them in general.  * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)   except they are mentioned in the Implementation Guidelines.**   Therefore the implementer might add these in his own realisation of a comlient API in addition to the elements defined in this file.  ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  Space 
 *
 * The version of the OpenAPI document: 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 * Contact: info@obp.ch
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPaymentInitiation_json.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaymentInitiation_json::OAIPaymentInitiation_json(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaymentInitiation_json::OAIPaymentInitiation_json() {
    this->initializeModel();
}

OAIPaymentInitiation_json::~OAIPaymentInitiation_json() {}

void OAIPaymentInitiation_json::initializeModel() {

    m_charge_bearer_isSet = false;
    m_charge_bearer_isValid = false;

    m_creditor_account_isSet = false;
    m_creditor_account_isValid = false;

    m_creditor_address_isSet = false;
    m_creditor_address_isValid = false;

    m_creditor_agent_isSet = false;
    m_creditor_agent_isValid = false;

    m_creditor_agent_name_isSet = false;
    m_creditor_agent_name_isValid = false;

    m_creditor_id_isSet = false;
    m_creditor_id_isValid = false;

    m_creditor_name_isSet = false;
    m_creditor_name_isValid = false;

    m_creditor_name_and_address_isSet = false;
    m_creditor_name_and_address_isValid = false;

    m_debtor_account_isSet = false;
    m_debtor_account_isValid = false;

    m_debtor_agent_isSet = false;
    m_debtor_agent_isValid = false;

    m_debtor_id_isSet = false;
    m_debtor_id_isValid = false;

    m_debtor_name_isSet = false;
    m_debtor_name_isValid = false;

    m_end_to_end_identification_isSet = false;
    m_end_to_end_identification_isValid = false;

    m_equivalent_amount_isSet = false;
    m_equivalent_amount_isValid = false;

    m_exchange_rate_information_isSet = false;
    m_exchange_rate_information_isValid = false;

    m_instructed_amount_isSet = false;
    m_instructed_amount_isValid = false;

    m_intermediary_agent_isSet = false;
    m_intermediary_agent_isValid = false;

    m_purpose_code_isSet = false;
    m_purpose_code_isValid = false;

    m_remittance_information_structured_isSet = false;
    m_remittance_information_structured_isValid = false;

    m_remittance_information_unstructured_isSet = false;
    m_remittance_information_unstructured_isValid = false;

    m_requested_execution_date_isSet = false;
    m_requested_execution_date_isValid = false;

    m_service_level_isSet = false;
    m_service_level_isValid = false;

    m_transaction_currency_isSet = false;
    m_transaction_currency_isValid = false;

    m_ultimate_creditor_isSet = false;
    m_ultimate_creditor_isValid = false;

    m_ultimate_debtor_isSet = false;
    m_ultimate_debtor_isValid = false;
}

void OAIPaymentInitiation_json::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPaymentInitiation_json::fromJsonObject(QJsonObject json) {

    m_charge_bearer_isValid = ::OpenAPI::fromJsonValue(m_charge_bearer, json[QString("chargeBearer")]);
    m_charge_bearer_isSet = !json[QString("chargeBearer")].isNull() && m_charge_bearer_isValid;

    m_creditor_account_isValid = ::OpenAPI::fromJsonValue(m_creditor_account, json[QString("creditorAccount")]);
    m_creditor_account_isSet = !json[QString("creditorAccount")].isNull() && m_creditor_account_isValid;

    m_creditor_address_isValid = ::OpenAPI::fromJsonValue(m_creditor_address, json[QString("creditorAddress")]);
    m_creditor_address_isSet = !json[QString("creditorAddress")].isNull() && m_creditor_address_isValid;

    m_creditor_agent_isValid = ::OpenAPI::fromJsonValue(m_creditor_agent, json[QString("creditorAgent")]);
    m_creditor_agent_isSet = !json[QString("creditorAgent")].isNull() && m_creditor_agent_isValid;

    m_creditor_agent_name_isValid = ::OpenAPI::fromJsonValue(m_creditor_agent_name, json[QString("creditorAgentName")]);
    m_creditor_agent_name_isSet = !json[QString("creditorAgentName")].isNull() && m_creditor_agent_name_isValid;

    m_creditor_id_isValid = ::OpenAPI::fromJsonValue(m_creditor_id, json[QString("creditorId")]);
    m_creditor_id_isSet = !json[QString("creditorId")].isNull() && m_creditor_id_isValid;

    m_creditor_name_isValid = ::OpenAPI::fromJsonValue(m_creditor_name, json[QString("creditorName")]);
    m_creditor_name_isSet = !json[QString("creditorName")].isNull() && m_creditor_name_isValid;

    m_creditor_name_and_address_isValid = ::OpenAPI::fromJsonValue(m_creditor_name_and_address, json[QString("creditorNameAndAddress")]);
    m_creditor_name_and_address_isSet = !json[QString("creditorNameAndAddress")].isNull() && m_creditor_name_and_address_isValid;

    m_debtor_account_isValid = ::OpenAPI::fromJsonValue(m_debtor_account, json[QString("debtorAccount")]);
    m_debtor_account_isSet = !json[QString("debtorAccount")].isNull() && m_debtor_account_isValid;

    m_debtor_agent_isValid = ::OpenAPI::fromJsonValue(m_debtor_agent, json[QString("debtorAgent")]);
    m_debtor_agent_isSet = !json[QString("debtorAgent")].isNull() && m_debtor_agent_isValid;

    m_debtor_id_isValid = ::OpenAPI::fromJsonValue(m_debtor_id, json[QString("debtorId")]);
    m_debtor_id_isSet = !json[QString("debtorId")].isNull() && m_debtor_id_isValid;

    m_debtor_name_isValid = ::OpenAPI::fromJsonValue(m_debtor_name, json[QString("debtorName")]);
    m_debtor_name_isSet = !json[QString("debtorName")].isNull() && m_debtor_name_isValid;

    m_end_to_end_identification_isValid = ::OpenAPI::fromJsonValue(m_end_to_end_identification, json[QString("endToEndIdentification")]);
    m_end_to_end_identification_isSet = !json[QString("endToEndIdentification")].isNull() && m_end_to_end_identification_isValid;

    m_equivalent_amount_isValid = ::OpenAPI::fromJsonValue(m_equivalent_amount, json[QString("equivalentAmount")]);
    m_equivalent_amount_isSet = !json[QString("equivalentAmount")].isNull() && m_equivalent_amount_isValid;

    m_exchange_rate_information_isValid = ::OpenAPI::fromJsonValue(m_exchange_rate_information, json[QString("exchangeRateInformation")]);
    m_exchange_rate_information_isSet = !json[QString("exchangeRateInformation")].isNull() && m_exchange_rate_information_isValid;

    m_instructed_amount_isValid = ::OpenAPI::fromJsonValue(m_instructed_amount, json[QString("instructedAmount")]);
    m_instructed_amount_isSet = !json[QString("instructedAmount")].isNull() && m_instructed_amount_isValid;

    m_intermediary_agent_isValid = ::OpenAPI::fromJsonValue(m_intermediary_agent, json[QString("intermediaryAgent")]);
    m_intermediary_agent_isSet = !json[QString("intermediaryAgent")].isNull() && m_intermediary_agent_isValid;

    m_purpose_code_isValid = ::OpenAPI::fromJsonValue(m_purpose_code, json[QString("purposeCode")]);
    m_purpose_code_isSet = !json[QString("purposeCode")].isNull() && m_purpose_code_isValid;

    m_remittance_information_structured_isValid = ::OpenAPI::fromJsonValue(m_remittance_information_structured, json[QString("remittanceInformationStructured")]);
    m_remittance_information_structured_isSet = !json[QString("remittanceInformationStructured")].isNull() && m_remittance_information_structured_isValid;

    m_remittance_information_unstructured_isValid = ::OpenAPI::fromJsonValue(m_remittance_information_unstructured, json[QString("remittanceInformationUnstructured")]);
    m_remittance_information_unstructured_isSet = !json[QString("remittanceInformationUnstructured")].isNull() && m_remittance_information_unstructured_isValid;

    m_requested_execution_date_isValid = ::OpenAPI::fromJsonValue(m_requested_execution_date, json[QString("requestedExecutionDate")]);
    m_requested_execution_date_isSet = !json[QString("requestedExecutionDate")].isNull() && m_requested_execution_date_isValid;

    m_service_level_isValid = ::OpenAPI::fromJsonValue(m_service_level, json[QString("serviceLevel")]);
    m_service_level_isSet = !json[QString("serviceLevel")].isNull() && m_service_level_isValid;

    m_transaction_currency_isValid = ::OpenAPI::fromJsonValue(m_transaction_currency, json[QString("transactionCurrency")]);
    m_transaction_currency_isSet = !json[QString("transactionCurrency")].isNull() && m_transaction_currency_isValid;

    m_ultimate_creditor_isValid = ::OpenAPI::fromJsonValue(m_ultimate_creditor, json[QString("ultimateCreditor")]);
    m_ultimate_creditor_isSet = !json[QString("ultimateCreditor")].isNull() && m_ultimate_creditor_isValid;

    m_ultimate_debtor_isValid = ::OpenAPI::fromJsonValue(m_ultimate_debtor, json[QString("ultimateDebtor")]);
    m_ultimate_debtor_isSet = !json[QString("ultimateDebtor")].isNull() && m_ultimate_debtor_isValid;
}

QString OAIPaymentInitiation_json::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPaymentInitiation_json::asJsonObject() const {
    QJsonObject obj;
    if (m_charge_bearer.isSet()) {
        obj.insert(QString("chargeBearer"), ::OpenAPI::toJsonValue(m_charge_bearer));
    }
    if (m_creditor_account.isSet()) {
        obj.insert(QString("creditorAccount"), ::OpenAPI::toJsonValue(m_creditor_account));
    }
    if (m_creditor_address.isSet()) {
        obj.insert(QString("creditorAddress"), ::OpenAPI::toJsonValue(m_creditor_address));
    }
    if (m_creditor_agent.isSet()) {
        obj.insert(QString("creditorAgent"), ::OpenAPI::toJsonValue(m_creditor_agent));
    }
    if (m_creditor_agent_name_isSet) {
        obj.insert(QString("creditorAgentName"), ::OpenAPI::toJsonValue(m_creditor_agent_name));
    }
    if (m_creditor_id_isSet) {
        obj.insert(QString("creditorId"), ::OpenAPI::toJsonValue(m_creditor_id));
    }
    if (m_creditor_name_isSet) {
        obj.insert(QString("creditorName"), ::OpenAPI::toJsonValue(m_creditor_name));
    }
    if (m_creditor_name_and_address_isSet) {
        obj.insert(QString("creditorNameAndAddress"), ::OpenAPI::toJsonValue(m_creditor_name_and_address));
    }
    if (m_debtor_account.isSet()) {
        obj.insert(QString("debtorAccount"), ::OpenAPI::toJsonValue(m_debtor_account));
    }
    if (m_debtor_agent.isSet()) {
        obj.insert(QString("debtorAgent"), ::OpenAPI::toJsonValue(m_debtor_agent));
    }
    if (m_debtor_id_isSet) {
        obj.insert(QString("debtorId"), ::OpenAPI::toJsonValue(m_debtor_id));
    }
    if (m_debtor_name_isSet) {
        obj.insert(QString("debtorName"), ::OpenAPI::toJsonValue(m_debtor_name));
    }
    if (m_end_to_end_identification_isSet) {
        obj.insert(QString("endToEndIdentification"), ::OpenAPI::toJsonValue(m_end_to_end_identification));
    }
    if (m_equivalent_amount.isSet()) {
        obj.insert(QString("equivalentAmount"), ::OpenAPI::toJsonValue(m_equivalent_amount));
    }
    if (m_exchange_rate_information.isSet()) {
        obj.insert(QString("exchangeRateInformation"), ::OpenAPI::toJsonValue(m_exchange_rate_information));
    }
    if (m_instructed_amount.isSet()) {
        obj.insert(QString("instructedAmount"), ::OpenAPI::toJsonValue(m_instructed_amount));
    }
    if (m_intermediary_agent_isSet) {
        obj.insert(QString("intermediaryAgent"), ::OpenAPI::toJsonValue(m_intermediary_agent));
    }
    if (m_purpose_code.isSet()) {
        obj.insert(QString("purposeCode"), ::OpenAPI::toJsonValue(m_purpose_code));
    }
    if (m_remittance_information_structured.isSet()) {
        obj.insert(QString("remittanceInformationStructured"), ::OpenAPI::toJsonValue(m_remittance_information_structured));
    }
    if (m_remittance_information_unstructured_isSet) {
        obj.insert(QString("remittanceInformationUnstructured"), ::OpenAPI::toJsonValue(m_remittance_information_unstructured));
    }
    if (m_requested_execution_date_isSet) {
        obj.insert(QString("requestedExecutionDate"), ::OpenAPI::toJsonValue(m_requested_execution_date));
    }
    if (m_service_level.isSet()) {
        obj.insert(QString("serviceLevel"), ::OpenAPI::toJsonValue(m_service_level));
    }
    if (m_transaction_currency_isSet) {
        obj.insert(QString("transactionCurrency"), ::OpenAPI::toJsonValue(m_transaction_currency));
    }
    if (m_ultimate_creditor_isSet) {
        obj.insert(QString("ultimateCreditor"), ::OpenAPI::toJsonValue(m_ultimate_creditor));
    }
    if (m_ultimate_debtor_isSet) {
        obj.insert(QString("ultimateDebtor"), ::OpenAPI::toJsonValue(m_ultimate_debtor));
    }
    return obj;
}

OAIChargeBearer OAIPaymentInitiation_json::getChargeBearer() const {
    return m_charge_bearer;
}
void OAIPaymentInitiation_json::setChargeBearer(const OAIChargeBearer &charge_bearer) {
    m_charge_bearer = charge_bearer;
    m_charge_bearer_isSet = true;
}

bool OAIPaymentInitiation_json::is_charge_bearer_Set() const{
    return m_charge_bearer_isSet;
}

bool OAIPaymentInitiation_json::is_charge_bearer_Valid() const{
    return m_charge_bearer_isValid;
}

OAIAccountReference16_CH OAIPaymentInitiation_json::getCreditorAccount() const {
    return m_creditor_account;
}
void OAIPaymentInitiation_json::setCreditorAccount(const OAIAccountReference16_CH &creditor_account) {
    m_creditor_account = creditor_account;
    m_creditor_account_isSet = true;
}

bool OAIPaymentInitiation_json::is_creditor_account_Set() const{
    return m_creditor_account_isSet;
}

bool OAIPaymentInitiation_json::is_creditor_account_Valid() const{
    return m_creditor_account_isValid;
}

OAIAddress OAIPaymentInitiation_json::getCreditorAddress() const {
    return m_creditor_address;
}
void OAIPaymentInitiation_json::setCreditorAddress(const OAIAddress &creditor_address) {
    m_creditor_address = creditor_address;
    m_creditor_address_isSet = true;
}

bool OAIPaymentInitiation_json::is_creditor_address_Set() const{
    return m_creditor_address_isSet;
}

bool OAIPaymentInitiation_json::is_creditor_address_Valid() const{
    return m_creditor_address_isValid;
}

OAICreditorAgent7_CH OAIPaymentInitiation_json::getCreditorAgent() const {
    return m_creditor_agent;
}
void OAIPaymentInitiation_json::setCreditorAgent(const OAICreditorAgent7_CH &creditor_agent) {
    m_creditor_agent = creditor_agent;
    m_creditor_agent_isSet = true;
}

bool OAIPaymentInitiation_json::is_creditor_agent_Set() const{
    return m_creditor_agent_isSet;
}

bool OAIPaymentInitiation_json::is_creditor_agent_Valid() const{
    return m_creditor_agent_isValid;
}

QString OAIPaymentInitiation_json::getCreditorAgentName() const {
    return m_creditor_agent_name;
}
void OAIPaymentInitiation_json::setCreditorAgentName(const QString &creditor_agent_name) {
    m_creditor_agent_name = creditor_agent_name;
    m_creditor_agent_name_isSet = true;
}

bool OAIPaymentInitiation_json::is_creditor_agent_name_Set() const{
    return m_creditor_agent_name_isSet;
}

bool OAIPaymentInitiation_json::is_creditor_agent_name_Valid() const{
    return m_creditor_agent_name_isValid;
}

QString OAIPaymentInitiation_json::getCreditorId() const {
    return m_creditor_id;
}
void OAIPaymentInitiation_json::setCreditorId(const QString &creditor_id) {
    m_creditor_id = creditor_id;
    m_creditor_id_isSet = true;
}

bool OAIPaymentInitiation_json::is_creditor_id_Set() const{
    return m_creditor_id_isSet;
}

bool OAIPaymentInitiation_json::is_creditor_id_Valid() const{
    return m_creditor_id_isValid;
}

QString OAIPaymentInitiation_json::getCreditorName() const {
    return m_creditor_name;
}
void OAIPaymentInitiation_json::setCreditorName(const QString &creditor_name) {
    m_creditor_name = creditor_name;
    m_creditor_name_isSet = true;
}

bool OAIPaymentInitiation_json::is_creditor_name_Set() const{
    return m_creditor_name_isSet;
}

bool OAIPaymentInitiation_json::is_creditor_name_Valid() const{
    return m_creditor_name_isValid;
}

QString OAIPaymentInitiation_json::getCreditorNameAndAddress() const {
    return m_creditor_name_and_address;
}
void OAIPaymentInitiation_json::setCreditorNameAndAddress(const QString &creditor_name_and_address) {
    m_creditor_name_and_address = creditor_name_and_address;
    m_creditor_name_and_address_isSet = true;
}

bool OAIPaymentInitiation_json::is_creditor_name_and_address_Set() const{
    return m_creditor_name_and_address_isSet;
}

bool OAIPaymentInitiation_json::is_creditor_name_and_address_Valid() const{
    return m_creditor_name_and_address_isValid;
}

OAIAccountReference16_CH OAIPaymentInitiation_json::getDebtorAccount() const {
    return m_debtor_account;
}
void OAIPaymentInitiation_json::setDebtorAccount(const OAIAccountReference16_CH &debtor_account) {
    m_debtor_account = debtor_account;
    m_debtor_account_isSet = true;
}

bool OAIPaymentInitiation_json::is_debtor_account_Set() const{
    return m_debtor_account_isSet;
}

bool OAIPaymentInitiation_json::is_debtor_account_Valid() const{
    return m_debtor_account_isValid;
}

OAIDebtorAgent7_CH OAIPaymentInitiation_json::getDebtorAgent() const {
    return m_debtor_agent;
}
void OAIPaymentInitiation_json::setDebtorAgent(const OAIDebtorAgent7_CH &debtor_agent) {
    m_debtor_agent = debtor_agent;
    m_debtor_agent_isSet = true;
}

bool OAIPaymentInitiation_json::is_debtor_agent_Set() const{
    return m_debtor_agent_isSet;
}

bool OAIPaymentInitiation_json::is_debtor_agent_Valid() const{
    return m_debtor_agent_isValid;
}

QString OAIPaymentInitiation_json::getDebtorId() const {
    return m_debtor_id;
}
void OAIPaymentInitiation_json::setDebtorId(const QString &debtor_id) {
    m_debtor_id = debtor_id;
    m_debtor_id_isSet = true;
}

bool OAIPaymentInitiation_json::is_debtor_id_Set() const{
    return m_debtor_id_isSet;
}

bool OAIPaymentInitiation_json::is_debtor_id_Valid() const{
    return m_debtor_id_isValid;
}

QString OAIPaymentInitiation_json::getDebtorName() const {
    return m_debtor_name;
}
void OAIPaymentInitiation_json::setDebtorName(const QString &debtor_name) {
    m_debtor_name = debtor_name;
    m_debtor_name_isSet = true;
}

bool OAIPaymentInitiation_json::is_debtor_name_Set() const{
    return m_debtor_name_isSet;
}

bool OAIPaymentInitiation_json::is_debtor_name_Valid() const{
    return m_debtor_name_isValid;
}

QString OAIPaymentInitiation_json::getEndToEndIdentification() const {
    return m_end_to_end_identification;
}
void OAIPaymentInitiation_json::setEndToEndIdentification(const QString &end_to_end_identification) {
    m_end_to_end_identification = end_to_end_identification;
    m_end_to_end_identification_isSet = true;
}

bool OAIPaymentInitiation_json::is_end_to_end_identification_Set() const{
    return m_end_to_end_identification_isSet;
}

bool OAIPaymentInitiation_json::is_end_to_end_identification_Valid() const{
    return m_end_to_end_identification_isValid;
}

OAIAmount OAIPaymentInitiation_json::getEquivalentAmount() const {
    return m_equivalent_amount;
}
void OAIPaymentInitiation_json::setEquivalentAmount(const OAIAmount &equivalent_amount) {
    m_equivalent_amount = equivalent_amount;
    m_equivalent_amount_isSet = true;
}

bool OAIPaymentInitiation_json::is_equivalent_amount_Set() const{
    return m_equivalent_amount_isSet;
}

bool OAIPaymentInitiation_json::is_equivalent_amount_Valid() const{
    return m_equivalent_amount_isValid;
}

OAIExchangeRateInformation1 OAIPaymentInitiation_json::getExchangeRateInformation() const {
    return m_exchange_rate_information;
}
void OAIPaymentInitiation_json::setExchangeRateInformation(const OAIExchangeRateInformation1 &exchange_rate_information) {
    m_exchange_rate_information = exchange_rate_information;
    m_exchange_rate_information_isSet = true;
}

bool OAIPaymentInitiation_json::is_exchange_rate_information_Set() const{
    return m_exchange_rate_information_isSet;
}

bool OAIPaymentInitiation_json::is_exchange_rate_information_Valid() const{
    return m_exchange_rate_information_isValid;
}

OAIAmount OAIPaymentInitiation_json::getInstructedAmount() const {
    return m_instructed_amount;
}
void OAIPaymentInitiation_json::setInstructedAmount(const OAIAmount &instructed_amount) {
    m_instructed_amount = instructed_amount;
    m_instructed_amount_isSet = true;
}

bool OAIPaymentInitiation_json::is_instructed_amount_Set() const{
    return m_instructed_amount_isSet;
}

bool OAIPaymentInitiation_json::is_instructed_amount_Valid() const{
    return m_instructed_amount_isValid;
}

QString OAIPaymentInitiation_json::getIntermediaryAgent() const {
    return m_intermediary_agent;
}
void OAIPaymentInitiation_json::setIntermediaryAgent(const QString &intermediary_agent) {
    m_intermediary_agent = intermediary_agent;
    m_intermediary_agent_isSet = true;
}

bool OAIPaymentInitiation_json::is_intermediary_agent_Set() const{
    return m_intermediary_agent_isSet;
}

bool OAIPaymentInitiation_json::is_intermediary_agent_Valid() const{
    return m_intermediary_agent_isValid;
}

OAIPurposeCode OAIPaymentInitiation_json::getPurposeCode() const {
    return m_purpose_code;
}
void OAIPaymentInitiation_json::setPurposeCode(const OAIPurposeCode &purpose_code) {
    m_purpose_code = purpose_code;
    m_purpose_code_isSet = true;
}

bool OAIPaymentInitiation_json::is_purpose_code_Set() const{
    return m_purpose_code_isSet;
}

bool OAIPaymentInitiation_json::is_purpose_code_Valid() const{
    return m_purpose_code_isValid;
}

OAIRemittanceInformationStructured OAIPaymentInitiation_json::getRemittanceInformationStructured() const {
    return m_remittance_information_structured;
}
void OAIPaymentInitiation_json::setRemittanceInformationStructured(const OAIRemittanceInformationStructured &remittance_information_structured) {
    m_remittance_information_structured = remittance_information_structured;
    m_remittance_information_structured_isSet = true;
}

bool OAIPaymentInitiation_json::is_remittance_information_structured_Set() const{
    return m_remittance_information_structured_isSet;
}

bool OAIPaymentInitiation_json::is_remittance_information_structured_Valid() const{
    return m_remittance_information_structured_isValid;
}

QString OAIPaymentInitiation_json::getRemittanceInformationUnstructured() const {
    return m_remittance_information_unstructured;
}
void OAIPaymentInitiation_json::setRemittanceInformationUnstructured(const QString &remittance_information_unstructured) {
    m_remittance_information_unstructured = remittance_information_unstructured;
    m_remittance_information_unstructured_isSet = true;
}

bool OAIPaymentInitiation_json::is_remittance_information_unstructured_Set() const{
    return m_remittance_information_unstructured_isSet;
}

bool OAIPaymentInitiation_json::is_remittance_information_unstructured_Valid() const{
    return m_remittance_information_unstructured_isValid;
}

QDate OAIPaymentInitiation_json::getRequestedExecutionDate() const {
    return m_requested_execution_date;
}
void OAIPaymentInitiation_json::setRequestedExecutionDate(const QDate &requested_execution_date) {
    m_requested_execution_date = requested_execution_date;
    m_requested_execution_date_isSet = true;
}

bool OAIPaymentInitiation_json::is_requested_execution_date_Set() const{
    return m_requested_execution_date_isSet;
}

bool OAIPaymentInitiation_json::is_requested_execution_date_Valid() const{
    return m_requested_execution_date_isValid;
}

OAIExternalServiceLevel1Code OAIPaymentInitiation_json::getServiceLevel() const {
    return m_service_level;
}
void OAIPaymentInitiation_json::setServiceLevel(const OAIExternalServiceLevel1Code &service_level) {
    m_service_level = service_level;
    m_service_level_isSet = true;
}

bool OAIPaymentInitiation_json::is_service_level_Set() const{
    return m_service_level_isSet;
}

bool OAIPaymentInitiation_json::is_service_level_Valid() const{
    return m_service_level_isValid;
}

QString OAIPaymentInitiation_json::getTransactionCurrency() const {
    return m_transaction_currency;
}
void OAIPaymentInitiation_json::setTransactionCurrency(const QString &transaction_currency) {
    m_transaction_currency = transaction_currency;
    m_transaction_currency_isSet = true;
}

bool OAIPaymentInitiation_json::is_transaction_currency_Set() const{
    return m_transaction_currency_isSet;
}

bool OAIPaymentInitiation_json::is_transaction_currency_Valid() const{
    return m_transaction_currency_isValid;
}

QString OAIPaymentInitiation_json::getUltimateCreditor() const {
    return m_ultimate_creditor;
}
void OAIPaymentInitiation_json::setUltimateCreditor(const QString &ultimate_creditor) {
    m_ultimate_creditor = ultimate_creditor;
    m_ultimate_creditor_isSet = true;
}

bool OAIPaymentInitiation_json::is_ultimate_creditor_Set() const{
    return m_ultimate_creditor_isSet;
}

bool OAIPaymentInitiation_json::is_ultimate_creditor_Valid() const{
    return m_ultimate_creditor_isValid;
}

QString OAIPaymentInitiation_json::getUltimateDebtor() const {
    return m_ultimate_debtor;
}
void OAIPaymentInitiation_json::setUltimateDebtor(const QString &ultimate_debtor) {
    m_ultimate_debtor = ultimate_debtor;
    m_ultimate_debtor_isSet = true;
}

bool OAIPaymentInitiation_json::is_ultimate_debtor_Set() const{
    return m_ultimate_debtor_isSet;
}

bool OAIPaymentInitiation_json::is_ultimate_debtor_Valid() const{
    return m_ultimate_debtor_isValid;
}

bool OAIPaymentInitiation_json::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_charge_bearer.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_creditor_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_creditor_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_creditor_agent.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_creditor_agent_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creditor_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creditor_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creditor_name_and_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_debtor_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_debtor_agent.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_debtor_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_debtor_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_to_end_identification_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_equivalent_amount.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_exchange_rate_information.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_instructed_amount.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_intermediary_agent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_purpose_code.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_remittance_information_structured.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_remittance_information_unstructured_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_requested_execution_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_level.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ultimate_creditor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ultimate_debtor_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPaymentInitiation_json::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_creditor_account_isValid && m_creditor_name_isValid && m_debtor_account_isValid && m_debtor_name_isValid && m_end_to_end_identification_isValid && m_requested_execution_date_isValid && true;
}

} // namespace OpenAPI
