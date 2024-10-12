/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApplicationPackage.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApplicationPackage::OAIApplicationPackage(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApplicationPackage::OAIApplicationPackage() {
    this->initializeModel();
}

OAIApplicationPackage::~OAIApplicationPackage() {}

void OAIApplicationPackage::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_etag_isSet = false;
    m_etag_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIApplicationPackage::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApplicationPackage::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_etag_isValid = ::OpenAPI::fromJsonValue(m_etag, json[QString("etag")]);
    m_etag_isSet = !json[QString("etag")].isNull() && m_etag_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIApplicationPackage::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApplicationPackage::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_etag_isSet) {
        obj.insert(QString("etag"), ::OpenAPI::toJsonValue(m_etag));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIApplicationPackageProperties OAIApplicationPackage::getProperties() const {
    return m_properties;
}
void OAIApplicationPackage::setProperties(const OAIApplicationPackageProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIApplicationPackage::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIApplicationPackage::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIApplicationPackage::getEtag() const {
    return m_etag;
}
void OAIApplicationPackage::setEtag(const QString &etag) {
    m_etag = etag;
    m_etag_isSet = true;
}

bool OAIApplicationPackage::is_etag_Set() const{
    return m_etag_isSet;
}

bool OAIApplicationPackage::is_etag_Valid() const{
    return m_etag_isValid;
}

QString OAIApplicationPackage::getId() const {
    return m_id;
}
void OAIApplicationPackage::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIApplicationPackage::is_id_Set() const{
    return m_id_isSet;
}

bool OAIApplicationPackage::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIApplicationPackage::getName() const {
    return m_name;
}
void OAIApplicationPackage::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIApplicationPackage::is_name_Set() const{
    return m_name_isSet;
}

bool OAIApplicationPackage::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIApplicationPackage::getType() const {
    return m_type;
}
void OAIApplicationPackage::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIApplicationPackage::is_type_Set() const{
    return m_type_isSet;
}

bool OAIApplicationPackage::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIApplicationPackage::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_etag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

bool OAIApplicationPackage::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
