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

#include "OAIConfigurableProductOptionRepositoryV1SavePost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConfigurableProductOptionRepositoryV1SavePost_request::OAIConfigurableProductOptionRepositoryV1SavePost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConfigurableProductOptionRepositoryV1SavePost_request::OAIConfigurableProductOptionRepositoryV1SavePost_request() {
    this->initializeModel();
}

OAIConfigurableProductOptionRepositoryV1SavePost_request::~OAIConfigurableProductOptionRepositoryV1SavePost_request() {}

void OAIConfigurableProductOptionRepositoryV1SavePost_request::initializeModel() {

    m_option_isSet = false;
    m_option_isValid = false;
}

void OAIConfigurableProductOptionRepositoryV1SavePost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConfigurableProductOptionRepositoryV1SavePost_request::fromJsonObject(QJsonObject json) {

    m_option_isValid = ::OpenAPI::fromJsonValue(m_option, json[QString("option")]);
    m_option_isSet = !json[QString("option")].isNull() && m_option_isValid;
}

QString OAIConfigurableProductOptionRepositoryV1SavePost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConfigurableProductOptionRepositoryV1SavePost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_option.isSet()) {
        obj.insert(QString("option"), ::OpenAPI::toJsonValue(m_option));
    }
    return obj;
}

OAIConfigurable_product_data_option_interface OAIConfigurableProductOptionRepositoryV1SavePost_request::getOption() const {
    return m_option;
}
void OAIConfigurableProductOptionRepositoryV1SavePost_request::setOption(const OAIConfigurable_product_data_option_interface &option) {
    m_option = option;
    m_option_isSet = true;
}

bool OAIConfigurableProductOptionRepositoryV1SavePost_request::is_option_Set() const{
    return m_option_isSet;
}

bool OAIConfigurableProductOptionRepositoryV1SavePost_request::is_option_Valid() const{
    return m_option_isValid;
}

bool OAIConfigurableProductOptionRepositoryV1SavePost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_option.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConfigurableProductOptionRepositoryV1SavePost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_option_isValid && true;
}

} // namespace OpenAPI
