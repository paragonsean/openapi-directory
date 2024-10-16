/**
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetTokenHoldersResponse_holders_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetTokenHoldersResponse_holders_inner::OAIGetTokenHoldersResponse_holders_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetTokenHoldersResponse_holders_inner::OAIGetTokenHoldersResponse_holders_inner() {
    this->initializeModel();
}

OAIGetTokenHoldersResponse_holders_inner::~OAIGetTokenHoldersResponse_holders_inner() {}

void OAIGetTokenHoldersResponse_holders_inner::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_amount_isSet = false;
    m_amount_isValid = false;
}

void OAIGetTokenHoldersResponse_holders_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetTokenHoldersResponse_holders_inner::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;
}

QString OAIGetTokenHoldersResponse_holders_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetTokenHoldersResponse_holders_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    return obj;
}

QString OAIGetTokenHoldersResponse_holders_inner::getAddress() const {
    return m_address;
}
void OAIGetTokenHoldersResponse_holders_inner::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIGetTokenHoldersResponse_holders_inner::is_address_Set() const{
    return m_address_isSet;
}

bool OAIGetTokenHoldersResponse_holders_inner::is_address_Valid() const{
    return m_address_isValid;
}

double OAIGetTokenHoldersResponse_holders_inner::getAmount() const {
    return m_amount;
}
void OAIGetTokenHoldersResponse_holders_inner::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIGetTokenHoldersResponse_holders_inner::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIGetTokenHoldersResponse_holders_inner::is_amount_Valid() const{
    return m_amount_isValid;
}

bool OAIGetTokenHoldersResponse_holders_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetTokenHoldersResponse_holders_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
