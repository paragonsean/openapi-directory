/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINewBatch.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINewBatch::OAINewBatch(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINewBatch::OAINewBatch() {
    this->initializeModel();
}

OAINewBatch::~OAINewBatch() {}

void OAINewBatch::initializeModel() {

    m_batch_name_isSet = false;
    m_batch_name_isValid = false;

    m_callback_url_isSet = false;
    m_callback_url_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_job_number_isSet = false;
    m_job_number_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAINewBatch::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINewBatch::fromJsonObject(QJsonObject json) {

    m_batch_name_isValid = ::OpenAPI::fromJsonValue(m_batch_name, json[QString("batchName")]);
    m_batch_name_isSet = !json[QString("batchName")].isNull() && m_batch_name_isValid;

    m_callback_url_isValid = ::OpenAPI::fromJsonValue(m_callback_url, json[QString("callbackUrl")]);
    m_callback_url_isSet = !json[QString("callbackUrl")].isNull() && m_callback_url_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_job_number_isValid = ::OpenAPI::fromJsonValue(m_job_number, json[QString("jobNumber")]);
    m_job_number_isSet = !json[QString("jobNumber")].isNull() && m_job_number_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAINewBatch::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINewBatch::asJsonObject() const {
    QJsonObject obj;
    if (m_batch_name_isSet) {
        obj.insert(QString("batchName"), ::OpenAPI::toJsonValue(m_batch_name));
    }
    if (m_callback_url_isSet) {
        obj.insert(QString("callbackUrl"), ::OpenAPI::toJsonValue(m_callback_url));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_job_number_isSet) {
        obj.insert(QString("jobNumber"), ::OpenAPI::toJsonValue(m_job_number));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAINewBatch::getBatchName() const {
    return m_batch_name;
}
void OAINewBatch::setBatchName(const QString &batch_name) {
    m_batch_name = batch_name;
    m_batch_name_isSet = true;
}

bool OAINewBatch::is_batch_name_Set() const{
    return m_batch_name_isSet;
}

bool OAINewBatch::is_batch_name_Valid() const{
    return m_batch_name_isValid;
}

QString OAINewBatch::getCallbackUrl() const {
    return m_callback_url;
}
void OAINewBatch::setCallbackUrl(const QString &callback_url) {
    m_callback_url = callback_url;
    m_callback_url_isSet = true;
}

bool OAINewBatch::is_callback_url_Set() const{
    return m_callback_url_isSet;
}

bool OAINewBatch::is_callback_url_Valid() const{
    return m_callback_url_isValid;
}

QString OAINewBatch::getCurrency() const {
    return m_currency;
}
void OAINewBatch::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAINewBatch::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAINewBatch::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAINewBatch::getJobNumber() const {
    return m_job_number;
}
void OAINewBatch::setJobNumber(const QString &job_number) {
    m_job_number = job_number;
    m_job_number_isSet = true;
}

bool OAINewBatch::is_job_number_Set() const{
    return m_job_number_isSet;
}

bool OAINewBatch::is_job_number_Valid() const{
    return m_job_number_isValid;
}

QString OAINewBatch::getType() const {
    return m_type;
}
void OAINewBatch::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAINewBatch::is_type_Set() const{
    return m_type_isSet;
}

bool OAINewBatch::is_type_Valid() const{
    return m_type_isValid;
}

bool OAINewBatch::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_batch_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_callback_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINewBatch::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
