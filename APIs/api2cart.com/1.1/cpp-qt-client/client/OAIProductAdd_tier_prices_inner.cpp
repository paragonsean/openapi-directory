/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProductAdd_tier_prices_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductAdd_tier_prices_inner::OAIProductAdd_tier_prices_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductAdd_tier_prices_inner::OAIProductAdd_tier_prices_inner() {
    this->initializeModel();
}

OAIProductAdd_tier_prices_inner::~OAIProductAdd_tier_prices_inner() {}

void OAIProductAdd_tier_prices_inner::initializeModel() {

    m_price_isSet = false;
    m_price_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;
}

void OAIProductAdd_tier_prices_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductAdd_tier_prices_inner::fromJsonObject(QJsonObject json) {

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;
}

QString OAIProductAdd_tier_prices_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductAdd_tier_prices_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    return obj;
}

double OAIProductAdd_tier_prices_inner::getPrice() const {
    return m_price;
}
void OAIProductAdd_tier_prices_inner::setPrice(const double &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIProductAdd_tier_prices_inner::is_price_Set() const{
    return m_price_isSet;
}

bool OAIProductAdd_tier_prices_inner::is_price_Valid() const{
    return m_price_isValid;
}

double OAIProductAdd_tier_prices_inner::getQuantity() const {
    return m_quantity;
}
void OAIProductAdd_tier_prices_inner::setQuantity(const double &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIProductAdd_tier_prices_inner::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIProductAdd_tier_prices_inner::is_quantity_Valid() const{
    return m_quantity_isValid;
}

bool OAIProductAdd_tier_prices_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductAdd_tier_prices_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
