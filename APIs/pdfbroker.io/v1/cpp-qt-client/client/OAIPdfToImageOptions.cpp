/**
 * PdfBroker.io API
 * PdfBroker.io is an api for creating pdf files from Xsl-Fo or Html and other useful pdf utilities.
 *
 * The version of the OpenAPI document: v1
 * Contact: support@pdfbroker.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPdfToImageOptions.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPdfToImageOptions::OAIPdfToImageOptions(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPdfToImageOptions::OAIPdfToImageOptions() {
    this->initializeModel();
}

OAIPdfToImageOptions::~OAIPdfToImageOptions() {}

void OAIPdfToImageOptions::initializeModel() {

    m_height_isSet = false;
    m_height_isValid = false;

    m_horizontal_resolution_isSet = false;
    m_horizontal_resolution_isValid = false;

    m_image_format_isSet = false;
    m_image_format_isValid = false;

    m_jpeg_quality_isSet = false;
    m_jpeg_quality_isValid = false;

    m_page_number_isSet = false;
    m_page_number_isValid = false;

    m_png_compression_level_isSet = false;
    m_png_compression_level_isValid = false;

    m_transparent_isSet = false;
    m_transparent_isValid = false;

    m_vertical_resolution_isSet = false;
    m_vertical_resolution_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAIPdfToImageOptions::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPdfToImageOptions::fromJsonObject(QJsonObject json) {

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_horizontal_resolution_isValid = ::OpenAPI::fromJsonValue(m_horizontal_resolution, json[QString("horizontalResolution")]);
    m_horizontal_resolution_isSet = !json[QString("horizontalResolution")].isNull() && m_horizontal_resolution_isValid;

    m_image_format_isValid = ::OpenAPI::fromJsonValue(m_image_format, json[QString("imageFormat")]);
    m_image_format_isSet = !json[QString("imageFormat")].isNull() && m_image_format_isValid;

    m_jpeg_quality_isValid = ::OpenAPI::fromJsonValue(m_jpeg_quality, json[QString("jpegQuality")]);
    m_jpeg_quality_isSet = !json[QString("jpegQuality")].isNull() && m_jpeg_quality_isValid;

    m_page_number_isValid = ::OpenAPI::fromJsonValue(m_page_number, json[QString("pageNumber")]);
    m_page_number_isSet = !json[QString("pageNumber")].isNull() && m_page_number_isValid;

    m_png_compression_level_isValid = ::OpenAPI::fromJsonValue(m_png_compression_level, json[QString("pngCompressionLevel")]);
    m_png_compression_level_isSet = !json[QString("pngCompressionLevel")].isNull() && m_png_compression_level_isValid;

    m_transparent_isValid = ::OpenAPI::fromJsonValue(m_transparent, json[QString("transparent")]);
    m_transparent_isSet = !json[QString("transparent")].isNull() && m_transparent_isValid;

    m_vertical_resolution_isValid = ::OpenAPI::fromJsonValue(m_vertical_resolution, json[QString("verticalResolution")]);
    m_vertical_resolution_isSet = !json[QString("verticalResolution")].isNull() && m_vertical_resolution_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAIPdfToImageOptions::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPdfToImageOptions::asJsonObject() const {
    QJsonObject obj;
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_horizontal_resolution_isSet) {
        obj.insert(QString("horizontalResolution"), ::OpenAPI::toJsonValue(m_horizontal_resolution));
    }
    if (m_image_format_isSet) {
        obj.insert(QString("imageFormat"), ::OpenAPI::toJsonValue(m_image_format));
    }
    if (m_jpeg_quality_isSet) {
        obj.insert(QString("jpegQuality"), ::OpenAPI::toJsonValue(m_jpeg_quality));
    }
    if (m_page_number_isSet) {
        obj.insert(QString("pageNumber"), ::OpenAPI::toJsonValue(m_page_number));
    }
    if (m_png_compression_level_isSet) {
        obj.insert(QString("pngCompressionLevel"), ::OpenAPI::toJsonValue(m_png_compression_level));
    }
    if (m_transparent_isSet) {
        obj.insert(QString("transparent"), ::OpenAPI::toJsonValue(m_transparent));
    }
    if (m_vertical_resolution_isSet) {
        obj.insert(QString("verticalResolution"), ::OpenAPI::toJsonValue(m_vertical_resolution));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

qint32 OAIPdfToImageOptions::getHeight() const {
    return m_height;
}
void OAIPdfToImageOptions::setHeight(const qint32 &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIPdfToImageOptions::is_height_Set() const{
    return m_height_isSet;
}

bool OAIPdfToImageOptions::is_height_Valid() const{
    return m_height_isValid;
}

double OAIPdfToImageOptions::getHorizontalResolution() const {
    return m_horizontal_resolution;
}
void OAIPdfToImageOptions::setHorizontalResolution(const double &horizontal_resolution) {
    m_horizontal_resolution = horizontal_resolution;
    m_horizontal_resolution_isSet = true;
}

bool OAIPdfToImageOptions::is_horizontal_resolution_Set() const{
    return m_horizontal_resolution_isSet;
}

bool OAIPdfToImageOptions::is_horizontal_resolution_Valid() const{
    return m_horizontal_resolution_isValid;
}

QString OAIPdfToImageOptions::getImageFormat() const {
    return m_image_format;
}
void OAIPdfToImageOptions::setImageFormat(const QString &image_format) {
    m_image_format = image_format;
    m_image_format_isSet = true;
}

bool OAIPdfToImageOptions::is_image_format_Set() const{
    return m_image_format_isSet;
}

bool OAIPdfToImageOptions::is_image_format_Valid() const{
    return m_image_format_isValid;
}

qint32 OAIPdfToImageOptions::getJpegQuality() const {
    return m_jpeg_quality;
}
void OAIPdfToImageOptions::setJpegQuality(const qint32 &jpeg_quality) {
    m_jpeg_quality = jpeg_quality;
    m_jpeg_quality_isSet = true;
}

bool OAIPdfToImageOptions::is_jpeg_quality_Set() const{
    return m_jpeg_quality_isSet;
}

bool OAIPdfToImageOptions::is_jpeg_quality_Valid() const{
    return m_jpeg_quality_isValid;
}

qint32 OAIPdfToImageOptions::getPageNumber() const {
    return m_page_number;
}
void OAIPdfToImageOptions::setPageNumber(const qint32 &page_number) {
    m_page_number = page_number;
    m_page_number_isSet = true;
}

bool OAIPdfToImageOptions::is_page_number_Set() const{
    return m_page_number_isSet;
}

bool OAIPdfToImageOptions::is_page_number_Valid() const{
    return m_page_number_isValid;
}

qint32 OAIPdfToImageOptions::getPngCompressionLevel() const {
    return m_png_compression_level;
}
void OAIPdfToImageOptions::setPngCompressionLevel(const qint32 &png_compression_level) {
    m_png_compression_level = png_compression_level;
    m_png_compression_level_isSet = true;
}

bool OAIPdfToImageOptions::is_png_compression_level_Set() const{
    return m_png_compression_level_isSet;
}

bool OAIPdfToImageOptions::is_png_compression_level_Valid() const{
    return m_png_compression_level_isValid;
}

bool OAIPdfToImageOptions::isTransparent() const {
    return m_transparent;
}
void OAIPdfToImageOptions::setTransparent(const bool &transparent) {
    m_transparent = transparent;
    m_transparent_isSet = true;
}

bool OAIPdfToImageOptions::is_transparent_Set() const{
    return m_transparent_isSet;
}

bool OAIPdfToImageOptions::is_transparent_Valid() const{
    return m_transparent_isValid;
}

double OAIPdfToImageOptions::getVerticalResolution() const {
    return m_vertical_resolution;
}
void OAIPdfToImageOptions::setVerticalResolution(const double &vertical_resolution) {
    m_vertical_resolution = vertical_resolution;
    m_vertical_resolution_isSet = true;
}

bool OAIPdfToImageOptions::is_vertical_resolution_Set() const{
    return m_vertical_resolution_isSet;
}

bool OAIPdfToImageOptions::is_vertical_resolution_Valid() const{
    return m_vertical_resolution_isValid;
}

qint32 OAIPdfToImageOptions::getWidth() const {
    return m_width;
}
void OAIPdfToImageOptions::setWidth(const qint32 &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAIPdfToImageOptions::is_width_Set() const{
    return m_width_isSet;
}

bool OAIPdfToImageOptions::is_width_Valid() const{
    return m_width_isValid;
}

bool OAIPdfToImageOptions::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_horizontal_resolution_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_jpeg_quality_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_png_compression_level_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transparent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vertical_resolution_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_width_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPdfToImageOptions::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
