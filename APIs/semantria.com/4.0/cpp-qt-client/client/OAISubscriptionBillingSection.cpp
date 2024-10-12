/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISubscriptionBillingSection.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscriptionBillingSection::OAISubscriptionBillingSection(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscriptionBillingSection::OAISubscriptionBillingSection() {
    this->initializeModel();
}

OAISubscriptionBillingSection::~OAISubscriptionBillingSection() {}

void OAISubscriptionBillingSection::initializeModel() {

    m_app_seats_allocated_isSet = false;
    m_app_seats_allocated_isValid = false;

    m_app_seats_permitted_isSet = false;
    m_app_seats_permitted_isValid = false;

    m_data_calls_balance_isSet = false;
    m_data_calls_balance_isValid = false;

    m_data_calls_limit_isSet = false;
    m_data_calls_limit_isValid = false;

    m_data_calls_limit_interval_isSet = false;
    m_data_calls_limit_interval_isValid = false;

    m_docs_balance_isSet = false;
    m_docs_balance_isValid = false;

    m_docs_limit_isSet = false;
    m_docs_limit_isValid = false;

    m_docs_limit_interval_isSet = false;
    m_docs_limit_interval_isValid = false;

    m_docs_suggested_isSet = false;
    m_docs_suggested_isValid = false;

    m_docs_suggested_interval_isSet = false;
    m_docs_suggested_interval_isValid = false;

    m_expiration_date_isSet = false;
    m_expiration_date_isValid = false;

    m_limit_type_isSet = false;
    m_limit_type_isValid = false;

    m_polling_calls_balance_isSet = false;
    m_polling_calls_balance_isValid = false;

    m_polling_calls_limit_isSet = false;
    m_polling_calls_limit_isValid = false;

    m_polling_calls_limit_interval_isSet = false;
    m_polling_calls_limit_interval_isValid = false;

    m_priority_isSet = false;
    m_priority_isValid = false;

    m_settings_calls_balance_isSet = false;
    m_settings_calls_balance_isValid = false;

    m_settings_calls_limit_isSet = false;
    m_settings_calls_limit_isValid = false;

    m_settings_calls_limit_interval_isSet = false;
    m_settings_calls_limit_interval_isValid = false;
}

void OAISubscriptionBillingSection::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubscriptionBillingSection::fromJsonObject(QJsonObject json) {

    m_app_seats_allocated_isValid = ::OpenAPI::fromJsonValue(m_app_seats_allocated, json[QString("app_seats_allocated")]);
    m_app_seats_allocated_isSet = !json[QString("app_seats_allocated")].isNull() && m_app_seats_allocated_isValid;

    m_app_seats_permitted_isValid = ::OpenAPI::fromJsonValue(m_app_seats_permitted, json[QString("app_seats_permitted")]);
    m_app_seats_permitted_isSet = !json[QString("app_seats_permitted")].isNull() && m_app_seats_permitted_isValid;

    m_data_calls_balance_isValid = ::OpenAPI::fromJsonValue(m_data_calls_balance, json[QString("data_calls_balance")]);
    m_data_calls_balance_isSet = !json[QString("data_calls_balance")].isNull() && m_data_calls_balance_isValid;

    m_data_calls_limit_isValid = ::OpenAPI::fromJsonValue(m_data_calls_limit, json[QString("data_calls_limit")]);
    m_data_calls_limit_isSet = !json[QString("data_calls_limit")].isNull() && m_data_calls_limit_isValid;

    m_data_calls_limit_interval_isValid = ::OpenAPI::fromJsonValue(m_data_calls_limit_interval, json[QString("data_calls_limit_interval")]);
    m_data_calls_limit_interval_isSet = !json[QString("data_calls_limit_interval")].isNull() && m_data_calls_limit_interval_isValid;

    m_docs_balance_isValid = ::OpenAPI::fromJsonValue(m_docs_balance, json[QString("docs_balance")]);
    m_docs_balance_isSet = !json[QString("docs_balance")].isNull() && m_docs_balance_isValid;

    m_docs_limit_isValid = ::OpenAPI::fromJsonValue(m_docs_limit, json[QString("docs_limit")]);
    m_docs_limit_isSet = !json[QString("docs_limit")].isNull() && m_docs_limit_isValid;

    m_docs_limit_interval_isValid = ::OpenAPI::fromJsonValue(m_docs_limit_interval, json[QString("docs_limit_interval")]);
    m_docs_limit_interval_isSet = !json[QString("docs_limit_interval")].isNull() && m_docs_limit_interval_isValid;

    m_docs_suggested_isValid = ::OpenAPI::fromJsonValue(m_docs_suggested, json[QString("docs_suggested")]);
    m_docs_suggested_isSet = !json[QString("docs_suggested")].isNull() && m_docs_suggested_isValid;

    m_docs_suggested_interval_isValid = ::OpenAPI::fromJsonValue(m_docs_suggested_interval, json[QString("docs_suggested_interval")]);
    m_docs_suggested_interval_isSet = !json[QString("docs_suggested_interval")].isNull() && m_docs_suggested_interval_isValid;

    m_expiration_date_isValid = ::OpenAPI::fromJsonValue(m_expiration_date, json[QString("expiration_date")]);
    m_expiration_date_isSet = !json[QString("expiration_date")].isNull() && m_expiration_date_isValid;

    m_limit_type_isValid = ::OpenAPI::fromJsonValue(m_limit_type, json[QString("limit_type")]);
    m_limit_type_isSet = !json[QString("limit_type")].isNull() && m_limit_type_isValid;

    m_polling_calls_balance_isValid = ::OpenAPI::fromJsonValue(m_polling_calls_balance, json[QString("polling_calls_balance")]);
    m_polling_calls_balance_isSet = !json[QString("polling_calls_balance")].isNull() && m_polling_calls_balance_isValid;

    m_polling_calls_limit_isValid = ::OpenAPI::fromJsonValue(m_polling_calls_limit, json[QString("polling_calls_limit")]);
    m_polling_calls_limit_isSet = !json[QString("polling_calls_limit")].isNull() && m_polling_calls_limit_isValid;

    m_polling_calls_limit_interval_isValid = ::OpenAPI::fromJsonValue(m_polling_calls_limit_interval, json[QString("polling_calls_limit_interval")]);
    m_polling_calls_limit_interval_isSet = !json[QString("polling_calls_limit_interval")].isNull() && m_polling_calls_limit_interval_isValid;

    m_priority_isValid = ::OpenAPI::fromJsonValue(m_priority, json[QString("priority")]);
    m_priority_isSet = !json[QString("priority")].isNull() && m_priority_isValid;

    m_settings_calls_balance_isValid = ::OpenAPI::fromJsonValue(m_settings_calls_balance, json[QString("settings_calls_balance")]);
    m_settings_calls_balance_isSet = !json[QString("settings_calls_balance")].isNull() && m_settings_calls_balance_isValid;

    m_settings_calls_limit_isValid = ::OpenAPI::fromJsonValue(m_settings_calls_limit, json[QString("settings_calls_limit")]);
    m_settings_calls_limit_isSet = !json[QString("settings_calls_limit")].isNull() && m_settings_calls_limit_isValid;

    m_settings_calls_limit_interval_isValid = ::OpenAPI::fromJsonValue(m_settings_calls_limit_interval, json[QString("settings_calls_limit_interval")]);
    m_settings_calls_limit_interval_isSet = !json[QString("settings_calls_limit_interval")].isNull() && m_settings_calls_limit_interval_isValid;
}

QString OAISubscriptionBillingSection::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubscriptionBillingSection::asJsonObject() const {
    QJsonObject obj;
    if (m_app_seats_allocated_isSet) {
        obj.insert(QString("app_seats_allocated"), ::OpenAPI::toJsonValue(m_app_seats_allocated));
    }
    if (m_app_seats_permitted_isSet) {
        obj.insert(QString("app_seats_permitted"), ::OpenAPI::toJsonValue(m_app_seats_permitted));
    }
    if (m_data_calls_balance_isSet) {
        obj.insert(QString("data_calls_balance"), ::OpenAPI::toJsonValue(m_data_calls_balance));
    }
    if (m_data_calls_limit_isSet) {
        obj.insert(QString("data_calls_limit"), ::OpenAPI::toJsonValue(m_data_calls_limit));
    }
    if (m_data_calls_limit_interval_isSet) {
        obj.insert(QString("data_calls_limit_interval"), ::OpenAPI::toJsonValue(m_data_calls_limit_interval));
    }
    if (m_docs_balance_isSet) {
        obj.insert(QString("docs_balance"), ::OpenAPI::toJsonValue(m_docs_balance));
    }
    if (m_docs_limit_isSet) {
        obj.insert(QString("docs_limit"), ::OpenAPI::toJsonValue(m_docs_limit));
    }
    if (m_docs_limit_interval_isSet) {
        obj.insert(QString("docs_limit_interval"), ::OpenAPI::toJsonValue(m_docs_limit_interval));
    }
    if (m_docs_suggested_isSet) {
        obj.insert(QString("docs_suggested"), ::OpenAPI::toJsonValue(m_docs_suggested));
    }
    if (m_docs_suggested_interval_isSet) {
        obj.insert(QString("docs_suggested_interval"), ::OpenAPI::toJsonValue(m_docs_suggested_interval));
    }
    if (m_expiration_date_isSet) {
        obj.insert(QString("expiration_date"), ::OpenAPI::toJsonValue(m_expiration_date));
    }
    if (m_limit_type_isSet) {
        obj.insert(QString("limit_type"), ::OpenAPI::toJsonValue(m_limit_type));
    }
    if (m_polling_calls_balance_isSet) {
        obj.insert(QString("polling_calls_balance"), ::OpenAPI::toJsonValue(m_polling_calls_balance));
    }
    if (m_polling_calls_limit_isSet) {
        obj.insert(QString("polling_calls_limit"), ::OpenAPI::toJsonValue(m_polling_calls_limit));
    }
    if (m_polling_calls_limit_interval_isSet) {
        obj.insert(QString("polling_calls_limit_interval"), ::OpenAPI::toJsonValue(m_polling_calls_limit_interval));
    }
    if (m_priority_isSet) {
        obj.insert(QString("priority"), ::OpenAPI::toJsonValue(m_priority));
    }
    if (m_settings_calls_balance_isSet) {
        obj.insert(QString("settings_calls_balance"), ::OpenAPI::toJsonValue(m_settings_calls_balance));
    }
    if (m_settings_calls_limit_isSet) {
        obj.insert(QString("settings_calls_limit"), ::OpenAPI::toJsonValue(m_settings_calls_limit));
    }
    if (m_settings_calls_limit_interval_isSet) {
        obj.insert(QString("settings_calls_limit_interval"), ::OpenAPI::toJsonValue(m_settings_calls_limit_interval));
    }
    return obj;
}

qint32 OAISubscriptionBillingSection::getAppSeatsAllocated() const {
    return m_app_seats_allocated;
}
void OAISubscriptionBillingSection::setAppSeatsAllocated(const qint32 &app_seats_allocated) {
    m_app_seats_allocated = app_seats_allocated;
    m_app_seats_allocated_isSet = true;
}

bool OAISubscriptionBillingSection::is_app_seats_allocated_Set() const{
    return m_app_seats_allocated_isSet;
}

bool OAISubscriptionBillingSection::is_app_seats_allocated_Valid() const{
    return m_app_seats_allocated_isValid;
}

qint32 OAISubscriptionBillingSection::getAppSeatsPermitted() const {
    return m_app_seats_permitted;
}
void OAISubscriptionBillingSection::setAppSeatsPermitted(const qint32 &app_seats_permitted) {
    m_app_seats_permitted = app_seats_permitted;
    m_app_seats_permitted_isSet = true;
}

bool OAISubscriptionBillingSection::is_app_seats_permitted_Set() const{
    return m_app_seats_permitted_isSet;
}

bool OAISubscriptionBillingSection::is_app_seats_permitted_Valid() const{
    return m_app_seats_permitted_isValid;
}

qint32 OAISubscriptionBillingSection::getDataCallsBalance() const {
    return m_data_calls_balance;
}
void OAISubscriptionBillingSection::setDataCallsBalance(const qint32 &data_calls_balance) {
    m_data_calls_balance = data_calls_balance;
    m_data_calls_balance_isSet = true;
}

bool OAISubscriptionBillingSection::is_data_calls_balance_Set() const{
    return m_data_calls_balance_isSet;
}

bool OAISubscriptionBillingSection::is_data_calls_balance_Valid() const{
    return m_data_calls_balance_isValid;
}

qint32 OAISubscriptionBillingSection::getDataCallsLimit() const {
    return m_data_calls_limit;
}
void OAISubscriptionBillingSection::setDataCallsLimit(const qint32 &data_calls_limit) {
    m_data_calls_limit = data_calls_limit;
    m_data_calls_limit_isSet = true;
}

bool OAISubscriptionBillingSection::is_data_calls_limit_Set() const{
    return m_data_calls_limit_isSet;
}

bool OAISubscriptionBillingSection::is_data_calls_limit_Valid() const{
    return m_data_calls_limit_isValid;
}

qint32 OAISubscriptionBillingSection::getDataCallsLimitInterval() const {
    return m_data_calls_limit_interval;
}
void OAISubscriptionBillingSection::setDataCallsLimitInterval(const qint32 &data_calls_limit_interval) {
    m_data_calls_limit_interval = data_calls_limit_interval;
    m_data_calls_limit_interval_isSet = true;
}

bool OAISubscriptionBillingSection::is_data_calls_limit_interval_Set() const{
    return m_data_calls_limit_interval_isSet;
}

bool OAISubscriptionBillingSection::is_data_calls_limit_interval_Valid() const{
    return m_data_calls_limit_interval_isValid;
}

qint32 OAISubscriptionBillingSection::getDocsBalance() const {
    return m_docs_balance;
}
void OAISubscriptionBillingSection::setDocsBalance(const qint32 &docs_balance) {
    m_docs_balance = docs_balance;
    m_docs_balance_isSet = true;
}

bool OAISubscriptionBillingSection::is_docs_balance_Set() const{
    return m_docs_balance_isSet;
}

bool OAISubscriptionBillingSection::is_docs_balance_Valid() const{
    return m_docs_balance_isValid;
}

qint32 OAISubscriptionBillingSection::getDocsLimit() const {
    return m_docs_limit;
}
void OAISubscriptionBillingSection::setDocsLimit(const qint32 &docs_limit) {
    m_docs_limit = docs_limit;
    m_docs_limit_isSet = true;
}

bool OAISubscriptionBillingSection::is_docs_limit_Set() const{
    return m_docs_limit_isSet;
}

bool OAISubscriptionBillingSection::is_docs_limit_Valid() const{
    return m_docs_limit_isValid;
}

qint32 OAISubscriptionBillingSection::getDocsLimitInterval() const {
    return m_docs_limit_interval;
}
void OAISubscriptionBillingSection::setDocsLimitInterval(const qint32 &docs_limit_interval) {
    m_docs_limit_interval = docs_limit_interval;
    m_docs_limit_interval_isSet = true;
}

bool OAISubscriptionBillingSection::is_docs_limit_interval_Set() const{
    return m_docs_limit_interval_isSet;
}

bool OAISubscriptionBillingSection::is_docs_limit_interval_Valid() const{
    return m_docs_limit_interval_isValid;
}

qint32 OAISubscriptionBillingSection::getDocsSuggested() const {
    return m_docs_suggested;
}
void OAISubscriptionBillingSection::setDocsSuggested(const qint32 &docs_suggested) {
    m_docs_suggested = docs_suggested;
    m_docs_suggested_isSet = true;
}

bool OAISubscriptionBillingSection::is_docs_suggested_Set() const{
    return m_docs_suggested_isSet;
}

bool OAISubscriptionBillingSection::is_docs_suggested_Valid() const{
    return m_docs_suggested_isValid;
}

qint32 OAISubscriptionBillingSection::getDocsSuggestedInterval() const {
    return m_docs_suggested_interval;
}
void OAISubscriptionBillingSection::setDocsSuggestedInterval(const qint32 &docs_suggested_interval) {
    m_docs_suggested_interval = docs_suggested_interval;
    m_docs_suggested_interval_isSet = true;
}

bool OAISubscriptionBillingSection::is_docs_suggested_interval_Set() const{
    return m_docs_suggested_interval_isSet;
}

bool OAISubscriptionBillingSection::is_docs_suggested_interval_Valid() const{
    return m_docs_suggested_interval_isValid;
}

QString OAISubscriptionBillingSection::getExpirationDate() const {
    return m_expiration_date;
}
void OAISubscriptionBillingSection::setExpirationDate(const QString &expiration_date) {
    m_expiration_date = expiration_date;
    m_expiration_date_isSet = true;
}

bool OAISubscriptionBillingSection::is_expiration_date_Set() const{
    return m_expiration_date_isSet;
}

bool OAISubscriptionBillingSection::is_expiration_date_Valid() const{
    return m_expiration_date_isValid;
}

QString OAISubscriptionBillingSection::getLimitType() const {
    return m_limit_type;
}
void OAISubscriptionBillingSection::setLimitType(const QString &limit_type) {
    m_limit_type = limit_type;
    m_limit_type_isSet = true;
}

bool OAISubscriptionBillingSection::is_limit_type_Set() const{
    return m_limit_type_isSet;
}

bool OAISubscriptionBillingSection::is_limit_type_Valid() const{
    return m_limit_type_isValid;
}

qint32 OAISubscriptionBillingSection::getPollingCallsBalance() const {
    return m_polling_calls_balance;
}
void OAISubscriptionBillingSection::setPollingCallsBalance(const qint32 &polling_calls_balance) {
    m_polling_calls_balance = polling_calls_balance;
    m_polling_calls_balance_isSet = true;
}

bool OAISubscriptionBillingSection::is_polling_calls_balance_Set() const{
    return m_polling_calls_balance_isSet;
}

bool OAISubscriptionBillingSection::is_polling_calls_balance_Valid() const{
    return m_polling_calls_balance_isValid;
}

qint32 OAISubscriptionBillingSection::getPollingCallsLimit() const {
    return m_polling_calls_limit;
}
void OAISubscriptionBillingSection::setPollingCallsLimit(const qint32 &polling_calls_limit) {
    m_polling_calls_limit = polling_calls_limit;
    m_polling_calls_limit_isSet = true;
}

bool OAISubscriptionBillingSection::is_polling_calls_limit_Set() const{
    return m_polling_calls_limit_isSet;
}

bool OAISubscriptionBillingSection::is_polling_calls_limit_Valid() const{
    return m_polling_calls_limit_isValid;
}

qint32 OAISubscriptionBillingSection::getPollingCallsLimitInterval() const {
    return m_polling_calls_limit_interval;
}
void OAISubscriptionBillingSection::setPollingCallsLimitInterval(const qint32 &polling_calls_limit_interval) {
    m_polling_calls_limit_interval = polling_calls_limit_interval;
    m_polling_calls_limit_interval_isSet = true;
}

bool OAISubscriptionBillingSection::is_polling_calls_limit_interval_Set() const{
    return m_polling_calls_limit_interval_isSet;
}

bool OAISubscriptionBillingSection::is_polling_calls_limit_interval_Valid() const{
    return m_polling_calls_limit_interval_isValid;
}

QString OAISubscriptionBillingSection::getPriority() const {
    return m_priority;
}
void OAISubscriptionBillingSection::setPriority(const QString &priority) {
    m_priority = priority;
    m_priority_isSet = true;
}

bool OAISubscriptionBillingSection::is_priority_Set() const{
    return m_priority_isSet;
}

bool OAISubscriptionBillingSection::is_priority_Valid() const{
    return m_priority_isValid;
}

qint32 OAISubscriptionBillingSection::getSettingsCallsBalance() const {
    return m_settings_calls_balance;
}
void OAISubscriptionBillingSection::setSettingsCallsBalance(const qint32 &settings_calls_balance) {
    m_settings_calls_balance = settings_calls_balance;
    m_settings_calls_balance_isSet = true;
}

bool OAISubscriptionBillingSection::is_settings_calls_balance_Set() const{
    return m_settings_calls_balance_isSet;
}

bool OAISubscriptionBillingSection::is_settings_calls_balance_Valid() const{
    return m_settings_calls_balance_isValid;
}

qint32 OAISubscriptionBillingSection::getSettingsCallsLimit() const {
    return m_settings_calls_limit;
}
void OAISubscriptionBillingSection::setSettingsCallsLimit(const qint32 &settings_calls_limit) {
    m_settings_calls_limit = settings_calls_limit;
    m_settings_calls_limit_isSet = true;
}

bool OAISubscriptionBillingSection::is_settings_calls_limit_Set() const{
    return m_settings_calls_limit_isSet;
}

bool OAISubscriptionBillingSection::is_settings_calls_limit_Valid() const{
    return m_settings_calls_limit_isValid;
}

qint32 OAISubscriptionBillingSection::getSettingsCallsLimitInterval() const {
    return m_settings_calls_limit_interval;
}
void OAISubscriptionBillingSection::setSettingsCallsLimitInterval(const qint32 &settings_calls_limit_interval) {
    m_settings_calls_limit_interval = settings_calls_limit_interval;
    m_settings_calls_limit_interval_isSet = true;
}

bool OAISubscriptionBillingSection::is_settings_calls_limit_interval_Set() const{
    return m_settings_calls_limit_interval_isSet;
}

bool OAISubscriptionBillingSection::is_settings_calls_limit_interval_Valid() const{
    return m_settings_calls_limit_interval_isValid;
}

bool OAISubscriptionBillingSection::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_seats_allocated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_app_seats_permitted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_calls_balance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_calls_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_calls_limit_interval_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_docs_balance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_docs_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_docs_limit_interval_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_docs_suggested_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_docs_suggested_interval_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiration_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_limit_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_polling_calls_balance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_polling_calls_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_polling_calls_limit_interval_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_priority_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings_calls_balance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings_calls_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings_calls_limit_interval_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISubscriptionBillingSection::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_app_seats_allocated_isValid && m_app_seats_permitted_isValid && m_data_calls_balance_isValid && m_data_calls_limit_isValid && m_data_calls_limit_interval_isValid && m_docs_balance_isValid && m_docs_limit_isValid && m_docs_limit_interval_isValid && m_docs_suggested_isValid && m_docs_suggested_interval_isValid && m_expiration_date_isValid && m_limit_type_isValid && m_polling_calls_balance_isValid && m_polling_calls_limit_isValid && m_polling_calls_limit_interval_isValid && m_priority_isValid && m_settings_calls_balance_isValid && m_settings_calls_limit_isValid && m_settings_calls_limit_interval_isValid && true;
}

} // namespace OpenAPI
