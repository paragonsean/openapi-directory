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

#include "OAISourceAccountResponseV3.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISourceAccountResponseV3::OAISourceAccountResponseV3(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISourceAccountResponseV3::OAISourceAccountResponseV3() {
    this->initializeModel();
}

OAISourceAccountResponseV3::~OAISourceAccountResponseV3() {}

void OAISourceAccountResponseV3::initializeModel() {

    m_auto_top_up_config_isSet = false;
    m_auto_top_up_config_isValid = false;

    m_balance_isSet = false;
    m_balance_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_deleted_at_isSet = false;
    m_deleted_at_isValid = false;

    m_funding_ref_isSet = false;
    m_funding_ref_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_notifications_isSet = false;
    m_notifications_isValid = false;

    m_payor_id_isSet = false;
    m_payor_id_isValid = false;

    m_physical_account_id_isSet = false;
    m_physical_account_id_isValid = false;

    m_physical_account_name_isSet = false;
    m_physical_account_name_isValid = false;

    m_pooled_isSet = false;
    m_pooled_isValid = false;

    m_rails_id_isSet = false;
    m_rails_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_user_deleted_isSet = false;
    m_user_deleted_isValid = false;
}

void OAISourceAccountResponseV3::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISourceAccountResponseV3::fromJsonObject(QJsonObject json) {

    m_auto_top_up_config_isValid = ::OpenAPI::fromJsonValue(m_auto_top_up_config, json[QString("autoTopUpConfig")]);
    m_auto_top_up_config_isSet = !json[QString("autoTopUpConfig")].isNull() && m_auto_top_up_config_isValid;

    m_balance_isValid = ::OpenAPI::fromJsonValue(m_balance, json[QString("balance")]);
    m_balance_isSet = !json[QString("balance")].isNull() && m_balance_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_deleted_at_isValid = ::OpenAPI::fromJsonValue(m_deleted_at, json[QString("deletedAt")]);
    m_deleted_at_isSet = !json[QString("deletedAt")].isNull() && m_deleted_at_isValid;

    m_funding_ref_isValid = ::OpenAPI::fromJsonValue(m_funding_ref, json[QString("fundingRef")]);
    m_funding_ref_isSet = !json[QString("fundingRef")].isNull() && m_funding_ref_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_notifications_isValid = ::OpenAPI::fromJsonValue(m_notifications, json[QString("notifications")]);
    m_notifications_isSet = !json[QString("notifications")].isNull() && m_notifications_isValid;

    m_payor_id_isValid = ::OpenAPI::fromJsonValue(m_payor_id, json[QString("payorId")]);
    m_payor_id_isSet = !json[QString("payorId")].isNull() && m_payor_id_isValid;

    m_physical_account_id_isValid = ::OpenAPI::fromJsonValue(m_physical_account_id, json[QString("physicalAccountId")]);
    m_physical_account_id_isSet = !json[QString("physicalAccountId")].isNull() && m_physical_account_id_isValid;

    m_physical_account_name_isValid = ::OpenAPI::fromJsonValue(m_physical_account_name, json[QString("physicalAccountName")]);
    m_physical_account_name_isSet = !json[QString("physicalAccountName")].isNull() && m_physical_account_name_isValid;

    m_pooled_isValid = ::OpenAPI::fromJsonValue(m_pooled, json[QString("pooled")]);
    m_pooled_isSet = !json[QString("pooled")].isNull() && m_pooled_isValid;

    m_rails_id_isValid = ::OpenAPI::fromJsonValue(m_rails_id, json[QString("railsId")]);
    m_rails_id_isSet = !json[QString("railsId")].isNull() && m_rails_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_user_deleted_isValid = ::OpenAPI::fromJsonValue(m_user_deleted, json[QString("userDeleted")]);
    m_user_deleted_isSet = !json[QString("userDeleted")].isNull() && m_user_deleted_isValid;
}

QString OAISourceAccountResponseV3::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISourceAccountResponseV3::asJsonObject() const {
    QJsonObject obj;
    if (m_auto_top_up_config.isSet()) {
        obj.insert(QString("autoTopUpConfig"), ::OpenAPI::toJsonValue(m_auto_top_up_config));
    }
    if (m_balance_isSet) {
        obj.insert(QString("balance"), ::OpenAPI::toJsonValue(m_balance));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_deleted_at_isSet) {
        obj.insert(QString("deletedAt"), ::OpenAPI::toJsonValue(m_deleted_at));
    }
    if (m_funding_ref_isSet) {
        obj.insert(QString("fundingRef"), ::OpenAPI::toJsonValue(m_funding_ref));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_notifications.isSet()) {
        obj.insert(QString("notifications"), ::OpenAPI::toJsonValue(m_notifications));
    }
    if (m_payor_id_isSet) {
        obj.insert(QString("payorId"), ::OpenAPI::toJsonValue(m_payor_id));
    }
    if (m_physical_account_id_isSet) {
        obj.insert(QString("physicalAccountId"), ::OpenAPI::toJsonValue(m_physical_account_id));
    }
    if (m_physical_account_name_isSet) {
        obj.insert(QString("physicalAccountName"), ::OpenAPI::toJsonValue(m_physical_account_name));
    }
    if (m_pooled_isSet) {
        obj.insert(QString("pooled"), ::OpenAPI::toJsonValue(m_pooled));
    }
    if (m_rails_id_isSet) {
        obj.insert(QString("railsId"), ::OpenAPI::toJsonValue(m_rails_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_user_deleted_isSet) {
        obj.insert(QString("userDeleted"), ::OpenAPI::toJsonValue(m_user_deleted));
    }
    return obj;
}

OAIAutoTopUpConfigV3 OAISourceAccountResponseV3::getAutoTopUpConfig() const {
    return m_auto_top_up_config;
}
void OAISourceAccountResponseV3::setAutoTopUpConfig(const OAIAutoTopUpConfigV3 &auto_top_up_config) {
    m_auto_top_up_config = auto_top_up_config;
    m_auto_top_up_config_isSet = true;
}

bool OAISourceAccountResponseV3::is_auto_top_up_config_Set() const{
    return m_auto_top_up_config_isSet;
}

bool OAISourceAccountResponseV3::is_auto_top_up_config_Valid() const{
    return m_auto_top_up_config_isValid;
}

qint64 OAISourceAccountResponseV3::getBalance() const {
    return m_balance;
}
void OAISourceAccountResponseV3::setBalance(const qint64 &balance) {
    m_balance = balance;
    m_balance_isSet = true;
}

bool OAISourceAccountResponseV3::is_balance_Set() const{
    return m_balance_isSet;
}

bool OAISourceAccountResponseV3::is_balance_Valid() const{
    return m_balance_isValid;
}

QString OAISourceAccountResponseV3::getCountry() const {
    return m_country;
}
void OAISourceAccountResponseV3::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAISourceAccountResponseV3::is_country_Set() const{
    return m_country_isSet;
}

bool OAISourceAccountResponseV3::is_country_Valid() const{
    return m_country_isValid;
}

QString OAISourceAccountResponseV3::getCurrency() const {
    return m_currency;
}
void OAISourceAccountResponseV3::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAISourceAccountResponseV3::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAISourceAccountResponseV3::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAISourceAccountResponseV3::getCustomerId() const {
    return m_customer_id;
}
void OAISourceAccountResponseV3::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAISourceAccountResponseV3::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAISourceAccountResponseV3::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

bool OAISourceAccountResponseV3::isDeleted() const {
    return m_deleted;
}
void OAISourceAccountResponseV3::setDeleted(const bool &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAISourceAccountResponseV3::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAISourceAccountResponseV3::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QDateTime OAISourceAccountResponseV3::getDeletedAt() const {
    return m_deleted_at;
}
void OAISourceAccountResponseV3::setDeletedAt(const QDateTime &deleted_at) {
    m_deleted_at = deleted_at;
    m_deleted_at_isSet = true;
}

bool OAISourceAccountResponseV3::is_deleted_at_Set() const{
    return m_deleted_at_isSet;
}

bool OAISourceAccountResponseV3::is_deleted_at_Valid() const{
    return m_deleted_at_isValid;
}

QString OAISourceAccountResponseV3::getFundingRef() const {
    return m_funding_ref;
}
void OAISourceAccountResponseV3::setFundingRef(const QString &funding_ref) {
    m_funding_ref = funding_ref;
    m_funding_ref_isSet = true;
}

bool OAISourceAccountResponseV3::is_funding_ref_Set() const{
    return m_funding_ref_isSet;
}

bool OAISourceAccountResponseV3::is_funding_ref_Valid() const{
    return m_funding_ref_isValid;
}

QString OAISourceAccountResponseV3::getId() const {
    return m_id;
}
void OAISourceAccountResponseV3::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISourceAccountResponseV3::is_id_Set() const{
    return m_id_isSet;
}

bool OAISourceAccountResponseV3::is_id_Valid() const{
    return m_id_isValid;
}

QString OAISourceAccountResponseV3::getName() const {
    return m_name;
}
void OAISourceAccountResponseV3::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISourceAccountResponseV3::is_name_Set() const{
    return m_name_isSet;
}

bool OAISourceAccountResponseV3::is_name_Valid() const{
    return m_name_isValid;
}

OAINotificationsV3 OAISourceAccountResponseV3::getNotifications() const {
    return m_notifications;
}
void OAISourceAccountResponseV3::setNotifications(const OAINotificationsV3 &notifications) {
    m_notifications = notifications;
    m_notifications_isSet = true;
}

bool OAISourceAccountResponseV3::is_notifications_Set() const{
    return m_notifications_isSet;
}

bool OAISourceAccountResponseV3::is_notifications_Valid() const{
    return m_notifications_isValid;
}

QString OAISourceAccountResponseV3::getPayorId() const {
    return m_payor_id;
}
void OAISourceAccountResponseV3::setPayorId(const QString &payor_id) {
    m_payor_id = payor_id;
    m_payor_id_isSet = true;
}

bool OAISourceAccountResponseV3::is_payor_id_Set() const{
    return m_payor_id_isSet;
}

bool OAISourceAccountResponseV3::is_payor_id_Valid() const{
    return m_payor_id_isValid;
}

QString OAISourceAccountResponseV3::getPhysicalAccountId() const {
    return m_physical_account_id;
}
void OAISourceAccountResponseV3::setPhysicalAccountId(const QString &physical_account_id) {
    m_physical_account_id = physical_account_id;
    m_physical_account_id_isSet = true;
}

bool OAISourceAccountResponseV3::is_physical_account_id_Set() const{
    return m_physical_account_id_isSet;
}

bool OAISourceAccountResponseV3::is_physical_account_id_Valid() const{
    return m_physical_account_id_isValid;
}

QString OAISourceAccountResponseV3::getPhysicalAccountName() const {
    return m_physical_account_name;
}
void OAISourceAccountResponseV3::setPhysicalAccountName(const QString &physical_account_name) {
    m_physical_account_name = physical_account_name;
    m_physical_account_name_isSet = true;
}

bool OAISourceAccountResponseV3::is_physical_account_name_Set() const{
    return m_physical_account_name_isSet;
}

bool OAISourceAccountResponseV3::is_physical_account_name_Valid() const{
    return m_physical_account_name_isValid;
}

bool OAISourceAccountResponseV3::isPooled() const {
    return m_pooled;
}
void OAISourceAccountResponseV3::setPooled(const bool &pooled) {
    m_pooled = pooled;
    m_pooled_isSet = true;
}

bool OAISourceAccountResponseV3::is_pooled_Set() const{
    return m_pooled_isSet;
}

bool OAISourceAccountResponseV3::is_pooled_Valid() const{
    return m_pooled_isValid;
}

QString OAISourceAccountResponseV3::getRailsId() const {
    return m_rails_id;
}
void OAISourceAccountResponseV3::setRailsId(const QString &rails_id) {
    m_rails_id = rails_id;
    m_rails_id_isSet = true;
}

bool OAISourceAccountResponseV3::is_rails_id_Set() const{
    return m_rails_id_isSet;
}

bool OAISourceAccountResponseV3::is_rails_id_Valid() const{
    return m_rails_id_isValid;
}

QString OAISourceAccountResponseV3::getType() const {
    return m_type;
}
void OAISourceAccountResponseV3::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAISourceAccountResponseV3::is_type_Set() const{
    return m_type_isSet;
}

bool OAISourceAccountResponseV3::is_type_Valid() const{
    return m_type_isValid;
}

bool OAISourceAccountResponseV3::isUserDeleted() const {
    return m_user_deleted;
}
void OAISourceAccountResponseV3::setUserDeleted(const bool &user_deleted) {
    m_user_deleted = user_deleted;
    m_user_deleted_isSet = true;
}

bool OAISourceAccountResponseV3::is_user_deleted_Set() const{
    return m_user_deleted_isSet;
}

bool OAISourceAccountResponseV3::is_user_deleted_Valid() const{
    return m_user_deleted_isValid;
}

bool OAISourceAccountResponseV3::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auto_top_up_config.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_balance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_funding_ref_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notifications.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_payor_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_physical_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_physical_account_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pooled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rails_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISourceAccountResponseV3::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_rails_id_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
