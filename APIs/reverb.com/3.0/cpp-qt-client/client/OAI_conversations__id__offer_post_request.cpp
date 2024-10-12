/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_conversations__id__offer_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_conversations__id__offer_post_request::OAI_conversations__id__offer_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_conversations__id__offer_post_request::OAI_conversations__id__offer_post_request() {
    this->initializeModel();
}

OAI_conversations__id__offer_post_request::~OAI_conversations__id__offer_post_request() {}

void OAI_conversations__id__offer_post_request::initializeModel() {

    m_message_isSet = false;
    m_message_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_shipping_price_isSet = false;
    m_shipping_price_isValid = false;
}

void OAI_conversations__id__offer_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_conversations__id__offer_post_request::fromJsonObject(QJsonObject json) {

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_shipping_price_isValid = ::OpenAPI::fromJsonValue(m_shipping_price, json[QString("shipping_price")]);
    m_shipping_price_isSet = !json[QString("shipping_price")].isNull() && m_shipping_price_isValid;
}

QString OAI_conversations__id__offer_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_conversations__id__offer_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_shipping_price_isSet) {
        obj.insert(QString("shipping_price"), ::OpenAPI::toJsonValue(m_shipping_price));
    }
    return obj;
}

QString OAI_conversations__id__offer_post_request::getMessage() const {
    return m_message;
}
void OAI_conversations__id__offer_post_request::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAI_conversations__id__offer_post_request::is_message_Set() const{
    return m_message_isSet;
}

bool OAI_conversations__id__offer_post_request::is_message_Valid() const{
    return m_message_isValid;
}

QString OAI_conversations__id__offer_post_request::getPrice() const {
    return m_price;
}
void OAI_conversations__id__offer_post_request::setPrice(const QString &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAI_conversations__id__offer_post_request::is_price_Set() const{
    return m_price_isSet;
}

bool OAI_conversations__id__offer_post_request::is_price_Valid() const{
    return m_price_isValid;
}

QString OAI_conversations__id__offer_post_request::getShippingPrice() const {
    return m_shipping_price;
}
void OAI_conversations__id__offer_post_request::setShippingPrice(const QString &shipping_price) {
    m_shipping_price = shipping_price;
    m_shipping_price_isSet = true;
}

bool OAI_conversations__id__offer_post_request::is_shipping_price_Set() const{
    return m_shipping_price_isSet;
}

bool OAI_conversations__id__offer_post_request::is_shipping_price_Valid() const{
    return m_shipping_price_isValid;
}

bool OAI_conversations__id__offer_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_price_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_conversations__id__offer_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_price_isValid && true;
}

} // namespace OpenAPI
