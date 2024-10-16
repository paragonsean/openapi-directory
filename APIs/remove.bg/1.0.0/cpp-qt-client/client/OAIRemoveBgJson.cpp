/**
 * Background Removal API
 * Remove the background of any image
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRemoveBgJson.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRemoveBgJson::OAIRemoveBgJson(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRemoveBgJson::OAIRemoveBgJson() {
    this->initializeModel();
}

OAIRemoveBgJson::~OAIRemoveBgJson() {}

void OAIRemoveBgJson::initializeModel() {

    m_add_shadow_isSet = false;
    m_add_shadow_isValid = false;

    m_bg_color_isSet = false;
    m_bg_color_isValid = false;

    m_bg_image_url_isSet = false;
    m_bg_image_url_isValid = false;

    m_channels_isSet = false;
    m_channels_isValid = false;

    m_crop_isSet = false;
    m_crop_isValid = false;

    m_crop_margin_isSet = false;
    m_crop_margin_isValid = false;

    m_format_isSet = false;
    m_format_isValid = false;

    m_image_file_b64_isSet = false;
    m_image_file_b64_isValid = false;

    m_image_url_isSet = false;
    m_image_url_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_roi_isSet = false;
    m_roi_isValid = false;

    m_scale_isSet = false;
    m_scale_isValid = false;

    m_semitransparency_isSet = false;
    m_semitransparency_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_type_level_isSet = false;
    m_type_level_isValid = false;
}

void OAIRemoveBgJson::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRemoveBgJson::fromJsonObject(QJsonObject json) {

    m_add_shadow_isValid = ::OpenAPI::fromJsonValue(m_add_shadow, json[QString("add_shadow")]);
    m_add_shadow_isSet = !json[QString("add_shadow")].isNull() && m_add_shadow_isValid;

    m_bg_color_isValid = ::OpenAPI::fromJsonValue(m_bg_color, json[QString("bg_color")]);
    m_bg_color_isSet = !json[QString("bg_color")].isNull() && m_bg_color_isValid;

    m_bg_image_url_isValid = ::OpenAPI::fromJsonValue(m_bg_image_url, json[QString("bg_image_url")]);
    m_bg_image_url_isSet = !json[QString("bg_image_url")].isNull() && m_bg_image_url_isValid;

    m_channels_isValid = ::OpenAPI::fromJsonValue(m_channels, json[QString("channels")]);
    m_channels_isSet = !json[QString("channels")].isNull() && m_channels_isValid;

    m_crop_isValid = ::OpenAPI::fromJsonValue(m_crop, json[QString("crop")]);
    m_crop_isSet = !json[QString("crop")].isNull() && m_crop_isValid;

    m_crop_margin_isValid = ::OpenAPI::fromJsonValue(m_crop_margin, json[QString("crop_margin")]);
    m_crop_margin_isSet = !json[QString("crop_margin")].isNull() && m_crop_margin_isValid;

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;

    m_image_file_b64_isValid = ::OpenAPI::fromJsonValue(m_image_file_b64, json[QString("image_file_b64")]);
    m_image_file_b64_isSet = !json[QString("image_file_b64")].isNull() && m_image_file_b64_isValid;

    m_image_url_isValid = ::OpenAPI::fromJsonValue(m_image_url, json[QString("image_url")]);
    m_image_url_isSet = !json[QString("image_url")].isNull() && m_image_url_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("position")]);
    m_position_isSet = !json[QString("position")].isNull() && m_position_isValid;

    m_roi_isValid = ::OpenAPI::fromJsonValue(m_roi, json[QString("roi")]);
    m_roi_isSet = !json[QString("roi")].isNull() && m_roi_isValid;

    m_scale_isValid = ::OpenAPI::fromJsonValue(m_scale, json[QString("scale")]);
    m_scale_isSet = !json[QString("scale")].isNull() && m_scale_isValid;

    m_semitransparency_isValid = ::OpenAPI::fromJsonValue(m_semitransparency, json[QString("semitransparency")]);
    m_semitransparency_isSet = !json[QString("semitransparency")].isNull() && m_semitransparency_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_type_level_isValid = ::OpenAPI::fromJsonValue(m_type_level, json[QString("type_level")]);
    m_type_level_isSet = !json[QString("type_level")].isNull() && m_type_level_isValid;
}

QString OAIRemoveBgJson::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRemoveBgJson::asJsonObject() const {
    QJsonObject obj;
    if (m_add_shadow_isSet) {
        obj.insert(QString("add_shadow"), ::OpenAPI::toJsonValue(m_add_shadow));
    }
    if (m_bg_color_isSet) {
        obj.insert(QString("bg_color"), ::OpenAPI::toJsonValue(m_bg_color));
    }
    if (m_bg_image_url_isSet) {
        obj.insert(QString("bg_image_url"), ::OpenAPI::toJsonValue(m_bg_image_url));
    }
    if (m_channels_isSet) {
        obj.insert(QString("channels"), ::OpenAPI::toJsonValue(m_channels));
    }
    if (m_crop_isSet) {
        obj.insert(QString("crop"), ::OpenAPI::toJsonValue(m_crop));
    }
    if (m_crop_margin_isSet) {
        obj.insert(QString("crop_margin"), ::OpenAPI::toJsonValue(m_crop_margin));
    }
    if (m_format_isSet) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_image_file_b64_isSet) {
        obj.insert(QString("image_file_b64"), ::OpenAPI::toJsonValue(m_image_file_b64));
    }
    if (m_image_url_isSet) {
        obj.insert(QString("image_url"), ::OpenAPI::toJsonValue(m_image_url));
    }
    if (m_position_isSet) {
        obj.insert(QString("position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_roi_isSet) {
        obj.insert(QString("roi"), ::OpenAPI::toJsonValue(m_roi));
    }
    if (m_scale_isSet) {
        obj.insert(QString("scale"), ::OpenAPI::toJsonValue(m_scale));
    }
    if (m_semitransparency_isSet) {
        obj.insert(QString("semitransparency"), ::OpenAPI::toJsonValue(m_semitransparency));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_type_level_isSet) {
        obj.insert(QString("type_level"), ::OpenAPI::toJsonValue(m_type_level));
    }
    return obj;
}

bool OAIRemoveBgJson::isAddShadow() const {
    return m_add_shadow;
}
void OAIRemoveBgJson::setAddShadow(const bool &add_shadow) {
    m_add_shadow = add_shadow;
    m_add_shadow_isSet = true;
}

bool OAIRemoveBgJson::is_add_shadow_Set() const{
    return m_add_shadow_isSet;
}

bool OAIRemoveBgJson::is_add_shadow_Valid() const{
    return m_add_shadow_isValid;
}

QString OAIRemoveBgJson::getBgColor() const {
    return m_bg_color;
}
void OAIRemoveBgJson::setBgColor(const QString &bg_color) {
    m_bg_color = bg_color;
    m_bg_color_isSet = true;
}

bool OAIRemoveBgJson::is_bg_color_Set() const{
    return m_bg_color_isSet;
}

bool OAIRemoveBgJson::is_bg_color_Valid() const{
    return m_bg_color_isValid;
}

QString OAIRemoveBgJson::getBgImageUrl() const {
    return m_bg_image_url;
}
void OAIRemoveBgJson::setBgImageUrl(const QString &bg_image_url) {
    m_bg_image_url = bg_image_url;
    m_bg_image_url_isSet = true;
}

bool OAIRemoveBgJson::is_bg_image_url_Set() const{
    return m_bg_image_url_isSet;
}

bool OAIRemoveBgJson::is_bg_image_url_Valid() const{
    return m_bg_image_url_isValid;
}

QString OAIRemoveBgJson::getChannels() const {
    return m_channels;
}
void OAIRemoveBgJson::setChannels(const QString &channels) {
    m_channels = channels;
    m_channels_isSet = true;
}

bool OAIRemoveBgJson::is_channels_Set() const{
    return m_channels_isSet;
}

bool OAIRemoveBgJson::is_channels_Valid() const{
    return m_channels_isValid;
}

bool OAIRemoveBgJson::isCrop() const {
    return m_crop;
}
void OAIRemoveBgJson::setCrop(const bool &crop) {
    m_crop = crop;
    m_crop_isSet = true;
}

bool OAIRemoveBgJson::is_crop_Set() const{
    return m_crop_isSet;
}

bool OAIRemoveBgJson::is_crop_Valid() const{
    return m_crop_isValid;
}

QString OAIRemoveBgJson::getCropMargin() const {
    return m_crop_margin;
}
void OAIRemoveBgJson::setCropMargin(const QString &crop_margin) {
    m_crop_margin = crop_margin;
    m_crop_margin_isSet = true;
}

bool OAIRemoveBgJson::is_crop_margin_Set() const{
    return m_crop_margin_isSet;
}

bool OAIRemoveBgJson::is_crop_margin_Valid() const{
    return m_crop_margin_isValid;
}

QString OAIRemoveBgJson::getFormat() const {
    return m_format;
}
void OAIRemoveBgJson::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAIRemoveBgJson::is_format_Set() const{
    return m_format_isSet;
}

bool OAIRemoveBgJson::is_format_Valid() const{
    return m_format_isValid;
}

QString OAIRemoveBgJson::getImageFileB64() const {
    return m_image_file_b64;
}
void OAIRemoveBgJson::setImageFileB64(const QString &image_file_b64) {
    m_image_file_b64 = image_file_b64;
    m_image_file_b64_isSet = true;
}

bool OAIRemoveBgJson::is_image_file_b64_Set() const{
    return m_image_file_b64_isSet;
}

bool OAIRemoveBgJson::is_image_file_b64_Valid() const{
    return m_image_file_b64_isValid;
}

QString OAIRemoveBgJson::getImageUrl() const {
    return m_image_url;
}
void OAIRemoveBgJson::setImageUrl(const QString &image_url) {
    m_image_url = image_url;
    m_image_url_isSet = true;
}

bool OAIRemoveBgJson::is_image_url_Set() const{
    return m_image_url_isSet;
}

bool OAIRemoveBgJson::is_image_url_Valid() const{
    return m_image_url_isValid;
}

QString OAIRemoveBgJson::getPosition() const {
    return m_position;
}
void OAIRemoveBgJson::setPosition(const QString &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIRemoveBgJson::is_position_Set() const{
    return m_position_isSet;
}

bool OAIRemoveBgJson::is_position_Valid() const{
    return m_position_isValid;
}

QString OAIRemoveBgJson::getRoi() const {
    return m_roi;
}
void OAIRemoveBgJson::setRoi(const QString &roi) {
    m_roi = roi;
    m_roi_isSet = true;
}

bool OAIRemoveBgJson::is_roi_Set() const{
    return m_roi_isSet;
}

bool OAIRemoveBgJson::is_roi_Valid() const{
    return m_roi_isValid;
}

QString OAIRemoveBgJson::getScale() const {
    return m_scale;
}
void OAIRemoveBgJson::setScale(const QString &scale) {
    m_scale = scale;
    m_scale_isSet = true;
}

bool OAIRemoveBgJson::is_scale_Set() const{
    return m_scale_isSet;
}

bool OAIRemoveBgJson::is_scale_Valid() const{
    return m_scale_isValid;
}

bool OAIRemoveBgJson::isSemitransparency() const {
    return m_semitransparency;
}
void OAIRemoveBgJson::setSemitransparency(const bool &semitransparency) {
    m_semitransparency = semitransparency;
    m_semitransparency_isSet = true;
}

bool OAIRemoveBgJson::is_semitransparency_Set() const{
    return m_semitransparency_isSet;
}

bool OAIRemoveBgJson::is_semitransparency_Valid() const{
    return m_semitransparency_isValid;
}

QString OAIRemoveBgJson::getSize() const {
    return m_size;
}
void OAIRemoveBgJson::setSize(const QString &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIRemoveBgJson::is_size_Set() const{
    return m_size_isSet;
}

bool OAIRemoveBgJson::is_size_Valid() const{
    return m_size_isValid;
}

QString OAIRemoveBgJson::getType() const {
    return m_type;
}
void OAIRemoveBgJson::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIRemoveBgJson::is_type_Set() const{
    return m_type_isSet;
}

bool OAIRemoveBgJson::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIRemoveBgJson::getTypeLevel() const {
    return m_type_level;
}
void OAIRemoveBgJson::setTypeLevel(const QString &type_level) {
    m_type_level = type_level;
    m_type_level_isSet = true;
}

bool OAIRemoveBgJson::is_type_level_Set() const{
    return m_type_level_isSet;
}

bool OAIRemoveBgJson::is_type_level_Valid() const{
    return m_type_level_isValid;
}

bool OAIRemoveBgJson::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_add_shadow_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bg_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bg_image_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_channels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_crop_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_crop_margin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_file_b64_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_roi_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scale_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_semitransparency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_level_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRemoveBgJson::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
