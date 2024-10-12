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

#include "OAICashbackObject.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICashbackObject::OAICashbackObject(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICashbackObject::OAICashbackObject() {
    this->initializeModel();
}

OAICashbackObject::~OAICashbackObject() {}

void OAICashbackObject::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;
}

void OAICashbackObject::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICashbackObject::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;
}

QString OAICashbackObject::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICashbackObject::asJsonObject() const {
    QJsonObject obj;
    if (m_amount.isSet()) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    return obj;
}

OAIMoneyObject OAICashbackObject::getAmount() const {
    return m_amount;
}
void OAICashbackObject::setAmount(const OAIMoneyObject &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAICashbackObject::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAICashbackObject::is_amount_Valid() const{
    return m_amount_isValid;
}

QString OAICashbackObject::getDescription() const {
    return m_description;
}
void OAICashbackObject::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAICashbackObject::is_description_Set() const{
    return m_description_isSet;
}

bool OAICashbackObject::is_description_Valid() const{
    return m_description_isValid;
}

bool OAICashbackObject::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICashbackObject::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_amount_isValid && m_description_isValid && true;
}

} // namespace OpenAPI
