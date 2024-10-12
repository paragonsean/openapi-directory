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

#include "OAICatalogProductAttributeGroupRepositoryV1SavePost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICatalogProductAttributeGroupRepositoryV1SavePost_request::OAICatalogProductAttributeGroupRepositoryV1SavePost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICatalogProductAttributeGroupRepositoryV1SavePost_request::OAICatalogProductAttributeGroupRepositoryV1SavePost_request() {
    this->initializeModel();
}

OAICatalogProductAttributeGroupRepositoryV1SavePost_request::~OAICatalogProductAttributeGroupRepositoryV1SavePost_request() {}

void OAICatalogProductAttributeGroupRepositoryV1SavePost_request::initializeModel() {

    m_group_isSet = false;
    m_group_isValid = false;
}

void OAICatalogProductAttributeGroupRepositoryV1SavePost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICatalogProductAttributeGroupRepositoryV1SavePost_request::fromJsonObject(QJsonObject json) {

    m_group_isValid = ::OpenAPI::fromJsonValue(m_group, json[QString("group")]);
    m_group_isSet = !json[QString("group")].isNull() && m_group_isValid;
}

QString OAICatalogProductAttributeGroupRepositoryV1SavePost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICatalogProductAttributeGroupRepositoryV1SavePost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_group.isSet()) {
        obj.insert(QString("group"), ::OpenAPI::toJsonValue(m_group));
    }
    return obj;
}

OAIEav_data_attribute_group_interface OAICatalogProductAttributeGroupRepositoryV1SavePost_request::getGroup() const {
    return m_group;
}
void OAICatalogProductAttributeGroupRepositoryV1SavePost_request::setGroup(const OAIEav_data_attribute_group_interface &group) {
    m_group = group;
    m_group_isSet = true;
}

bool OAICatalogProductAttributeGroupRepositoryV1SavePost_request::is_group_Set() const{
    return m_group_isSet;
}

bool OAICatalogProductAttributeGroupRepositoryV1SavePost_request::is_group_Valid() const{
    return m_group_isValid;
}

bool OAICatalogProductAttributeGroupRepositoryV1SavePost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_group.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICatalogProductAttributeGroupRepositoryV1SavePost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_group_isValid && true;
}

} // namespace OpenAPI
