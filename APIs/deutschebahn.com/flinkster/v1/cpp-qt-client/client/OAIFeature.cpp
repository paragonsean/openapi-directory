/**
 * Flinkster_API_NG
 * This REST-API enables you to query for private transport sharing offers provided by companies and cities in Germany, Netherland and Austria.  You can search for informations about the rental stations (points or areas) where you can find the rentals by utilizing the /areas/ ressource.  With the help of the proximity search in the /bookingproposals/ URI you can request the availabilities of the rentalobjects for spontaneous or planed usage in the future.   Feel free to browse through data by setting the parameter 'providernetwork' to the value:   1: Search for car sharing offers provided by the Flinkster platform (http://www.flinkster.de) 2: Finding bike rental offers from Call a Bike (http://www.callabike.de)   You can find more details in the documentation section (Unfortunately only available in german language).  Have lots of fun and we are lucky to take notice of your products or getting your feedback.
 *
 * The version of the OpenAPI document: v1
 * Contact: partner@flinkster.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFeature.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFeature::OAIFeature(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFeature::OAIFeature() {
    this->initializeModel();
}

OAIFeature::~OAIFeature() {}

void OAIFeature::initializeModel() {

    m_bbox_isSet = false;
    m_bbox_isValid = false;

    m_crs_isSet = false;
    m_crs_isValid = false;

    m_geometry_isSet = false;
    m_geometry_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIFeature::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFeature::fromJsonObject(QJsonObject json) {

    m_bbox_isValid = ::OpenAPI::fromJsonValue(m_bbox, json[QString("bbox")]);
    m_bbox_isSet = !json[QString("bbox")].isNull() && m_bbox_isValid;

    m_crs_isValid = ::OpenAPI::fromJsonValue(m_crs, json[QString("crs")]);
    m_crs_isSet = !json[QString("crs")].isNull() && m_crs_isValid;

    m_geometry_isValid = ::OpenAPI::fromJsonValue(m_geometry, json[QString("geometry")]);
    m_geometry_isSet = !json[QString("geometry")].isNull() && m_geometry_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIFeature::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFeature::asJsonObject() const {
    QJsonObject obj;
    if (m_bbox.size() > 0) {
        obj.insert(QString("bbox"), ::OpenAPI::toJsonValue(m_bbox));
    }
    if (m_crs.isSet()) {
        obj.insert(QString("crs"), ::OpenAPI::toJsonValue(m_crs));
    }
    if (m_geometry.isSet()) {
        obj.insert(QString("geometry"), ::OpenAPI::toJsonValue(m_geometry));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_properties.size() > 0) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

QList<double> OAIFeature::getBbox() const {
    return m_bbox;
}
void OAIFeature::setBbox(const QList<double> &bbox) {
    m_bbox = bbox;
    m_bbox_isSet = true;
}

bool OAIFeature::is_bbox_Set() const{
    return m_bbox_isSet;
}

bool OAIFeature::is_bbox_Valid() const{
    return m_bbox_isValid;
}

OAICrs OAIFeature::getCrs() const {
    return m_crs;
}
void OAIFeature::setCrs(const OAICrs &crs) {
    m_crs = crs;
    m_crs_isSet = true;
}

bool OAIFeature::is_crs_Set() const{
    return m_crs_isSet;
}

bool OAIFeature::is_crs_Valid() const{
    return m_crs_isValid;
}

OAIGeoJsonObject OAIFeature::getGeometry() const {
    return m_geometry;
}
void OAIFeature::setGeometry(const OAIGeoJsonObject &geometry) {
    m_geometry = geometry;
    m_geometry_isSet = true;
}

bool OAIFeature::is_geometry_Set() const{
    return m_geometry_isSet;
}

bool OAIFeature::is_geometry_Valid() const{
    return m_geometry_isValid;
}

QString OAIFeature::getId() const {
    return m_id;
}
void OAIFeature::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIFeature::is_id_Set() const{
    return m_id_isSet;
}

bool OAIFeature::is_id_Valid() const{
    return m_id_isValid;
}

QMap<QString, OAIObject> OAIFeature::getProperties() const {
    return m_properties;
}
void OAIFeature::setProperties(const QMap<QString, OAIObject> &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIFeature::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIFeature::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIFeature::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bbox.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_crs.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_geometry.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFeature::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
