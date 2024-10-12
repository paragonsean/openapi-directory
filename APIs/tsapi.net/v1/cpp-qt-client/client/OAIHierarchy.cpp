/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHierarchy.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHierarchy::OAIHierarchy(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHierarchy::OAIHierarchy() {
    this->initializeModel();
}

OAIHierarchy::~OAIHierarchy() {}

void OAIHierarchy::initializeModel() {

    m_ident_isSet = false;
    m_ident_isValid = false;

    m_metadata_isSet = false;
    m_metadata_isValid = false;

    m_parent_isSet = false;
    m_parent_isValid = false;
}

void OAIHierarchy::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHierarchy::fromJsonObject(QJsonObject json) {

    m_ident_isValid = ::OpenAPI::fromJsonValue(m_ident, json[QString("ident")]);
    m_ident_isSet = !json[QString("ident")].isNull() && m_ident_isValid;

    m_metadata_isValid = ::OpenAPI::fromJsonValue(m_metadata, json[QString("metadata")]);
    m_metadata_isSet = !json[QString("metadata")].isNull() && m_metadata_isValid;

    m_parent_isValid = ::OpenAPI::fromJsonValue(m_parent, json[QString("parent")]);
    m_parent_isSet = !json[QString("parent")].isNull() && m_parent_isValid;
}

QString OAIHierarchy::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHierarchy::asJsonObject() const {
    QJsonObject obj;
    if (m_ident_isSet) {
        obj.insert(QString("ident"), ::OpenAPI::toJsonValue(m_ident));
    }
    if (m_metadata.isSet()) {
        obj.insert(QString("metadata"), ::OpenAPI::toJsonValue(m_metadata));
    }
    if (m_parent.isSet()) {
        obj.insert(QString("parent"), ::OpenAPI::toJsonValue(m_parent));
    }
    return obj;
}

QString OAIHierarchy::getIdent() const {
    return m_ident;
}
void OAIHierarchy::setIdent(const QString &ident) {
    m_ident = ident;
    m_ident_isSet = true;
}

bool OAIHierarchy::is_ident_Set() const{
    return m_ident_isSet;
}

bool OAIHierarchy::is_ident_Valid() const{
    return m_ident_isValid;
}

OAISurveyMetadataBase OAIHierarchy::getMetadata() const {
    return m_metadata;
}
void OAIHierarchy::setMetadata(const OAISurveyMetadataBase &metadata) {
    m_metadata = metadata;
    m_metadata_isSet = true;
}

bool OAIHierarchy::is_metadata_Set() const{
    return m_metadata_isSet;
}

bool OAIHierarchy::is_metadata_Valid() const{
    return m_metadata_isValid;
}

OAIParentDetails OAIHierarchy::getParent() const {
    return m_parent;
}
void OAIHierarchy::setParent(const OAIParentDetails &parent) {
    m_parent = parent;
    m_parent_isSet = true;
}

bool OAIHierarchy::is_parent_Set() const{
    return m_parent_isSet;
}

bool OAIHierarchy::is_parent_Valid() const{
    return m_parent_isValid;
}

bool OAIHierarchy::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ident_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHierarchy::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
