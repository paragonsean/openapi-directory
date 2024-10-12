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

#include "OAIOrderFulfillmentStatusList_200_response_result.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrderFulfillmentStatusList_200_response_result::OAIOrderFulfillmentStatusList_200_response_result(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrderFulfillmentStatusList_200_response_result::OAIOrderFulfillmentStatusList_200_response_result() {
    this->initializeModel();
}

OAIOrderFulfillmentStatusList_200_response_result::~OAIOrderFulfillmentStatusList_200_response_result() {}

void OAIOrderFulfillmentStatusList_200_response_result::initializeModel() {

    m_order_fulfillment_statuses_isSet = false;
    m_order_fulfillment_statuses_isValid = false;
}

void OAIOrderFulfillmentStatusList_200_response_result::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrderFulfillmentStatusList_200_response_result::fromJsonObject(QJsonObject json) {

    m_order_fulfillment_statuses_isValid = ::OpenAPI::fromJsonValue(m_order_fulfillment_statuses, json[QString("order_fulfillment_statuses")]);
    m_order_fulfillment_statuses_isSet = !json[QString("order_fulfillment_statuses")].isNull() && m_order_fulfillment_statuses_isValid;
}

QString OAIOrderFulfillmentStatusList_200_response_result::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrderFulfillmentStatusList_200_response_result::asJsonObject() const {
    QJsonObject obj;
    if (m_order_fulfillment_statuses.size() > 0) {
        obj.insert(QString("order_fulfillment_statuses"), ::OpenAPI::toJsonValue(m_order_fulfillment_statuses));
    }
    return obj;
}

QList<OAIOrderFinancialStatusList_200_response_result_order_financial_statuses_inner> OAIOrderFulfillmentStatusList_200_response_result::getOrderFulfillmentStatuses() const {
    return m_order_fulfillment_statuses;
}
void OAIOrderFulfillmentStatusList_200_response_result::setOrderFulfillmentStatuses(const QList<OAIOrderFinancialStatusList_200_response_result_order_financial_statuses_inner> &order_fulfillment_statuses) {
    m_order_fulfillment_statuses = order_fulfillment_statuses;
    m_order_fulfillment_statuses_isSet = true;
}

bool OAIOrderFulfillmentStatusList_200_response_result::is_order_fulfillment_statuses_Set() const{
    return m_order_fulfillment_statuses_isSet;
}

bool OAIOrderFulfillmentStatusList_200_response_result::is_order_fulfillment_statuses_Valid() const{
    return m_order_fulfillment_statuses_isValid;
}

bool OAIOrderFulfillmentStatusList_200_response_result::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_order_fulfillment_statuses.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrderFulfillmentStatusList_200_response_result::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
