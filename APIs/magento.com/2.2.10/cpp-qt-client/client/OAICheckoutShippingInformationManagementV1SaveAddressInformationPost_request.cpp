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

#include "OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request() {
    this->initializeModel();
}

OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::~OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request() {}

void OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::initializeModel() {

    m_address_information_isSet = false;
    m_address_information_isValid = false;
}

void OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::fromJsonObject(QJsonObject json) {

    m_address_information_isValid = ::OpenAPI::fromJsonValue(m_address_information, json[QString("addressInformation")]);
    m_address_information_isSet = !json[QString("addressInformation")].isNull() && m_address_information_isValid;
}

QString OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_address_information.isSet()) {
        obj.insert(QString("addressInformation"), ::OpenAPI::toJsonValue(m_address_information));
    }
    return obj;
}

OAICheckout_data_shipping_information_interface OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::getAddressInformation() const {
    return m_address_information;
}
void OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::setAddressInformation(const OAICheckout_data_shipping_information_interface &address_information) {
    m_address_information = address_information;
    m_address_information_isSet = true;
}

bool OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::is_address_information_Set() const{
    return m_address_information_isSet;
}

bool OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::is_address_information_Valid() const{
    return m_address_information_isValid;
}

bool OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_information.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICheckoutShippingInformationManagementV1SaveAddressInformationPost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_address_information_isValid && true;
}

} // namespace OpenAPI
