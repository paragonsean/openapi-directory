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

#include "OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request() {
    this->initializeModel();
}

OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::~OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request() {}

void OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::initializeModel() {

    m_gift_card_account_data_isSet = false;
    m_gift_card_account_data_isValid = false;
}

void OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::fromJsonObject(QJsonObject json) {

    m_gift_card_account_data_isValid = ::OpenAPI::fromJsonValue(m_gift_card_account_data, json[QString("giftCardAccountData")]);
    m_gift_card_account_data_isSet = !json[QString("giftCardAccountData")].isNull() && m_gift_card_account_data_isValid;
}

QString OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_gift_card_account_data.isSet()) {
        obj.insert(QString("giftCardAccountData"), ::OpenAPI::toJsonValue(m_gift_card_account_data));
    }
    return obj;
}

OAIGift_card_account_data_gift_card_account_interface OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::getGiftCardAccountData() const {
    return m_gift_card_account_data;
}
void OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::setGiftCardAccountData(const OAIGift_card_account_data_gift_card_account_interface &gift_card_account_data) {
    m_gift_card_account_data = gift_card_account_data;
    m_gift_card_account_data_isSet = true;
}

bool OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::is_gift_card_account_data_Set() const{
    return m_gift_card_account_data_isSet;
}

bool OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::is_gift_card_account_data_Valid() const{
    return m_gift_card_account_data_isValid;
}

bool OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_gift_card_account_data.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGiftCardAccountGuestGiftCardAccountManagementV1AddGiftCardPost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_gift_card_account_data_isValid && true;
}

} // namespace OpenAPI
