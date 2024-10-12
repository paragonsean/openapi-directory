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

#include "OAICatalogProductLinkManagementV1SetProductLinksPost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICatalogProductLinkManagementV1SetProductLinksPost_request::OAICatalogProductLinkManagementV1SetProductLinksPost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICatalogProductLinkManagementV1SetProductLinksPost_request::OAICatalogProductLinkManagementV1SetProductLinksPost_request() {
    this->initializeModel();
}

OAICatalogProductLinkManagementV1SetProductLinksPost_request::~OAICatalogProductLinkManagementV1SetProductLinksPost_request() {}

void OAICatalogProductLinkManagementV1SetProductLinksPost_request::initializeModel() {

    m_items_isSet = false;
    m_items_isValid = false;
}

void OAICatalogProductLinkManagementV1SetProductLinksPost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICatalogProductLinkManagementV1SetProductLinksPost_request::fromJsonObject(QJsonObject json) {

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;
}

QString OAICatalogProductLinkManagementV1SetProductLinksPost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICatalogProductLinkManagementV1SetProductLinksPost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    return obj;
}

QList<OAICatalog_data_product_link_interface> OAICatalogProductLinkManagementV1SetProductLinksPost_request::getItems() const {
    return m_items;
}
void OAICatalogProductLinkManagementV1SetProductLinksPost_request::setItems(const QList<OAICatalog_data_product_link_interface> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAICatalogProductLinkManagementV1SetProductLinksPost_request::is_items_Set() const{
    return m_items_isSet;
}

bool OAICatalogProductLinkManagementV1SetProductLinksPost_request::is_items_Valid() const{
    return m_items_isValid;
}

bool OAICatalogProductLinkManagementV1SetProductLinksPost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICatalogProductLinkManagementV1SetProductLinksPost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_items_isValid && true;
}

} // namespace OpenAPI
