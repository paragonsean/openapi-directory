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

#include "OAIPayorV2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPayorV2::OAIPayorV2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPayorV2::OAIPayorV2() {
    this->initializeModel();
}

OAIPayorV2::~OAIPayorV2() {}

void OAIPayorV2::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_allows_language_choice_isSet = false;
    m_allows_language_choice_isValid = false;

    m_collective_alias_isSet = false;
    m_collective_alias_isValid = false;

    m_dba_name_isSet = false;
    m_dba_name_isValid = false;

    m_includes_reports_isSet = false;
    m_includes_reports_isValid = false;

    m_kyc_state_isSet = false;
    m_kyc_state_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_managing_payees_isSet = false;
    m_managing_payees_isValid = false;

    m_manual_lockout_isSet = false;
    m_manual_lockout_isValid = false;

    m_max_master_payor_admins_isSet = false;
    m_max_master_payor_admins_isValid = false;

    m_open_banking_enabled_isSet = false;
    m_open_banking_enabled_isValid = false;

    m_payee_grace_period_days_isSet = false;
    m_payee_grace_period_days_isValid = false;

    m_payee_grace_period_processing_enabled_isSet = false;
    m_payee_grace_period_processing_enabled_isValid = false;

    m_payment_rails_isSet = false;
    m_payment_rails_isValid = false;

    m_payor_id_isSet = false;
    m_payor_id_isValid = false;

    m_payor_name_isSet = false;
    m_payor_name_isValid = false;

    m_payor_xid_isSet = false;
    m_payor_xid_isValid = false;

    m_primary_contact_email_isSet = false;
    m_primary_contact_email_isValid = false;

    m_primary_contact_name_isSet = false;
    m_primary_contact_name_isValid = false;

    m_primary_contact_phone_isSet = false;
    m_primary_contact_phone_isValid = false;

    m_provider_isSet = false;
    m_provider_isValid = false;

    m_reminder_emails_opt_out_isSet = false;
    m_reminder_emails_opt_out_isValid = false;

    m_remote_system_ids_isSet = false;
    m_remote_system_ids_isValid = false;

    m_support_contact_isSet = false;
    m_support_contact_isValid = false;

    m_transmission_types_isSet = false;
    m_transmission_types_isValid = false;

    m_usd_txn_value_reporting_threshold_isSet = false;
    m_usd_txn_value_reporting_threshold_isValid = false;

    m_wu_customer_id_isSet = false;
    m_wu_customer_id_isValid = false;
}

void OAIPayorV2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPayorV2::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_allows_language_choice_isValid = ::OpenAPI::fromJsonValue(m_allows_language_choice, json[QString("allowsLanguageChoice")]);
    m_allows_language_choice_isSet = !json[QString("allowsLanguageChoice")].isNull() && m_allows_language_choice_isValid;

    m_collective_alias_isValid = ::OpenAPI::fromJsonValue(m_collective_alias, json[QString("collectiveAlias")]);
    m_collective_alias_isSet = !json[QString("collectiveAlias")].isNull() && m_collective_alias_isValid;

    m_dba_name_isValid = ::OpenAPI::fromJsonValue(m_dba_name, json[QString("dbaName")]);
    m_dba_name_isSet = !json[QString("dbaName")].isNull() && m_dba_name_isValid;

    m_includes_reports_isValid = ::OpenAPI::fromJsonValue(m_includes_reports, json[QString("includesReports")]);
    m_includes_reports_isSet = !json[QString("includesReports")].isNull() && m_includes_reports_isValid;

    m_kyc_state_isValid = ::OpenAPI::fromJsonValue(m_kyc_state, json[QString("kycState")]);
    m_kyc_state_isSet = !json[QString("kycState")].isNull() && m_kyc_state_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_managing_payees_isValid = ::OpenAPI::fromJsonValue(m_managing_payees, json[QString("managingPayees")]);
    m_managing_payees_isSet = !json[QString("managingPayees")].isNull() && m_managing_payees_isValid;

    m_manual_lockout_isValid = ::OpenAPI::fromJsonValue(m_manual_lockout, json[QString("manualLockout")]);
    m_manual_lockout_isSet = !json[QString("manualLockout")].isNull() && m_manual_lockout_isValid;

    m_max_master_payor_admins_isValid = ::OpenAPI::fromJsonValue(m_max_master_payor_admins, json[QString("maxMasterPayorAdmins")]);
    m_max_master_payor_admins_isSet = !json[QString("maxMasterPayorAdmins")].isNull() && m_max_master_payor_admins_isValid;

    m_open_banking_enabled_isValid = ::OpenAPI::fromJsonValue(m_open_banking_enabled, json[QString("openBankingEnabled")]);
    m_open_banking_enabled_isSet = !json[QString("openBankingEnabled")].isNull() && m_open_banking_enabled_isValid;

    m_payee_grace_period_days_isValid = ::OpenAPI::fromJsonValue(m_payee_grace_period_days, json[QString("payeeGracePeriodDays")]);
    m_payee_grace_period_days_isSet = !json[QString("payeeGracePeriodDays")].isNull() && m_payee_grace_period_days_isValid;

    m_payee_grace_period_processing_enabled_isValid = ::OpenAPI::fromJsonValue(m_payee_grace_period_processing_enabled, json[QString("payeeGracePeriodProcessingEnabled")]);
    m_payee_grace_period_processing_enabled_isSet = !json[QString("payeeGracePeriodProcessingEnabled")].isNull() && m_payee_grace_period_processing_enabled_isValid;

    m_payment_rails_isValid = ::OpenAPI::fromJsonValue(m_payment_rails, json[QString("paymentRails")]);
    m_payment_rails_isSet = !json[QString("paymentRails")].isNull() && m_payment_rails_isValid;

    m_payor_id_isValid = ::OpenAPI::fromJsonValue(m_payor_id, json[QString("payorId")]);
    m_payor_id_isSet = !json[QString("payorId")].isNull() && m_payor_id_isValid;

    m_payor_name_isValid = ::OpenAPI::fromJsonValue(m_payor_name, json[QString("payorName")]);
    m_payor_name_isSet = !json[QString("payorName")].isNull() && m_payor_name_isValid;

    m_payor_xid_isValid = ::OpenAPI::fromJsonValue(m_payor_xid, json[QString("payorXid")]);
    m_payor_xid_isSet = !json[QString("payorXid")].isNull() && m_payor_xid_isValid;

    m_primary_contact_email_isValid = ::OpenAPI::fromJsonValue(m_primary_contact_email, json[QString("primaryContactEmail")]);
    m_primary_contact_email_isSet = !json[QString("primaryContactEmail")].isNull() && m_primary_contact_email_isValid;

    m_primary_contact_name_isValid = ::OpenAPI::fromJsonValue(m_primary_contact_name, json[QString("primaryContactName")]);
    m_primary_contact_name_isSet = !json[QString("primaryContactName")].isNull() && m_primary_contact_name_isValid;

    m_primary_contact_phone_isValid = ::OpenAPI::fromJsonValue(m_primary_contact_phone, json[QString("primaryContactPhone")]);
    m_primary_contact_phone_isSet = !json[QString("primaryContactPhone")].isNull() && m_primary_contact_phone_isValid;

    m_provider_isValid = ::OpenAPI::fromJsonValue(m_provider, json[QString("provider")]);
    m_provider_isSet = !json[QString("provider")].isNull() && m_provider_isValid;

    m_reminder_emails_opt_out_isValid = ::OpenAPI::fromJsonValue(m_reminder_emails_opt_out, json[QString("reminderEmailsOptOut")]);
    m_reminder_emails_opt_out_isSet = !json[QString("reminderEmailsOptOut")].isNull() && m_reminder_emails_opt_out_isValid;

    m_remote_system_ids_isValid = ::OpenAPI::fromJsonValue(m_remote_system_ids, json[QString("remoteSystemIds")]);
    m_remote_system_ids_isSet = !json[QString("remoteSystemIds")].isNull() && m_remote_system_ids_isValid;

    m_support_contact_isValid = ::OpenAPI::fromJsonValue(m_support_contact, json[QString("supportContact")]);
    m_support_contact_isSet = !json[QString("supportContact")].isNull() && m_support_contact_isValid;

    m_transmission_types_isValid = ::OpenAPI::fromJsonValue(m_transmission_types, json[QString("transmissionTypes")]);
    m_transmission_types_isSet = !json[QString("transmissionTypes")].isNull() && m_transmission_types_isValid;

    m_usd_txn_value_reporting_threshold_isValid = ::OpenAPI::fromJsonValue(m_usd_txn_value_reporting_threshold, json[QString("usdTxnValueReportingThreshold")]);
    m_usd_txn_value_reporting_threshold_isSet = !json[QString("usdTxnValueReportingThreshold")].isNull() && m_usd_txn_value_reporting_threshold_isValid;

    m_wu_customer_id_isValid = ::OpenAPI::fromJsonValue(m_wu_customer_id, json[QString("wuCustomerId")]);
    m_wu_customer_id_isSet = !json[QString("wuCustomerId")].isNull() && m_wu_customer_id_isValid;
}

QString OAIPayorV2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPayorV2::asJsonObject() const {
    QJsonObject obj;
    if (m_address.isSet()) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_allows_language_choice_isSet) {
        obj.insert(QString("allowsLanguageChoice"), ::OpenAPI::toJsonValue(m_allows_language_choice));
    }
    if (m_collective_alias_isSet) {
        obj.insert(QString("collectiveAlias"), ::OpenAPI::toJsonValue(m_collective_alias));
    }
    if (m_dba_name_isSet) {
        obj.insert(QString("dbaName"), ::OpenAPI::toJsonValue(m_dba_name));
    }
    if (m_includes_reports_isSet) {
        obj.insert(QString("includesReports"), ::OpenAPI::toJsonValue(m_includes_reports));
    }
    if (m_kyc_state_isSet) {
        obj.insert(QString("kycState"), ::OpenAPI::toJsonValue(m_kyc_state));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_managing_payees_isSet) {
        obj.insert(QString("managingPayees"), ::OpenAPI::toJsonValue(m_managing_payees));
    }
    if (m_manual_lockout_isSet) {
        obj.insert(QString("manualLockout"), ::OpenAPI::toJsonValue(m_manual_lockout));
    }
    if (m_max_master_payor_admins_isSet) {
        obj.insert(QString("maxMasterPayorAdmins"), ::OpenAPI::toJsonValue(m_max_master_payor_admins));
    }
    if (m_open_banking_enabled_isSet) {
        obj.insert(QString("openBankingEnabled"), ::OpenAPI::toJsonValue(m_open_banking_enabled));
    }
    if (m_payee_grace_period_days_isSet) {
        obj.insert(QString("payeeGracePeriodDays"), ::OpenAPI::toJsonValue(m_payee_grace_period_days));
    }
    if (m_payee_grace_period_processing_enabled_isSet) {
        obj.insert(QString("payeeGracePeriodProcessingEnabled"), ::OpenAPI::toJsonValue(m_payee_grace_period_processing_enabled));
    }
    if (m_payment_rails_isSet) {
        obj.insert(QString("paymentRails"), ::OpenAPI::toJsonValue(m_payment_rails));
    }
    if (m_payor_id_isSet) {
        obj.insert(QString("payorId"), ::OpenAPI::toJsonValue(m_payor_id));
    }
    if (m_payor_name_isSet) {
        obj.insert(QString("payorName"), ::OpenAPI::toJsonValue(m_payor_name));
    }
    if (m_payor_xid_isSet) {
        obj.insert(QString("payorXid"), ::OpenAPI::toJsonValue(m_payor_xid));
    }
    if (m_primary_contact_email_isSet) {
        obj.insert(QString("primaryContactEmail"), ::OpenAPI::toJsonValue(m_primary_contact_email));
    }
    if (m_primary_contact_name_isSet) {
        obj.insert(QString("primaryContactName"), ::OpenAPI::toJsonValue(m_primary_contact_name));
    }
    if (m_primary_contact_phone_isSet) {
        obj.insert(QString("primaryContactPhone"), ::OpenAPI::toJsonValue(m_primary_contact_phone));
    }
    if (m_provider_isSet) {
        obj.insert(QString("provider"), ::OpenAPI::toJsonValue(m_provider));
    }
    if (m_reminder_emails_opt_out_isSet) {
        obj.insert(QString("reminderEmailsOptOut"), ::OpenAPI::toJsonValue(m_reminder_emails_opt_out));
    }
    if (m_remote_system_ids.size() > 0) {
        obj.insert(QString("remoteSystemIds"), ::OpenAPI::toJsonValue(m_remote_system_ids));
    }
    if (m_support_contact_isSet) {
        obj.insert(QString("supportContact"), ::OpenAPI::toJsonValue(m_support_contact));
    }
    if (m_transmission_types.isSet()) {
        obj.insert(QString("transmissionTypes"), ::OpenAPI::toJsonValue(m_transmission_types));
    }
    if (m_usd_txn_value_reporting_threshold_isSet) {
        obj.insert(QString("usdTxnValueReportingThreshold"), ::OpenAPI::toJsonValue(m_usd_txn_value_reporting_threshold));
    }
    if (m_wu_customer_id_isSet) {
        obj.insert(QString("wuCustomerId"), ::OpenAPI::toJsonValue(m_wu_customer_id));
    }
    return obj;
}

OAIPayorAddressV2 OAIPayorV2::getAddress() const {
    return m_address;
}
void OAIPayorV2::setAddress(const OAIPayorAddressV2 &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIPayorV2::is_address_Set() const{
    return m_address_isSet;
}

bool OAIPayorV2::is_address_Valid() const{
    return m_address_isValid;
}

bool OAIPayorV2::isAllowsLanguageChoice() const {
    return m_allows_language_choice;
}
void OAIPayorV2::setAllowsLanguageChoice(const bool &allows_language_choice) {
    m_allows_language_choice = allows_language_choice;
    m_allows_language_choice_isSet = true;
}

bool OAIPayorV2::is_allows_language_choice_Set() const{
    return m_allows_language_choice_isSet;
}

bool OAIPayorV2::is_allows_language_choice_Valid() const{
    return m_allows_language_choice_isValid;
}

QString OAIPayorV2::getCollectiveAlias() const {
    return m_collective_alias;
}
void OAIPayorV2::setCollectiveAlias(const QString &collective_alias) {
    m_collective_alias = collective_alias;
    m_collective_alias_isSet = true;
}

bool OAIPayorV2::is_collective_alias_Set() const{
    return m_collective_alias_isSet;
}

bool OAIPayorV2::is_collective_alias_Valid() const{
    return m_collective_alias_isValid;
}

QString OAIPayorV2::getDbaName() const {
    return m_dba_name;
}
void OAIPayorV2::setDbaName(const QString &dba_name) {
    m_dba_name = dba_name;
    m_dba_name_isSet = true;
}

bool OAIPayorV2::is_dba_name_Set() const{
    return m_dba_name_isSet;
}

bool OAIPayorV2::is_dba_name_Valid() const{
    return m_dba_name_isValid;
}

bool OAIPayorV2::isIncludesReports() const {
    return m_includes_reports;
}
void OAIPayorV2::setIncludesReports(const bool &includes_reports) {
    m_includes_reports = includes_reports;
    m_includes_reports_isSet = true;
}

bool OAIPayorV2::is_includes_reports_Set() const{
    return m_includes_reports_isSet;
}

bool OAIPayorV2::is_includes_reports_Valid() const{
    return m_includes_reports_isValid;
}

QString OAIPayorV2::getKycState() const {
    return m_kyc_state;
}
void OAIPayorV2::setKycState(const QString &kyc_state) {
    m_kyc_state = kyc_state;
    m_kyc_state_isSet = true;
}

bool OAIPayorV2::is_kyc_state_Set() const{
    return m_kyc_state_isSet;
}

bool OAIPayorV2::is_kyc_state_Valid() const{
    return m_kyc_state_isValid;
}

QString OAIPayorV2::getLanguage() const {
    return m_language;
}
void OAIPayorV2::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIPayorV2::is_language_Set() const{
    return m_language_isSet;
}

bool OAIPayorV2::is_language_Valid() const{
    return m_language_isValid;
}

bool OAIPayorV2::isManagingPayees() const {
    return m_managing_payees;
}
void OAIPayorV2::setManagingPayees(const bool &managing_payees) {
    m_managing_payees = managing_payees;
    m_managing_payees_isSet = true;
}

bool OAIPayorV2::is_managing_payees_Set() const{
    return m_managing_payees_isSet;
}

bool OAIPayorV2::is_managing_payees_Valid() const{
    return m_managing_payees_isValid;
}

bool OAIPayorV2::isManualLockout() const {
    return m_manual_lockout;
}
void OAIPayorV2::setManualLockout(const bool &manual_lockout) {
    m_manual_lockout = manual_lockout;
    m_manual_lockout_isSet = true;
}

bool OAIPayorV2::is_manual_lockout_Set() const{
    return m_manual_lockout_isSet;
}

bool OAIPayorV2::is_manual_lockout_Valid() const{
    return m_manual_lockout_isValid;
}

qint32 OAIPayorV2::getMaxMasterPayorAdmins() const {
    return m_max_master_payor_admins;
}
void OAIPayorV2::setMaxMasterPayorAdmins(const qint32 &max_master_payor_admins) {
    m_max_master_payor_admins = max_master_payor_admins;
    m_max_master_payor_admins_isSet = true;
}

bool OAIPayorV2::is_max_master_payor_admins_Set() const{
    return m_max_master_payor_admins_isSet;
}

bool OAIPayorV2::is_max_master_payor_admins_Valid() const{
    return m_max_master_payor_admins_isValid;
}

bool OAIPayorV2::isOpenBankingEnabled() const {
    return m_open_banking_enabled;
}
void OAIPayorV2::setOpenBankingEnabled(const bool &open_banking_enabled) {
    m_open_banking_enabled = open_banking_enabled;
    m_open_banking_enabled_isSet = true;
}

bool OAIPayorV2::is_open_banking_enabled_Set() const{
    return m_open_banking_enabled_isSet;
}

bool OAIPayorV2::is_open_banking_enabled_Valid() const{
    return m_open_banking_enabled_isValid;
}

qint32 OAIPayorV2::getPayeeGracePeriodDays() const {
    return m_payee_grace_period_days;
}
void OAIPayorV2::setPayeeGracePeriodDays(const qint32 &payee_grace_period_days) {
    m_payee_grace_period_days = payee_grace_period_days;
    m_payee_grace_period_days_isSet = true;
}

bool OAIPayorV2::is_payee_grace_period_days_Set() const{
    return m_payee_grace_period_days_isSet;
}

bool OAIPayorV2::is_payee_grace_period_days_Valid() const{
    return m_payee_grace_period_days_isValid;
}

bool OAIPayorV2::isPayeeGracePeriodProcessingEnabled() const {
    return m_payee_grace_period_processing_enabled;
}
void OAIPayorV2::setPayeeGracePeriodProcessingEnabled(const bool &payee_grace_period_processing_enabled) {
    m_payee_grace_period_processing_enabled = payee_grace_period_processing_enabled;
    m_payee_grace_period_processing_enabled_isSet = true;
}

bool OAIPayorV2::is_payee_grace_period_processing_enabled_Set() const{
    return m_payee_grace_period_processing_enabled_isSet;
}

bool OAIPayorV2::is_payee_grace_period_processing_enabled_Valid() const{
    return m_payee_grace_period_processing_enabled_isValid;
}

QString OAIPayorV2::getPaymentRails() const {
    return m_payment_rails;
}
void OAIPayorV2::setPaymentRails(const QString &payment_rails) {
    m_payment_rails = payment_rails;
    m_payment_rails_isSet = true;
}

bool OAIPayorV2::is_payment_rails_Set() const{
    return m_payment_rails_isSet;
}

bool OAIPayorV2::is_payment_rails_Valid() const{
    return m_payment_rails_isValid;
}

QString OAIPayorV2::getPayorId() const {
    return m_payor_id;
}
void OAIPayorV2::setPayorId(const QString &payor_id) {
    m_payor_id = payor_id;
    m_payor_id_isSet = true;
}

bool OAIPayorV2::is_payor_id_Set() const{
    return m_payor_id_isSet;
}

bool OAIPayorV2::is_payor_id_Valid() const{
    return m_payor_id_isValid;
}

QString OAIPayorV2::getPayorName() const {
    return m_payor_name;
}
void OAIPayorV2::setPayorName(const QString &payor_name) {
    m_payor_name = payor_name;
    m_payor_name_isSet = true;
}

bool OAIPayorV2::is_payor_name_Set() const{
    return m_payor_name_isSet;
}

bool OAIPayorV2::is_payor_name_Valid() const{
    return m_payor_name_isValid;
}

QString OAIPayorV2::getPayorXid() const {
    return m_payor_xid;
}
void OAIPayorV2::setPayorXid(const QString &payor_xid) {
    m_payor_xid = payor_xid;
    m_payor_xid_isSet = true;
}

bool OAIPayorV2::is_payor_xid_Set() const{
    return m_payor_xid_isSet;
}

bool OAIPayorV2::is_payor_xid_Valid() const{
    return m_payor_xid_isValid;
}

QString OAIPayorV2::getPrimaryContactEmail() const {
    return m_primary_contact_email;
}
void OAIPayorV2::setPrimaryContactEmail(const QString &primary_contact_email) {
    m_primary_contact_email = primary_contact_email;
    m_primary_contact_email_isSet = true;
}

bool OAIPayorV2::is_primary_contact_email_Set() const{
    return m_primary_contact_email_isSet;
}

bool OAIPayorV2::is_primary_contact_email_Valid() const{
    return m_primary_contact_email_isValid;
}

QString OAIPayorV2::getPrimaryContactName() const {
    return m_primary_contact_name;
}
void OAIPayorV2::setPrimaryContactName(const QString &primary_contact_name) {
    m_primary_contact_name = primary_contact_name;
    m_primary_contact_name_isSet = true;
}

bool OAIPayorV2::is_primary_contact_name_Set() const{
    return m_primary_contact_name_isSet;
}

bool OAIPayorV2::is_primary_contact_name_Valid() const{
    return m_primary_contact_name_isValid;
}

QString OAIPayorV2::getPrimaryContactPhone() const {
    return m_primary_contact_phone;
}
void OAIPayorV2::setPrimaryContactPhone(const QString &primary_contact_phone) {
    m_primary_contact_phone = primary_contact_phone;
    m_primary_contact_phone_isSet = true;
}

bool OAIPayorV2::is_primary_contact_phone_Set() const{
    return m_primary_contact_phone_isSet;
}

bool OAIPayorV2::is_primary_contact_phone_Valid() const{
    return m_primary_contact_phone_isValid;
}

QString OAIPayorV2::getProvider() const {
    return m_provider;
}
void OAIPayorV2::setProvider(const QString &provider) {
    m_provider = provider;
    m_provider_isSet = true;
}

bool OAIPayorV2::is_provider_Set() const{
    return m_provider_isSet;
}

bool OAIPayorV2::is_provider_Valid() const{
    return m_provider_isValid;
}

bool OAIPayorV2::isReminderEmailsOptOut() const {
    return m_reminder_emails_opt_out;
}
void OAIPayorV2::setReminderEmailsOptOut(const bool &reminder_emails_opt_out) {
    m_reminder_emails_opt_out = reminder_emails_opt_out;
    m_reminder_emails_opt_out_isSet = true;
}

bool OAIPayorV2::is_reminder_emails_opt_out_Set() const{
    return m_reminder_emails_opt_out_isSet;
}

bool OAIPayorV2::is_reminder_emails_opt_out_Valid() const{
    return m_reminder_emails_opt_out_isValid;
}

QList<QString> OAIPayorV2::getRemoteSystemIds() const {
    return m_remote_system_ids;
}
void OAIPayorV2::setRemoteSystemIds(const QList<QString> &remote_system_ids) {
    m_remote_system_ids = remote_system_ids;
    m_remote_system_ids_isSet = true;
}

bool OAIPayorV2::is_remote_system_ids_Set() const{
    return m_remote_system_ids_isSet;
}

bool OAIPayorV2::is_remote_system_ids_Valid() const{
    return m_remote_system_ids_isValid;
}

QString OAIPayorV2::getSupportContact() const {
    return m_support_contact;
}
void OAIPayorV2::setSupportContact(const QString &support_contact) {
    m_support_contact = support_contact;
    m_support_contact_isSet = true;
}

bool OAIPayorV2::is_support_contact_Set() const{
    return m_support_contact_isSet;
}

bool OAIPayorV2::is_support_contact_Valid() const{
    return m_support_contact_isValid;
}

OAITransmissionTypes_2 OAIPayorV2::getTransmissionTypes() const {
    return m_transmission_types;
}
void OAIPayorV2::setTransmissionTypes(const OAITransmissionTypes_2 &transmission_types) {
    m_transmission_types = transmission_types;
    m_transmission_types_isSet = true;
}

bool OAIPayorV2::is_transmission_types_Set() const{
    return m_transmission_types_isSet;
}

bool OAIPayorV2::is_transmission_types_Valid() const{
    return m_transmission_types_isValid;
}

qint32 OAIPayorV2::getUsdTxnValueReportingThreshold() const {
    return m_usd_txn_value_reporting_threshold;
}
void OAIPayorV2::setUsdTxnValueReportingThreshold(const qint32 &usd_txn_value_reporting_threshold) {
    m_usd_txn_value_reporting_threshold = usd_txn_value_reporting_threshold;
    m_usd_txn_value_reporting_threshold_isSet = true;
}

bool OAIPayorV2::is_usd_txn_value_reporting_threshold_Set() const{
    return m_usd_txn_value_reporting_threshold_isSet;
}

bool OAIPayorV2::is_usd_txn_value_reporting_threshold_Valid() const{
    return m_usd_txn_value_reporting_threshold_isValid;
}

QString OAIPayorV2::getWuCustomerId() const {
    return m_wu_customer_id;
}
void OAIPayorV2::setWuCustomerId(const QString &wu_customer_id) {
    m_wu_customer_id = wu_customer_id;
    m_wu_customer_id_isSet = true;
}

bool OAIPayorV2::is_wu_customer_id_Set() const{
    return m_wu_customer_id_isSet;
}

bool OAIPayorV2::is_wu_customer_id_Valid() const{
    return m_wu_customer_id_isValid;
}

bool OAIPayorV2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_allows_language_choice_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_collective_alias_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dba_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_includes_reports_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kyc_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_managing_payees_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_manual_lockout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_master_payor_admins_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_open_banking_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payee_grace_period_days_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payee_grace_period_processing_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_rails_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payor_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payor_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payor_xid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_contact_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_contact_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_contact_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reminder_emails_opt_out_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_remote_system_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_support_contact_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transmission_types.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_usd_txn_value_reporting_threshold_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wu_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPayorV2::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_payor_id_isValid && m_payor_name_isValid && true;
}

} // namespace OpenAPI
