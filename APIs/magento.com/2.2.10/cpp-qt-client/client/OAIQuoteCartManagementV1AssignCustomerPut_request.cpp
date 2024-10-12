/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQuoteCartManagementV1AssignCustomerPut_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuoteCartManagementV1AssignCustomerPut_request::OAIQuoteCartManagementV1AssignCustomerPut_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuoteCartManagementV1AssignCustomerPut_request::OAIQuoteCartManagementV1AssignCustomerPut_request() {
    this->initializeModel();
}

OAIQuoteCartManagementV1AssignCustomerPut_request::~OAIQuoteCartManagementV1AssignCustomerPut_request() {}

void OAIQuoteCartManagementV1AssignCustomerPut_request::initializeModel() {

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_store_id_isSet = false;
    m_store_id_isValid = false;
}

void OAIQuoteCartManagementV1AssignCustomerPut_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuoteCartManagementV1AssignCustomerPut_request::fromJsonObject(QJsonObject json) {

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_store_id_isValid = ::OpenAPI::fromJsonValue(m_store_id, json[QString("storeId")]);
    m_store_id_isSet = !json[QString("storeId")].isNull() && m_store_id_isValid;
}

QString OAIQuoteCartManagementV1AssignCustomerPut_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuoteCartManagementV1AssignCustomerPut_request::asJsonObject() const {
    QJsonObject obj;
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_store_id_isSet) {
        obj.insert(QString("storeId"), ::OpenAPI::toJsonValue(m_store_id));
    }
    return obj;
}

qint32 OAIQuoteCartManagementV1AssignCustomerPut_request::getCustomerId() const {
    return m_customer_id;
}
void OAIQuoteCartManagementV1AssignCustomerPut_request::setCustomerId(const qint32 &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIQuoteCartManagementV1AssignCustomerPut_request::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIQuoteCartManagementV1AssignCustomerPut_request::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

qint32 OAIQuoteCartManagementV1AssignCustomerPut_request::getStoreId() const {
    return m_store_id;
}
void OAIQuoteCartManagementV1AssignCustomerPut_request::setStoreId(const qint32 &store_id) {
    m_store_id = store_id;
    m_store_id_isSet = true;
}

bool OAIQuoteCartManagementV1AssignCustomerPut_request::is_store_id_Set() const{
    return m_store_id_isSet;
}

bool OAIQuoteCartManagementV1AssignCustomerPut_request::is_store_id_Valid() const{
    return m_store_id_isValid;
}

bool OAIQuoteCartManagementV1AssignCustomerPut_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuoteCartManagementV1AssignCustomerPut_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_customer_id_isValid && m_store_id_isValid && true;
}

} // namespace OpenAPI
