/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImageInformation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageInformation::OAIImageInformation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageInformation::OAIImageInformation() {
    this->initializeModel();
}

OAIImageInformation::~OAIImageInformation() {}

void OAIImageInformation::initializeModel() {

    m_frame_index_isSet = false;
    m_frame_index_isValid = false;

    m_maximum_pixel_value_isSet = false;
    m_maximum_pixel_value_isValid = false;

    m_minimum_pixel_value_isSet = false;
    m_minimum_pixel_value_isValid = false;

    m_number_of_frames_isSet = false;
    m_number_of_frames_isValid = false;
}

void OAIImageInformation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageInformation::fromJsonObject(QJsonObject json) {

    m_frame_index_isValid = ::OpenAPI::fromJsonValue(m_frame_index, json[QString("frameIndex")]);
    m_frame_index_isSet = !json[QString("frameIndex")].isNull() && m_frame_index_isValid;

    m_maximum_pixel_value_isValid = ::OpenAPI::fromJsonValue(m_maximum_pixel_value, json[QString("maximumPixelValue")]);
    m_maximum_pixel_value_isSet = !json[QString("maximumPixelValue")].isNull() && m_maximum_pixel_value_isValid;

    m_minimum_pixel_value_isValid = ::OpenAPI::fromJsonValue(m_minimum_pixel_value, json[QString("minimumPixelValue")]);
    m_minimum_pixel_value_isSet = !json[QString("minimumPixelValue")].isNull() && m_minimum_pixel_value_isValid;

    m_number_of_frames_isValid = ::OpenAPI::fromJsonValue(m_number_of_frames, json[QString("numberOfFrames")]);
    m_number_of_frames_isSet = !json[QString("numberOfFrames")].isNull() && m_number_of_frames_isValid;
}

QString OAIImageInformation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageInformation::asJsonObject() const {
    QJsonObject obj;
    if (m_frame_index_isSet) {
        obj.insert(QString("frameIndex"), ::OpenAPI::toJsonValue(m_frame_index));
    }
    if (m_maximum_pixel_value_isSet) {
        obj.insert(QString("maximumPixelValue"), ::OpenAPI::toJsonValue(m_maximum_pixel_value));
    }
    if (m_minimum_pixel_value_isSet) {
        obj.insert(QString("minimumPixelValue"), ::OpenAPI::toJsonValue(m_minimum_pixel_value));
    }
    if (m_number_of_frames_isSet) {
        obj.insert(QString("numberOfFrames"), ::OpenAPI::toJsonValue(m_number_of_frames));
    }
    return obj;
}

qint32 OAIImageInformation::getFrameIndex() const {
    return m_frame_index;
}
void OAIImageInformation::setFrameIndex(const qint32 &frame_index) {
    m_frame_index = frame_index;
    m_frame_index_isSet = true;
}

bool OAIImageInformation::is_frame_index_Set() const{
    return m_frame_index_isSet;
}

bool OAIImageInformation::is_frame_index_Valid() const{
    return m_frame_index_isValid;
}

qint32 OAIImageInformation::getMaximumPixelValue() const {
    return m_maximum_pixel_value;
}
void OAIImageInformation::setMaximumPixelValue(const qint32 &maximum_pixel_value) {
    m_maximum_pixel_value = maximum_pixel_value;
    m_maximum_pixel_value_isSet = true;
}

bool OAIImageInformation::is_maximum_pixel_value_Set() const{
    return m_maximum_pixel_value_isSet;
}

bool OAIImageInformation::is_maximum_pixel_value_Valid() const{
    return m_maximum_pixel_value_isValid;
}

qint32 OAIImageInformation::getMinimumPixelValue() const {
    return m_minimum_pixel_value;
}
void OAIImageInformation::setMinimumPixelValue(const qint32 &minimum_pixel_value) {
    m_minimum_pixel_value = minimum_pixel_value;
    m_minimum_pixel_value_isSet = true;
}

bool OAIImageInformation::is_minimum_pixel_value_Set() const{
    return m_minimum_pixel_value_isSet;
}

bool OAIImageInformation::is_minimum_pixel_value_Valid() const{
    return m_minimum_pixel_value_isValid;
}

qint32 OAIImageInformation::getNumberOfFrames() const {
    return m_number_of_frames;
}
void OAIImageInformation::setNumberOfFrames(const qint32 &number_of_frames) {
    m_number_of_frames = number_of_frames;
    m_number_of_frames_isSet = true;
}

bool OAIImageInformation::is_number_of_frames_Set() const{
    return m_number_of_frames_isSet;
}

bool OAIImageInformation::is_number_of_frames_Valid() const{
    return m_number_of_frames_isValid;
}

bool OAIImageInformation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_frame_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_maximum_pixel_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minimum_pixel_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_frames_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImageInformation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
