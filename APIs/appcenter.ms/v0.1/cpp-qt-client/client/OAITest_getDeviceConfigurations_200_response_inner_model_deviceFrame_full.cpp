/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full() {
    this->initializeModel();
}

OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::~OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full() {}

void OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::initializeModel() {

    m_frame_url_isSet = false;
    m_frame_url_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_screen_isSet = false;
    m_screen_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::fromJsonObject(QJsonObject json) {

    m_frame_url_isValid = ::OpenAPI::fromJsonValue(m_frame_url, json[QString("frameUrl")]);
    m_frame_url_isSet = !json[QString("frameUrl")].isNull() && m_frame_url_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_screen_isValid = ::OpenAPI::fromJsonValue(m_screen, json[QString("screen")]);
    m_screen_isSet = !json[QString("screen")].isNull() && m_screen_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::asJsonObject() const {
    QJsonObject obj;
    if (m_frame_url_isSet) {
        obj.insert(QString("frameUrl"), ::OpenAPI::toJsonValue(m_frame_url));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_screen.size() > 0) {
        obj.insert(QString("screen"), ::OpenAPI::toJsonValue(m_screen));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

QString OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::getFrameUrl() const {
    return m_frame_url;
}
void OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::setFrameUrl(const QString &frame_url) {
    m_frame_url = frame_url;
    m_frame_url_isSet = true;
}

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::is_frame_url_Set() const{
    return m_frame_url_isSet;
}

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::is_frame_url_Valid() const{
    return m_frame_url_isValid;
}

double OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::getHeight() const {
    return m_height;
}
void OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::setHeight(const double &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::is_height_Set() const{
    return m_height_isSet;
}

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::is_height_Valid() const{
    return m_height_isValid;
}

QList<double> OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::getScreen() const {
    return m_screen;
}
void OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::setScreen(const QList<double> &screen) {
    m_screen = screen;
    m_screen_isSet = true;
}

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::is_screen_Set() const{
    return m_screen_isSet;
}

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::is_screen_Valid() const{
    return m_screen_isValid;
}

double OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::getWidth() const {
    return m_width;
}
void OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::setWidth(const double &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::is_width_Set() const{
    return m_width_isSet;
}

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::is_width_Valid() const{
    return m_width_isValid;
}

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_frame_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_screen.size() > 0) {
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

bool OAITest_getDeviceConfigurations_200_response_inner_model_deviceFrame_full::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
