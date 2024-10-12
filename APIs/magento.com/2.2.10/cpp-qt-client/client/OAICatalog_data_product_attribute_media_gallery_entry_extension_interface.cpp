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

#include "OAICatalog_data_product_attribute_media_gallery_entry_extension_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::OAICatalog_data_product_attribute_media_gallery_entry_extension_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::OAICatalog_data_product_attribute_media_gallery_entry_extension_interface() {
    this->initializeModel();
}

OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::~OAICatalog_data_product_attribute_media_gallery_entry_extension_interface() {}

void OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::initializeModel() {

    m_video_content_isSet = false;
    m_video_content_isValid = false;
}

void OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::fromJsonObject(QJsonObject json) {

    m_video_content_isValid = ::OpenAPI::fromJsonValue(m_video_content, json[QString("video_content")]);
    m_video_content_isSet = !json[QString("video_content")].isNull() && m_video_content_isValid;
}

QString OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_video_content.isSet()) {
        obj.insert(QString("video_content"), ::OpenAPI::toJsonValue(m_video_content));
    }
    return obj;
}

OAIFramework_data_video_content_interface OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::getVideoContent() const {
    return m_video_content;
}
void OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::setVideoContent(const OAIFramework_data_video_content_interface &video_content) {
    m_video_content = video_content;
    m_video_content_isSet = true;
}

bool OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::is_video_content_Set() const{
    return m_video_content_isSet;
}

bool OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::is_video_content_Valid() const{
    return m_video_content_isValid;
}

bool OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_video_content.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICatalog_data_product_attribute_media_gallery_entry_extension_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
