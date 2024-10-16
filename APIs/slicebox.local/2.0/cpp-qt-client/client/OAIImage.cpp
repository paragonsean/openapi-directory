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

#include "OAIImage.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImage::OAIImage(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImage::OAIImage() {
    this->initializeModel();
}

OAIImage::~OAIImage() {}

void OAIImage::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_type_isSet = false;
    m_image_type_isValid = false;

    m_instance_number_isSet = false;
    m_instance_number_isValid = false;

    m_series_id_isSet = false;
    m_series_id_isValid = false;

    m_sop_instance_uid_isSet = false;
    m_sop_instance_uid_isValid = false;
}

void OAIImage::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImage::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_type_isValid = ::OpenAPI::fromJsonValue(m_image_type, json[QString("imageType")]);
    m_image_type_isSet = !json[QString("imageType")].isNull() && m_image_type_isValid;

    m_instance_number_isValid = ::OpenAPI::fromJsonValue(m_instance_number, json[QString("instanceNumber")]);
    m_instance_number_isSet = !json[QString("instanceNumber")].isNull() && m_instance_number_isValid;

    m_series_id_isValid = ::OpenAPI::fromJsonValue(m_series_id, json[QString("seriesId")]);
    m_series_id_isSet = !json[QString("seriesId")].isNull() && m_series_id_isValid;

    m_sop_instance_uid_isValid = ::OpenAPI::fromJsonValue(m_sop_instance_uid, json[QString("sopInstanceUID")]);
    m_sop_instance_uid_isSet = !json[QString("sopInstanceUID")].isNull() && m_sop_instance_uid_isValid;
}

QString OAIImage::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImage::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_type.isSet()) {
        obj.insert(QString("imageType"), ::OpenAPI::toJsonValue(m_image_type));
    }
    if (m_instance_number.isSet()) {
        obj.insert(QString("instanceNumber"), ::OpenAPI::toJsonValue(m_instance_number));
    }
    if (m_series_id_isSet) {
        obj.insert(QString("seriesId"), ::OpenAPI::toJsonValue(m_series_id));
    }
    if (m_sop_instance_uid.isSet()) {
        obj.insert(QString("sopInstanceUID"), ::OpenAPI::toJsonValue(m_sop_instance_uid));
    }
    return obj;
}

qint64 OAIImage::getId() const {
    return m_id;
}
void OAIImage::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIImage::is_id_Set() const{
    return m_id_isSet;
}

bool OAIImage::is_id_Valid() const{
    return m_id_isValid;
}

OAIDicomPropertyValue OAIImage::getImageType() const {
    return m_image_type;
}
void OAIImage::setImageType(const OAIDicomPropertyValue &image_type) {
    m_image_type = image_type;
    m_image_type_isSet = true;
}

bool OAIImage::is_image_type_Set() const{
    return m_image_type_isSet;
}

bool OAIImage::is_image_type_Valid() const{
    return m_image_type_isValid;
}

OAIDicomPropertyValue OAIImage::getInstanceNumber() const {
    return m_instance_number;
}
void OAIImage::setInstanceNumber(const OAIDicomPropertyValue &instance_number) {
    m_instance_number = instance_number;
    m_instance_number_isSet = true;
}

bool OAIImage::is_instance_number_Set() const{
    return m_instance_number_isSet;
}

bool OAIImage::is_instance_number_Valid() const{
    return m_instance_number_isValid;
}

qint64 OAIImage::getSeriesId() const {
    return m_series_id;
}
void OAIImage::setSeriesId(const qint64 &series_id) {
    m_series_id = series_id;
    m_series_id_isSet = true;
}

bool OAIImage::is_series_id_Set() const{
    return m_series_id_isSet;
}

bool OAIImage::is_series_id_Valid() const{
    return m_series_id_isValid;
}

OAIDicomPropertyValue OAIImage::getSopInstanceUid() const {
    return m_sop_instance_uid;
}
void OAIImage::setSopInstanceUid(const OAIDicomPropertyValue &sop_instance_uid) {
    m_sop_instance_uid = sop_instance_uid;
    m_sop_instance_uid_isSet = true;
}

bool OAIImage::is_sop_instance_uid_Set() const{
    return m_sop_instance_uid_isSet;
}

bool OAIImage::is_sop_instance_uid_Valid() const{
    return m_sop_instance_uid_isValid;
}

bool OAIImage::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_instance_number.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_series_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sop_instance_uid.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImage::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
