/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIShared_Effects_Details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShared_Effects_Details::OAIShared_Effects_Details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShared_Effects_Details::OAIShared_Effects_Details() {
    this->initializeModel();
}

OAIShared_Effects_Details::~OAIShared_Effects_Details() {}

void OAIShared_Effects_Details::initializeModel() {

    m_connector_id_isSet = false;
    m_connector_id_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_modified_isSet = false;
    m_date_modified_isValid = false;

    m_effect_attributes_isSet = false;
    m_effect_attributes_isValid = false;

    m_effect_map_isSet = false;
    m_effect_map_isValid = false;

    m_effect_map_id_isSet = false;
    m_effect_map_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_parent_connector_isSet = false;
    m_parent_connector_isValid = false;

    m_parent_shape_isSet = false;
    m_parent_shape_isValid = false;

    m_shape_id_isSet = false;
    m_shape_id_isValid = false;

    m_user_created_isSet = false;
    m_user_created_isValid = false;

    m_user_modified_isSet = false;
    m_user_modified_isValid = false;
}

void OAIShared_Effects_Details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShared_Effects_Details::fromJsonObject(QJsonObject json) {

    m_connector_id_isValid = ::OpenAPI::fromJsonValue(m_connector_id, json[QString("connectorId")]);
    m_connector_id_isSet = !json[QString("connectorId")].isNull() && m_connector_id_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("dateCreated")]);
    m_date_created_isSet = !json[QString("dateCreated")].isNull() && m_date_created_isValid;

    m_date_modified_isValid = ::OpenAPI::fromJsonValue(m_date_modified, json[QString("dateModified")]);
    m_date_modified_isSet = !json[QString("dateModified")].isNull() && m_date_modified_isValid;

    m_effect_attributes_isValid = ::OpenAPI::fromJsonValue(m_effect_attributes, json[QString("effectAttributes")]);
    m_effect_attributes_isSet = !json[QString("effectAttributes")].isNull() && m_effect_attributes_isValid;

    m_effect_map_isValid = ::OpenAPI::fromJsonValue(m_effect_map, json[QString("effectMap")]);
    m_effect_map_isSet = !json[QString("effectMap")].isNull() && m_effect_map_isValid;

    m_effect_map_id_isValid = ::OpenAPI::fromJsonValue(m_effect_map_id, json[QString("effectMapId")]);
    m_effect_map_id_isSet = !json[QString("effectMapId")].isNull() && m_effect_map_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_parent_connector_isValid = ::OpenAPI::fromJsonValue(m_parent_connector, json[QString("parentConnector")]);
    m_parent_connector_isSet = !json[QString("parentConnector")].isNull() && m_parent_connector_isValid;

    m_parent_shape_isValid = ::OpenAPI::fromJsonValue(m_parent_shape, json[QString("parentShape")]);
    m_parent_shape_isSet = !json[QString("parentShape")].isNull() && m_parent_shape_isValid;

    m_shape_id_isValid = ::OpenAPI::fromJsonValue(m_shape_id, json[QString("shapeId")]);
    m_shape_id_isSet = !json[QString("shapeId")].isNull() && m_shape_id_isValid;

    m_user_created_isValid = ::OpenAPI::fromJsonValue(m_user_created, json[QString("userCreated")]);
    m_user_created_isSet = !json[QString("userCreated")].isNull() && m_user_created_isValid;

    m_user_modified_isValid = ::OpenAPI::fromJsonValue(m_user_modified, json[QString("userModified")]);
    m_user_modified_isSet = !json[QString("userModified")].isNull() && m_user_modified_isValid;
}

QString OAIShared_Effects_Details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShared_Effects_Details::asJsonObject() const {
    QJsonObject obj;
    if (m_connector_id_isSet) {
        obj.insert(QString("connectorId"), ::OpenAPI::toJsonValue(m_connector_id));
    }
    if (m_date_created_isSet) {
        obj.insert(QString("dateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_date_modified_isSet) {
        obj.insert(QString("dateModified"), ::OpenAPI::toJsonValue(m_date_modified));
    }
    if (m_effect_attributes.size() > 0) {
        obj.insert(QString("effectAttributes"), ::OpenAPI::toJsonValue(m_effect_attributes));
    }
    if (m_effect_map.isSet()) {
        obj.insert(QString("effectMap"), ::OpenAPI::toJsonValue(m_effect_map));
    }
    if (m_effect_map_id_isSet) {
        obj.insert(QString("effectMapId"), ::OpenAPI::toJsonValue(m_effect_map_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_parent_connector.isSet()) {
        obj.insert(QString("parentConnector"), ::OpenAPI::toJsonValue(m_parent_connector));
    }
    if (m_parent_shape.isSet()) {
        obj.insert(QString("parentShape"), ::OpenAPI::toJsonValue(m_parent_shape));
    }
    if (m_shape_id_isSet) {
        obj.insert(QString("shapeId"), ::OpenAPI::toJsonValue(m_shape_id));
    }
    if (m_user_created_isSet) {
        obj.insert(QString("userCreated"), ::OpenAPI::toJsonValue(m_user_created));
    }
    if (m_user_modified_isSet) {
        obj.insert(QString("userModified"), ::OpenAPI::toJsonValue(m_user_modified));
    }
    return obj;
}

QString OAIShared_Effects_Details::getConnectorId() const {
    return m_connector_id;
}
void OAIShared_Effects_Details::setConnectorId(const QString &connector_id) {
    m_connector_id = connector_id;
    m_connector_id_isSet = true;
}

bool OAIShared_Effects_Details::is_connector_id_Set() const{
    return m_connector_id_isSet;
}

bool OAIShared_Effects_Details::is_connector_id_Valid() const{
    return m_connector_id_isValid;
}

QDateTime OAIShared_Effects_Details::getDateCreated() const {
    return m_date_created;
}
void OAIShared_Effects_Details::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAIShared_Effects_Details::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAIShared_Effects_Details::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAIShared_Effects_Details::getDateModified() const {
    return m_date_modified;
}
void OAIShared_Effects_Details::setDateModified(const QDateTime &date_modified) {
    m_date_modified = date_modified;
    m_date_modified_isSet = true;
}

bool OAIShared_Effects_Details::is_date_modified_Set() const{
    return m_date_modified_isSet;
}

bool OAIShared_Effects_Details::is_date_modified_Valid() const{
    return m_date_modified_isValid;
}

QList<OAIShared_EffectAttributes_Details> OAIShared_Effects_Details::getEffectAttributes() const {
    return m_effect_attributes;
}
void OAIShared_Effects_Details::setEffectAttributes(const QList<OAIShared_EffectAttributes_Details> &effect_attributes) {
    m_effect_attributes = effect_attributes;
    m_effect_attributes_isSet = true;
}

bool OAIShared_Effects_Details::is_effect_attributes_Set() const{
    return m_effect_attributes_isSet;
}

bool OAIShared_Effects_Details::is_effect_attributes_Valid() const{
    return m_effect_attributes_isValid;
}

OAITheme_EffectMap_Details OAIShared_Effects_Details::getEffectMap() const {
    return m_effect_map;
}
void OAIShared_Effects_Details::setEffectMap(const OAITheme_EffectMap_Details &effect_map) {
    m_effect_map = effect_map;
    m_effect_map_isSet = true;
}

bool OAIShared_Effects_Details::is_effect_map_Set() const{
    return m_effect_map_isSet;
}

bool OAIShared_Effects_Details::is_effect_map_Valid() const{
    return m_effect_map_isValid;
}

QString OAIShared_Effects_Details::getEffectMapId() const {
    return m_effect_map_id;
}
void OAIShared_Effects_Details::setEffectMapId(const QString &effect_map_id) {
    m_effect_map_id = effect_map_id;
    m_effect_map_id_isSet = true;
}

bool OAIShared_Effects_Details::is_effect_map_id_Set() const{
    return m_effect_map_id_isSet;
}

bool OAIShared_Effects_Details::is_effect_map_id_Valid() const{
    return m_effect_map_id_isValid;
}

QString OAIShared_Effects_Details::getId() const {
    return m_id;
}
void OAIShared_Effects_Details::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIShared_Effects_Details::is_id_Set() const{
    return m_id_isSet;
}

bool OAIShared_Effects_Details::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIShared_Effects_Details::getName() const {
    return m_name;
}
void OAIShared_Effects_Details::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIShared_Effects_Details::is_name_Set() const{
    return m_name_isSet;
}

bool OAIShared_Effects_Details::is_name_Valid() const{
    return m_name_isValid;
}

OAISlide_Connector_Details OAIShared_Effects_Details::getParentConnector() const {
    return m_parent_connector;
}
void OAIShared_Effects_Details::setParentConnector(const OAISlide_Connector_Details &parent_connector) {
    m_parent_connector = parent_connector;
    m_parent_connector_isSet = true;
}

bool OAIShared_Effects_Details::is_parent_connector_Set() const{
    return m_parent_connector_isSet;
}

bool OAIShared_Effects_Details::is_parent_connector_Valid() const{
    return m_parent_connector_isValid;
}

OAISlide_Shapes_Details OAIShared_Effects_Details::getParentShape() const {
    return m_parent_shape;
}
void OAIShared_Effects_Details::setParentShape(const OAISlide_Shapes_Details &parent_shape) {
    m_parent_shape = parent_shape;
    m_parent_shape_isSet = true;
}

bool OAIShared_Effects_Details::is_parent_shape_Set() const{
    return m_parent_shape_isSet;
}

bool OAIShared_Effects_Details::is_parent_shape_Valid() const{
    return m_parent_shape_isValid;
}

QString OAIShared_Effects_Details::getShapeId() const {
    return m_shape_id;
}
void OAIShared_Effects_Details::setShapeId(const QString &shape_id) {
    m_shape_id = shape_id;
    m_shape_id_isSet = true;
}

bool OAIShared_Effects_Details::is_shape_id_Set() const{
    return m_shape_id_isSet;
}

bool OAIShared_Effects_Details::is_shape_id_Valid() const{
    return m_shape_id_isValid;
}

QString OAIShared_Effects_Details::getUserCreated() const {
    return m_user_created;
}
void OAIShared_Effects_Details::setUserCreated(const QString &user_created) {
    m_user_created = user_created;
    m_user_created_isSet = true;
}

bool OAIShared_Effects_Details::is_user_created_Set() const{
    return m_user_created_isSet;
}

bool OAIShared_Effects_Details::is_user_created_Valid() const{
    return m_user_created_isValid;
}

QString OAIShared_Effects_Details::getUserModified() const {
    return m_user_modified;
}
void OAIShared_Effects_Details::setUserModified(const QString &user_modified) {
    m_user_modified = user_modified;
    m_user_modified_isSet = true;
}

bool OAIShared_Effects_Details::is_user_modified_Set() const{
    return m_user_modified_isSet;
}

bool OAIShared_Effects_Details::is_user_modified_Valid() const{
    return m_user_modified_isValid;
}

bool OAIShared_Effects_Details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_connector_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_effect_attributes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_effect_map.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_effect_map_id_isSet) {
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

        if (m_parent_connector.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_shape.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_shape_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_modified_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShared_Effects_Details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
