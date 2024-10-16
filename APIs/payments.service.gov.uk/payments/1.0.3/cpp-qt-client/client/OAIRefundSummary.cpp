/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRefundSummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRefundSummary::OAIRefundSummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRefundSummary::OAIRefundSummary() {
    this->initializeModel();
}

OAIRefundSummary::~OAIRefundSummary() {}

void OAIRefundSummary::initializeModel() {

    m_amount_available_isSet = false;
    m_amount_available_isValid = false;

    m_amount_submitted_isSet = false;
    m_amount_submitted_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIRefundSummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRefundSummary::fromJsonObject(QJsonObject json) {

    m_amount_available_isValid = ::OpenAPI::fromJsonValue(m_amount_available, json[QString("amount_available")]);
    m_amount_available_isSet = !json[QString("amount_available")].isNull() && m_amount_available_isValid;

    m_amount_submitted_isValid = ::OpenAPI::fromJsonValue(m_amount_submitted, json[QString("amount_submitted")]);
    m_amount_submitted_isSet = !json[QString("amount_submitted")].isNull() && m_amount_submitted_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIRefundSummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRefundSummary::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_available_isSet) {
        obj.insert(QString("amount_available"), ::OpenAPI::toJsonValue(m_amount_available));
    }
    if (m_amount_submitted_isSet) {
        obj.insert(QString("amount_submitted"), ::OpenAPI::toJsonValue(m_amount_submitted));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

qint64 OAIRefundSummary::getAmountAvailable() const {
    return m_amount_available;
}
void OAIRefundSummary::setAmountAvailable(const qint64 &amount_available) {
    m_amount_available = amount_available;
    m_amount_available_isSet = true;
}

bool OAIRefundSummary::is_amount_available_Set() const{
    return m_amount_available_isSet;
}

bool OAIRefundSummary::is_amount_available_Valid() const{
    return m_amount_available_isValid;
}

qint64 OAIRefundSummary::getAmountSubmitted() const {
    return m_amount_submitted;
}
void OAIRefundSummary::setAmountSubmitted(const qint64 &amount_submitted) {
    m_amount_submitted = amount_submitted;
    m_amount_submitted_isSet = true;
}

bool OAIRefundSummary::is_amount_submitted_Set() const{
    return m_amount_submitted_isSet;
}

bool OAIRefundSummary::is_amount_submitted_Valid() const{
    return m_amount_submitted_isValid;
}

QString OAIRefundSummary::getStatus() const {
    return m_status;
}
void OAIRefundSummary::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIRefundSummary::is_status_Set() const{
    return m_status_isSet;
}

bool OAIRefundSummary::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIRefundSummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_submitted_isSet) {
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

bool OAIRefundSummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
