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

#include "OAICatalogProductAttributeOptionManagementV1AddPost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICatalogProductAttributeOptionManagementV1AddPost_request::OAICatalogProductAttributeOptionManagementV1AddPost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICatalogProductAttributeOptionManagementV1AddPost_request::OAICatalogProductAttributeOptionManagementV1AddPost_request() {
    this->initializeModel();
}

OAICatalogProductAttributeOptionManagementV1AddPost_request::~OAICatalogProductAttributeOptionManagementV1AddPost_request() {}

void OAICatalogProductAttributeOptionManagementV1AddPost_request::initializeModel() {

    m_option_isSet = false;
    m_option_isValid = false;
}

void OAICatalogProductAttributeOptionManagementV1AddPost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICatalogProductAttributeOptionManagementV1AddPost_request::fromJsonObject(QJsonObject json) {

    m_option_isValid = ::OpenAPI::fromJsonValue(m_option, json[QString("option")]);
    m_option_isSet = !json[QString("option")].isNull() && m_option_isValid;
}

QString OAICatalogProductAttributeOptionManagementV1AddPost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICatalogProductAttributeOptionManagementV1AddPost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_option.isSet()) {
        obj.insert(QString("option"), ::OpenAPI::toJsonValue(m_option));
    }
    return obj;
}

OAIEav_data_attribute_option_interface OAICatalogProductAttributeOptionManagementV1AddPost_request::getOption() const {
    return m_option;
}
void OAICatalogProductAttributeOptionManagementV1AddPost_request::setOption(const OAIEav_data_attribute_option_interface &option) {
    m_option = option;
    m_option_isSet = true;
}

bool OAICatalogProductAttributeOptionManagementV1AddPost_request::is_option_Set() const{
    return m_option_isSet;
}

bool OAICatalogProductAttributeOptionManagementV1AddPost_request::is_option_Valid() const{
    return m_option_isValid;
}

bool OAICatalogProductAttributeOptionManagementV1AddPost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_option.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICatalogProductAttributeOptionManagementV1AddPost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_option_isValid && true;
}

} // namespace OpenAPI
