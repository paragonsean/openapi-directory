/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHoldInfoObject.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHoldInfoObject::OAIHoldInfoObject(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHoldInfoObject::OAIHoldInfoObject() {
    this->initializeModel();
}

OAIHoldInfoObject::~OAIHoldInfoObject() {}

void OAIHoldInfoObject::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_foreign_amount_isSet = false;
    m_foreign_amount_isValid = false;
}

void OAIHoldInfoObject::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHoldInfoObject::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_foreign_amount_isValid = ::OpenAPI::fromJsonValue(m_foreign_amount, json[QString("foreignAmount")]);
    m_foreign_amount_isSet = !json[QString("foreignAmount")].isNull() && m_foreign_amount_isValid;
}

QString OAIHoldInfoObject::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHoldInfoObject::asJsonObject() const {
    QJsonObject obj;
    if (m_amount.isSet()) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_foreign_amount.isSet()) {
        obj.insert(QString("foreignAmount"), ::OpenAPI::toJsonValue(m_foreign_amount));
    }
    return obj;
}

OAIMoneyObject OAIHoldInfoObject::getAmount() const {
    return m_amount;
}
void OAIHoldInfoObject::setAmount(const OAIMoneyObject &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIHoldInfoObject::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIHoldInfoObject::is_amount_Valid() const{
    return m_amount_isValid;
}

OAIMoneyObject OAIHoldInfoObject::getForeignAmount() const {
    return m_foreign_amount;
}
void OAIHoldInfoObject::setForeignAmount(const OAIMoneyObject &foreign_amount) {
    m_foreign_amount = foreign_amount;
    m_foreign_amount_isSet = true;
}

bool OAIHoldInfoObject::is_foreign_amount_Set() const{
    return m_foreign_amount_isSet;
}

bool OAIHoldInfoObject::is_foreign_amount_Valid() const{
    return m_foreign_amount_isValid;
}

bool OAIHoldInfoObject::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_foreign_amount.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHoldInfoObject::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_amount_isValid && m_foreign_amount_isValid && true;
}

} // namespace OpenAPI
