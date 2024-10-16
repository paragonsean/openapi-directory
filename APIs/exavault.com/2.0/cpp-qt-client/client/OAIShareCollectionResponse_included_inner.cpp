/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIShareCollectionResponse_included_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShareCollectionResponse_included_inner::OAIShareCollectionResponse_included_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShareCollectionResponse_included_inner::OAIShareCollectionResponse_included_inner() {
    this->initializeModel();
}

OAIShareCollectionResponse_included_inner::~OAIShareCollectionResponse_included_inner() {}

void OAIShareCollectionResponse_included_inner::initializeModel() {

    m_attributes_isSet = false;
    m_attributes_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_relationships_isSet = false;
    m_relationships_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIShareCollectionResponse_included_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShareCollectionResponse_included_inner::fromJsonObject(QJsonObject json) {

    m_attributes_isValid = ::OpenAPI::fromJsonValue(m_attributes, json[QString("attributes")]);
    m_attributes_isSet = !json[QString("attributes")].isNull() && m_attributes_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_relationships_isValid = ::OpenAPI::fromJsonValue(m_relationships, json[QString("relationships")]);
    m_relationships_isSet = !json[QString("relationships")].isNull() && m_relationships_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIShareCollectionResponse_included_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShareCollectionResponse_included_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_attributes.isSet()) {
        obj.insert(QString("attributes"), ::OpenAPI::toJsonValue(m_attributes));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_relationships.isSet()) {
        obj.insert(QString("relationships"), ::OpenAPI::toJsonValue(m_relationships));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIResourceAttributes OAIShareCollectionResponse_included_inner::getAttributes() const {
    return m_attributes;
}
void OAIShareCollectionResponse_included_inner::setAttributes(const OAIResourceAttributes &attributes) {
    m_attributes = attributes;
    m_attributes_isSet = true;
}

bool OAIShareCollectionResponse_included_inner::is_attributes_Set() const{
    return m_attributes_isSet;
}

bool OAIShareCollectionResponse_included_inner::is_attributes_Valid() const{
    return m_attributes_isValid;
}

qint64 OAIShareCollectionResponse_included_inner::getId() const {
    return m_id;
}
void OAIShareCollectionResponse_included_inner::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIShareCollectionResponse_included_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIShareCollectionResponse_included_inner::is_id_Valid() const{
    return m_id_isValid;
}

OAIResource_relationships OAIShareCollectionResponse_included_inner::getRelationships() const {
    return m_relationships;
}
void OAIShareCollectionResponse_included_inner::setRelationships(const OAIResource_relationships &relationships) {
    m_relationships = relationships;
    m_relationships_isSet = true;
}

bool OAIShareCollectionResponse_included_inner::is_relationships_Set() const{
    return m_relationships_isSet;
}

bool OAIShareCollectionResponse_included_inner::is_relationships_Valid() const{
    return m_relationships_isValid;
}

QString OAIShareCollectionResponse_included_inner::getType() const {
    return m_type;
}
void OAIShareCollectionResponse_included_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIShareCollectionResponse_included_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIShareCollectionResponse_included_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIShareCollectionResponse_included_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_attributes.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relationships.isSet()) {
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

bool OAIShareCollectionResponse_included_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
