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

#include "OAIShared_ColorTransformationAttributes_Details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShared_ColorTransformationAttributes_Details::OAIShared_ColorTransformationAttributes_Details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShared_ColorTransformationAttributes_Details::OAIShared_ColorTransformationAttributes_Details() {
    this->initializeModel();
}

OAIShared_ColorTransformationAttributes_Details::~OAIShared_ColorTransformationAttributes_Details() {}

void OAIShared_ColorTransformationAttributes_Details::initializeModel() {

    m_color_transformation_isSet = false;
    m_color_transformation_isValid = false;

    m_color_transformations_id_isSet = false;
    m_color_transformations_id_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_modified_isSet = false;
    m_date_modified_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_user_created_isSet = false;
    m_user_created_isValid = false;

    m_user_modified_isSet = false;
    m_user_modified_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIShared_ColorTransformationAttributes_Details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShared_ColorTransformationAttributes_Details::fromJsonObject(QJsonObject json) {

    m_color_transformation_isValid = ::OpenAPI::fromJsonValue(m_color_transformation, json[QString("colorTransformation")]);
    m_color_transformation_isSet = !json[QString("colorTransformation")].isNull() && m_color_transformation_isValid;

    m_color_transformations_id_isValid = ::OpenAPI::fromJsonValue(m_color_transformations_id, json[QString("colorTransformationsId")]);
    m_color_transformations_id_isSet = !json[QString("colorTransformationsId")].isNull() && m_color_transformations_id_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("dateCreated")]);
    m_date_created_isSet = !json[QString("dateCreated")].isNull() && m_date_created_isValid;

    m_date_modified_isValid = ::OpenAPI::fromJsonValue(m_date_modified, json[QString("dateModified")]);
    m_date_modified_isSet = !json[QString("dateModified")].isNull() && m_date_modified_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_user_created_isValid = ::OpenAPI::fromJsonValue(m_user_created, json[QString("userCreated")]);
    m_user_created_isSet = !json[QString("userCreated")].isNull() && m_user_created_isValid;

    m_user_modified_isValid = ::OpenAPI::fromJsonValue(m_user_modified, json[QString("userModified")]);
    m_user_modified_isSet = !json[QString("userModified")].isNull() && m_user_modified_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIShared_ColorTransformationAttributes_Details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShared_ColorTransformationAttributes_Details::asJsonObject() const {
    QJsonObject obj;
    if (m_color_transformation.isSet()) {
        obj.insert(QString("colorTransformation"), ::OpenAPI::toJsonValue(m_color_transformation));
    }
    if (m_color_transformations_id_isSet) {
        obj.insert(QString("colorTransformationsId"), ::OpenAPI::toJsonValue(m_color_transformations_id));
    }
    if (m_date_created_isSet) {
        obj.insert(QString("dateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_date_modified_isSet) {
        obj.insert(QString("dateModified"), ::OpenAPI::toJsonValue(m_date_modified));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_user_created_isSet) {
        obj.insert(QString("userCreated"), ::OpenAPI::toJsonValue(m_user_created));
    }
    if (m_user_modified_isSet) {
        obj.insert(QString("userModified"), ::OpenAPI::toJsonValue(m_user_modified));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

OAIShared_ColorTransformations_Details OAIShared_ColorTransformationAttributes_Details::getColorTransformation() const {
    return m_color_transformation;
}
void OAIShared_ColorTransformationAttributes_Details::setColorTransformation(const OAIShared_ColorTransformations_Details &color_transformation) {
    m_color_transformation = color_transformation;
    m_color_transformation_isSet = true;
}

bool OAIShared_ColorTransformationAttributes_Details::is_color_transformation_Set() const{
    return m_color_transformation_isSet;
}

bool OAIShared_ColorTransformationAttributes_Details::is_color_transformation_Valid() const{
    return m_color_transformation_isValid;
}

QString OAIShared_ColorTransformationAttributes_Details::getColorTransformationsId() const {
    return m_color_transformations_id;
}
void OAIShared_ColorTransformationAttributes_Details::setColorTransformationsId(const QString &color_transformations_id) {
    m_color_transformations_id = color_transformations_id;
    m_color_transformations_id_isSet = true;
}

bool OAIShared_ColorTransformationAttributes_Details::is_color_transformations_id_Set() const{
    return m_color_transformations_id_isSet;
}

bool OAIShared_ColorTransformationAttributes_Details::is_color_transformations_id_Valid() const{
    return m_color_transformations_id_isValid;
}

QDateTime OAIShared_ColorTransformationAttributes_Details::getDateCreated() const {
    return m_date_created;
}
void OAIShared_ColorTransformationAttributes_Details::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAIShared_ColorTransformationAttributes_Details::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAIShared_ColorTransformationAttributes_Details::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAIShared_ColorTransformationAttributes_Details::getDateModified() const {
    return m_date_modified;
}
void OAIShared_ColorTransformationAttributes_Details::setDateModified(const QDateTime &date_modified) {
    m_date_modified = date_modified;
    m_date_modified_isSet = true;
}

bool OAIShared_ColorTransformationAttributes_Details::is_date_modified_Set() const{
    return m_date_modified_isSet;
}

bool OAIShared_ColorTransformationAttributes_Details::is_date_modified_Valid() const{
    return m_date_modified_isValid;
}

QString OAIShared_ColorTransformationAttributes_Details::getId() const {
    return m_id;
}
void OAIShared_ColorTransformationAttributes_Details::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIShared_ColorTransformationAttributes_Details::is_id_Set() const{
    return m_id_isSet;
}

bool OAIShared_ColorTransformationAttributes_Details::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIShared_ColorTransformationAttributes_Details::getName() const {
    return m_name;
}
void OAIShared_ColorTransformationAttributes_Details::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIShared_ColorTransformationAttributes_Details::is_name_Set() const{
    return m_name_isSet;
}

bool OAIShared_ColorTransformationAttributes_Details::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIShared_ColorTransformationAttributes_Details::getUserCreated() const {
    return m_user_created;
}
void OAIShared_ColorTransformationAttributes_Details::setUserCreated(const QString &user_created) {
    m_user_created = user_created;
    m_user_created_isSet = true;
}

bool OAIShared_ColorTransformationAttributes_Details::is_user_created_Set() const{
    return m_user_created_isSet;
}

bool OAIShared_ColorTransformationAttributes_Details::is_user_created_Valid() const{
    return m_user_created_isValid;
}

QString OAIShared_ColorTransformationAttributes_Details::getUserModified() const {
    return m_user_modified;
}
void OAIShared_ColorTransformationAttributes_Details::setUserModified(const QString &user_modified) {
    m_user_modified = user_modified;
    m_user_modified_isSet = true;
}

bool OAIShared_ColorTransformationAttributes_Details::is_user_modified_Set() const{
    return m_user_modified_isSet;
}

bool OAIShared_ColorTransformationAttributes_Details::is_user_modified_Valid() const{
    return m_user_modified_isValid;
}

QString OAIShared_ColorTransformationAttributes_Details::getValue() const {
    return m_value;
}
void OAIShared_ColorTransformationAttributes_Details::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIShared_ColorTransformationAttributes_Details::is_value_Set() const{
    return m_value_isSet;
}

bool OAIShared_ColorTransformationAttributes_Details::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIShared_ColorTransformationAttributes_Details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_color_transformation.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_color_transformations_id_isSet) {
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

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShared_ColorTransformationAttributes_Details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
