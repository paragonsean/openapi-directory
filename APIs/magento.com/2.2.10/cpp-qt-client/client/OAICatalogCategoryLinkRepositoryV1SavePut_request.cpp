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

#include "OAICatalogCategoryLinkRepositoryV1SavePut_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICatalogCategoryLinkRepositoryV1SavePut_request::OAICatalogCategoryLinkRepositoryV1SavePut_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICatalogCategoryLinkRepositoryV1SavePut_request::OAICatalogCategoryLinkRepositoryV1SavePut_request() {
    this->initializeModel();
}

OAICatalogCategoryLinkRepositoryV1SavePut_request::~OAICatalogCategoryLinkRepositoryV1SavePut_request() {}

void OAICatalogCategoryLinkRepositoryV1SavePut_request::initializeModel() {

    m_product_link_isSet = false;
    m_product_link_isValid = false;
}

void OAICatalogCategoryLinkRepositoryV1SavePut_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICatalogCategoryLinkRepositoryV1SavePut_request::fromJsonObject(QJsonObject json) {

    m_product_link_isValid = ::OpenAPI::fromJsonValue(m_product_link, json[QString("productLink")]);
    m_product_link_isSet = !json[QString("productLink")].isNull() && m_product_link_isValid;
}

QString OAICatalogCategoryLinkRepositoryV1SavePut_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICatalogCategoryLinkRepositoryV1SavePut_request::asJsonObject() const {
    QJsonObject obj;
    if (m_product_link.isSet()) {
        obj.insert(QString("productLink"), ::OpenAPI::toJsonValue(m_product_link));
    }
    return obj;
}

OAICatalog_data_category_product_link_interface OAICatalogCategoryLinkRepositoryV1SavePut_request::getProductLink() const {
    return m_product_link;
}
void OAICatalogCategoryLinkRepositoryV1SavePut_request::setProductLink(const OAICatalog_data_category_product_link_interface &product_link) {
    m_product_link = product_link;
    m_product_link_isSet = true;
}

bool OAICatalogCategoryLinkRepositoryV1SavePut_request::is_product_link_Set() const{
    return m_product_link_isSet;
}

bool OAICatalogCategoryLinkRepositoryV1SavePut_request::is_product_link_Valid() const{
    return m_product_link_isValid;
}

bool OAICatalogCategoryLinkRepositoryV1SavePut_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_product_link.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICatalogCategoryLinkRepositoryV1SavePut_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_product_link_isValid && true;
}

} // namespace OpenAPI
