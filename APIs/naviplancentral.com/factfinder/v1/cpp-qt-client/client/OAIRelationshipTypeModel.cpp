/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRelationshipTypeModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRelationshipTypeModel::OAIRelationshipTypeModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRelationshipTypeModel::OAIRelationshipTypeModel() {
    this->initializeModel();
}

OAIRelationshipTypeModel::~OAIRelationshipTypeModel() {}

void OAIRelationshipTypeModel::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_child_type_isSet = false;
    m_is_child_type_isValid = false;

    m_relationship_type_isSet = false;
    m_relationship_type_isValid = false;
}

void OAIRelationshipTypeModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRelationshipTypeModel::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_child_type_isValid = ::OpenAPI::fromJsonValue(m_is_child_type, json[QString("isChildType")]);
    m_is_child_type_isSet = !json[QString("isChildType")].isNull() && m_is_child_type_isValid;

    m_relationship_type_isValid = ::OpenAPI::fromJsonValue(m_relationship_type, json[QString("relationshipType")]);
    m_relationship_type_isSet = !json[QString("relationshipType")].isNull() && m_relationship_type_isValid;
}

QString OAIRelationshipTypeModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRelationshipTypeModel::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_child_type_isSet) {
        obj.insert(QString("isChildType"), ::OpenAPI::toJsonValue(m_is_child_type));
    }
    if (m_relationship_type_isSet) {
        obj.insert(QString("relationshipType"), ::OpenAPI::toJsonValue(m_relationship_type));
    }
    return obj;
}

qint32 OAIRelationshipTypeModel::getId() const {
    return m_id;
}
void OAIRelationshipTypeModel::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRelationshipTypeModel::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRelationshipTypeModel::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIRelationshipTypeModel::isIsChildType() const {
    return m_is_child_type;
}
void OAIRelationshipTypeModel::setIsChildType(const bool &is_child_type) {
    m_is_child_type = is_child_type;
    m_is_child_type_isSet = true;
}

bool OAIRelationshipTypeModel::is_is_child_type_Set() const{
    return m_is_child_type_isSet;
}

bool OAIRelationshipTypeModel::is_is_child_type_Valid() const{
    return m_is_child_type_isValid;
}

QString OAIRelationshipTypeModel::getRelationshipType() const {
    return m_relationship_type;
}
void OAIRelationshipTypeModel::setRelationshipType(const QString &relationship_type) {
    m_relationship_type = relationship_type;
    m_relationship_type_isSet = true;
}

bool OAIRelationshipTypeModel::is_relationship_type_Set() const{
    return m_relationship_type_isSet;
}

bool OAIRelationshipTypeModel::is_relationship_type_Valid() const{
    return m_relationship_type_isValid;
}

bool OAIRelationshipTypeModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_child_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relationship_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRelationshipTypeModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
