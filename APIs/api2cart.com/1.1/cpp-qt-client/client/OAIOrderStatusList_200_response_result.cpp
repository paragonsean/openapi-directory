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

#include "OAIOrderStatusList_200_response_result.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrderStatusList_200_response_result::OAIOrderStatusList_200_response_result(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrderStatusList_200_response_result::OAIOrderStatusList_200_response_result() {
    this->initializeModel();
}

OAIOrderStatusList_200_response_result::~OAIOrderStatusList_200_response_result() {}

void OAIOrderStatusList_200_response_result::initializeModel() {

    m_cart_order_statuses_isSet = false;
    m_cart_order_statuses_isValid = false;
}

void OAIOrderStatusList_200_response_result::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrderStatusList_200_response_result::fromJsonObject(QJsonObject json) {

    m_cart_order_statuses_isValid = ::OpenAPI::fromJsonValue(m_cart_order_statuses, json[QString("cart_order_statuses")]);
    m_cart_order_statuses_isSet = !json[QString("cart_order_statuses")].isNull() && m_cart_order_statuses_isValid;
}

QString OAIOrderStatusList_200_response_result::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrderStatusList_200_response_result::asJsonObject() const {
    QJsonObject obj;
    if (m_cart_order_statuses.size() > 0) {
        obj.insert(QString("cart_order_statuses"), ::OpenAPI::toJsonValue(m_cart_order_statuses));
    }
    return obj;
}

QList<OAIOrderFinancialStatusList_200_response_result_order_financial_statuses_inner> OAIOrderStatusList_200_response_result::getCartOrderStatuses() const {
    return m_cart_order_statuses;
}
void OAIOrderStatusList_200_response_result::setCartOrderStatuses(const QList<OAIOrderFinancialStatusList_200_response_result_order_financial_statuses_inner> &cart_order_statuses) {
    m_cart_order_statuses = cart_order_statuses;
    m_cart_order_statuses_isSet = true;
}

bool OAIOrderStatusList_200_response_result::is_cart_order_statuses_Set() const{
    return m_cart_order_statuses_isSet;
}

bool OAIOrderStatusList_200_response_result::is_cart_order_statuses_Valid() const{
    return m_cart_order_statuses_isValid;
}

bool OAIOrderStatusList_200_response_result::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cart_order_statuses.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrderStatusList_200_response_result::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
