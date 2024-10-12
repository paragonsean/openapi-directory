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

#include "OAICustomerAccountManagementV1IsEmailAvailablePost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomerAccountManagementV1IsEmailAvailablePost_request::OAICustomerAccountManagementV1IsEmailAvailablePost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomerAccountManagementV1IsEmailAvailablePost_request::OAICustomerAccountManagementV1IsEmailAvailablePost_request() {
    this->initializeModel();
}

OAICustomerAccountManagementV1IsEmailAvailablePost_request::~OAICustomerAccountManagementV1IsEmailAvailablePost_request() {}

void OAICustomerAccountManagementV1IsEmailAvailablePost_request::initializeModel() {

    m_customer_email_isSet = false;
    m_customer_email_isValid = false;

    m_website_id_isSet = false;
    m_website_id_isValid = false;
}

void OAICustomerAccountManagementV1IsEmailAvailablePost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomerAccountManagementV1IsEmailAvailablePost_request::fromJsonObject(QJsonObject json) {

    m_customer_email_isValid = ::OpenAPI::fromJsonValue(m_customer_email, json[QString("customerEmail")]);
    m_customer_email_isSet = !json[QString("customerEmail")].isNull() && m_customer_email_isValid;

    m_website_id_isValid = ::OpenAPI::fromJsonValue(m_website_id, json[QString("websiteId")]);
    m_website_id_isSet = !json[QString("websiteId")].isNull() && m_website_id_isValid;
}

QString OAICustomerAccountManagementV1IsEmailAvailablePost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomerAccountManagementV1IsEmailAvailablePost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_customer_email_isSet) {
        obj.insert(QString("customerEmail"), ::OpenAPI::toJsonValue(m_customer_email));
    }
    if (m_website_id_isSet) {
        obj.insert(QString("websiteId"), ::OpenAPI::toJsonValue(m_website_id));
    }
    return obj;
}

QString OAICustomerAccountManagementV1IsEmailAvailablePost_request::getCustomerEmail() const {
    return m_customer_email;
}
void OAICustomerAccountManagementV1IsEmailAvailablePost_request::setCustomerEmail(const QString &customer_email) {
    m_customer_email = customer_email;
    m_customer_email_isSet = true;
}

bool OAICustomerAccountManagementV1IsEmailAvailablePost_request::is_customer_email_Set() const{
    return m_customer_email_isSet;
}

bool OAICustomerAccountManagementV1IsEmailAvailablePost_request::is_customer_email_Valid() const{
    return m_customer_email_isValid;
}

qint32 OAICustomerAccountManagementV1IsEmailAvailablePost_request::getWebsiteId() const {
    return m_website_id;
}
void OAICustomerAccountManagementV1IsEmailAvailablePost_request::setWebsiteId(const qint32 &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAICustomerAccountManagementV1IsEmailAvailablePost_request::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAICustomerAccountManagementV1IsEmailAvailablePost_request::is_website_id_Valid() const{
    return m_website_id_isValid;
}

bool OAICustomerAccountManagementV1IsEmailAvailablePost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_customer_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomerAccountManagementV1IsEmailAvailablePost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_customer_email_isValid && true;
}

} // namespace OpenAPI
