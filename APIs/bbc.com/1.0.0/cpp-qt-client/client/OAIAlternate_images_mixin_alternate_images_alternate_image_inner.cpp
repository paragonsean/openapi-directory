/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAlternate_images_mixin_alternate_images_alternate_image_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlternate_images_mixin_alternate_images_alternate_image_inner::OAIAlternate_images_mixin_alternate_images_alternate_image_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlternate_images_mixin_alternate_images_alternate_image_inner::OAIAlternate_images_mixin_alternate_images_alternate_image_inner() {
    this->initializeModel();
}

OAIAlternate_images_mixin_alternate_images_alternate_image_inner::~OAIAlternate_images_mixin_alternate_images_alternate_image_inner() {}

void OAIAlternate_images_mixin_alternate_images_alternate_image_inner::initializeModel() {

    m_alternate_images_isSet = false;
    m_alternate_images_isValid = false;

    m_href_isSet = false;
    m_href_isValid = false;

    m_template_url_isSet = false;
    m_template_url_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIAlternate_images_mixin_alternate_images_alternate_image_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAlternate_images_mixin_alternate_images_alternate_image_inner::fromJsonObject(QJsonObject json) {

    m_alternate_images_isValid = ::OpenAPI::fromJsonValue(m_alternate_images, json[QString("alternate_images")]);
    m_alternate_images_isSet = !json[QString("alternate_images")].isNull() && m_alternate_images_isValid;

    m_href_isValid = ::OpenAPI::fromJsonValue(m_href, json[QString("href")]);
    m_href_isSet = !json[QString("href")].isNull() && m_href_isValid;

    m_template_url_isValid = ::OpenAPI::fromJsonValue(m_template_url, json[QString("template_url")]);
    m_template_url_isSet = !json[QString("template_url")].isNull() && m_template_url_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIAlternate_images_mixin_alternate_images_alternate_image_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAlternate_images_mixin_alternate_images_alternate_image_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_alternate_images.isSet()) {
        obj.insert(QString("alternate_images"), ::OpenAPI::toJsonValue(m_alternate_images));
    }
    if (m_href_isSet) {
        obj.insert(QString("href"), ::OpenAPI::toJsonValue(m_href));
    }
    if (m_template_url_isSet) {
        obj.insert(QString("template_url"), ::OpenAPI::toJsonValue(m_template_url));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIAlternate_images_mixin_alternate_images_alternate_image_inner_alternate_images OAIAlternate_images_mixin_alternate_images_alternate_image_inner::getAlternateImages() const {
    return m_alternate_images;
}
void OAIAlternate_images_mixin_alternate_images_alternate_image_inner::setAlternateImages(const OAIAlternate_images_mixin_alternate_images_alternate_image_inner_alternate_images &alternate_images) {
    m_alternate_images = alternate_images;
    m_alternate_images_isSet = true;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::is_alternate_images_Set() const{
    return m_alternate_images_isSet;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::is_alternate_images_Valid() const{
    return m_alternate_images_isValid;
}

QString OAIAlternate_images_mixin_alternate_images_alternate_image_inner::getHref() const {
    return m_href;
}
void OAIAlternate_images_mixin_alternate_images_alternate_image_inner::setHref(const QString &href) {
    m_href = href;
    m_href_isSet = true;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::is_href_Set() const{
    return m_href_isSet;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::is_href_Valid() const{
    return m_href_isValid;
}

QString OAIAlternate_images_mixin_alternate_images_alternate_image_inner::getTemplateUrl() const {
    return m_template_url;
}
void OAIAlternate_images_mixin_alternate_images_alternate_image_inner::setTemplateUrl(const QString &template_url) {
    m_template_url = template_url;
    m_template_url_isSet = true;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::is_template_url_Set() const{
    return m_template_url_isSet;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::is_template_url_Valid() const{
    return m_template_url_isValid;
}

QString OAIAlternate_images_mixin_alternate_images_alternate_image_inner::getType() const {
    return m_type;
}
void OAIAlternate_images_mixin_alternate_images_alternate_image_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alternate_images.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_href_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_template_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAlternate_images_mixin_alternate_images_alternate_image_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_alternate_images_isValid && m_template_url_isValid && true;
}

} // namespace OpenAPI
