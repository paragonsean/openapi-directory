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

#include "OAIProductPriceUpdate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductPriceUpdate::OAIProductPriceUpdate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductPriceUpdate::OAIProductPriceUpdate() {
    this->initializeModel();
}

OAIProductPriceUpdate::~OAIProductPriceUpdate() {}

void OAIProductPriceUpdate::initializeModel() {

    m_group_prices_isSet = false;
    m_group_prices_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;
}

void OAIProductPriceUpdate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductPriceUpdate::fromJsonObject(QJsonObject json) {

    m_group_prices_isValid = ::OpenAPI::fromJsonValue(m_group_prices, json[QString("group_prices")]);
    m_group_prices_isSet = !json[QString("group_prices")].isNull() && m_group_prices_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("product_id")]);
    m_product_id_isSet = !json[QString("product_id")].isNull() && m_product_id_isValid;
}

QString OAIProductPriceUpdate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductPriceUpdate::asJsonObject() const {
    QJsonObject obj;
    if (m_group_prices.size() > 0) {
        obj.insert(QString("group_prices"), ::OpenAPI::toJsonValue(m_group_prices));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("product_id"), ::OpenAPI::toJsonValue(m_product_id));
    }
    return obj;
}

QList<OAIProductPriceUpdate_group_prices_inner> OAIProductPriceUpdate::getGroupPrices() const {
    return m_group_prices;
}
void OAIProductPriceUpdate::setGroupPrices(const QList<OAIProductPriceUpdate_group_prices_inner> &group_prices) {
    m_group_prices = group_prices;
    m_group_prices_isSet = true;
}

bool OAIProductPriceUpdate::is_group_prices_Set() const{
    return m_group_prices_isSet;
}

bool OAIProductPriceUpdate::is_group_prices_Valid() const{
    return m_group_prices_isValid;
}

QString OAIProductPriceUpdate::getProductId() const {
    return m_product_id;
}
void OAIProductPriceUpdate::setProductId(const QString &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIProductPriceUpdate::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIProductPriceUpdate::is_product_id_Valid() const{
    return m_product_id_isValid;
}

bool OAIProductPriceUpdate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_group_prices.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductPriceUpdate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
