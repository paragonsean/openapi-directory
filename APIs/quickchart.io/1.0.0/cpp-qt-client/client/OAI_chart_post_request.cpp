/**
 * QuickChart API
 * An API to generate charts and QR codes using QuickChart services.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_chart_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_chart_post_request::OAI_chart_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_chart_post_request::OAI_chart_post_request() {
    this->initializeModel();
}

OAI_chart_post_request::~OAI_chart_post_request() {}

void OAI_chart_post_request::initializeModel() {

    m_background_color_isSet = false;
    m_background_color_isValid = false;

    m_chart_isSet = false;
    m_chart_isValid = false;

    m_format_isSet = false;
    m_format_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAI_chart_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_chart_post_request::fromJsonObject(QJsonObject json) {

    m_background_color_isValid = ::OpenAPI::fromJsonValue(m_background_color, json[QString("backgroundColor")]);
    m_background_color_isSet = !json[QString("backgroundColor")].isNull() && m_background_color_isValid;

    m_chart_isValid = ::OpenAPI::fromJsonValue(m_chart, json[QString("chart")]);
    m_chart_isSet = !json[QString("chart")].isNull() && m_chart_isValid;

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAI_chart_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_chart_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_background_color_isSet) {
        obj.insert(QString("backgroundColor"), ::OpenAPI::toJsonValue(m_background_color));
    }
    if (m_chart_isSet) {
        obj.insert(QString("chart"), ::OpenAPI::toJsonValue(m_chart));
    }
    if (m_format_isSet) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

QString OAI_chart_post_request::getBackgroundColor() const {
    return m_background_color;
}
void OAI_chart_post_request::setBackgroundColor(const QString &background_color) {
    m_background_color = background_color;
    m_background_color_isSet = true;
}

bool OAI_chart_post_request::is_background_color_Set() const{
    return m_background_color_isSet;
}

bool OAI_chart_post_request::is_background_color_Valid() const{
    return m_background_color_isValid;
}

OAIObject OAI_chart_post_request::getChart() const {
    return m_chart;
}
void OAI_chart_post_request::setChart(const OAIObject &chart) {
    m_chart = chart;
    m_chart_isSet = true;
}

bool OAI_chart_post_request::is_chart_Set() const{
    return m_chart_isSet;
}

bool OAI_chart_post_request::is_chart_Valid() const{
    return m_chart_isValid;
}

QString OAI_chart_post_request::getFormat() const {
    return m_format;
}
void OAI_chart_post_request::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAI_chart_post_request::is_format_Set() const{
    return m_format_isSet;
}

bool OAI_chart_post_request::is_format_Valid() const{
    return m_format_isValid;
}

qint32 OAI_chart_post_request::getHeight() const {
    return m_height;
}
void OAI_chart_post_request::setHeight(const qint32 &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAI_chart_post_request::is_height_Set() const{
    return m_height_isSet;
}

bool OAI_chart_post_request::is_height_Valid() const{
    return m_height_isValid;
}

qint32 OAI_chart_post_request::getWidth() const {
    return m_width;
}
void OAI_chart_post_request::setWidth(const qint32 &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAI_chart_post_request::is_width_Set() const{
    return m_width_isSet;
}

bool OAI_chart_post_request::is_width_Valid() const{
    return m_width_isValid;
}

bool OAI_chart_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_background_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_chart_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
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

bool OAI_chart_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
