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

#include "OAICustomerAccountManagementV1ValidatePut_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomerAccountManagementV1ValidatePut_request::OAICustomerAccountManagementV1ValidatePut_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomerAccountManagementV1ValidatePut_request::OAICustomerAccountManagementV1ValidatePut_request() {
    this->initializeModel();
}

OAICustomerAccountManagementV1ValidatePut_request::~OAICustomerAccountManagementV1ValidatePut_request() {}

void OAICustomerAccountManagementV1ValidatePut_request::initializeModel() {

    m_customer_isSet = false;
    m_customer_isValid = false;
}

void OAICustomerAccountManagementV1ValidatePut_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomerAccountManagementV1ValidatePut_request::fromJsonObject(QJsonObject json) {

    m_customer_isValid = ::OpenAPI::fromJsonValue(m_customer, json[QString("customer")]);
    m_customer_isSet = !json[QString("customer")].isNull() && m_customer_isValid;
}

QString OAICustomerAccountManagementV1ValidatePut_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomerAccountManagementV1ValidatePut_request::asJsonObject() const {
    QJsonObject obj;
    if (m_customer.isSet()) {
        obj.insert(QString("customer"), ::OpenAPI::toJsonValue(m_customer));
    }
    return obj;
}

OAICustomer_data_customer_interface OAICustomerAccountManagementV1ValidatePut_request::getCustomer() const {
    return m_customer;
}
void OAICustomerAccountManagementV1ValidatePut_request::setCustomer(const OAICustomer_data_customer_interface &customer) {
    m_customer = customer;
    m_customer_isSet = true;
}

bool OAICustomerAccountManagementV1ValidatePut_request::is_customer_Set() const{
    return m_customer_isSet;
}

bool OAICustomerAccountManagementV1ValidatePut_request::is_customer_Valid() const{
    return m_customer_isValid;
}

bool OAICustomerAccountManagementV1ValidatePut_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_customer.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomerAccountManagementV1ValidatePut_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_customer_isValid && true;
}

} // namespace OpenAPI
