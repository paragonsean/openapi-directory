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

#include "OAIShared_SolidFills_Details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShared_SolidFills_Details::OAIShared_SolidFills_Details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShared_SolidFills_Details::OAIShared_SolidFills_Details() {
    this->initializeModel();
}

OAIShared_SolidFills_Details::~OAIShared_SolidFills_Details() {}

void OAIShared_SolidFills_Details::initializeModel() {

    m_color_transformations_isSet = false;
    m_color_transformations_isValid = false;

    m_color_type_id_isSet = false;
    m_color_type_id_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_modified_isSet = false;
    m_date_modified_isValid = false;

    m_fill_map_id_isSet = false;
    m_fill_map_id_isValid = false;

    m_hex_value_isSet = false;
    m_hex_value_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_user_color_isSet = false;
    m_is_user_color_isValid = false;

    m_parent_fill_map_isSet = false;
    m_parent_fill_map_isValid = false;

    m_parent_gradient_stop_isSet = false;
    m_parent_gradient_stop_isValid = false;

    m_parent_gradient_stop_id_isSet = false;
    m_parent_gradient_stop_id_isValid = false;

    m_parent_line_isSet = false;
    m_parent_line_isValid = false;

    m_parent_line_id_isSet = false;
    m_parent_line_id_isValid = false;

    m_parent_text_isSet = false;
    m_parent_text_isValid = false;

    m_parent_text_id_isSet = false;
    m_parent_text_id_isValid = false;

    m_user_created_isSet = false;
    m_user_created_isValid = false;

    m_user_modified_isSet = false;
    m_user_modified_isValid = false;
}

void OAIShared_SolidFills_Details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShared_SolidFills_Details::fromJsonObject(QJsonObject json) {

    m_color_transformations_isValid = ::OpenAPI::fromJsonValue(m_color_transformations, json[QString("colorTransformations")]);
    m_color_transformations_isSet = !json[QString("colorTransformations")].isNull() && m_color_transformations_isValid;

    m_color_type_id_isValid = ::OpenAPI::fromJsonValue(m_color_type_id, json[QString("colorTypeId")]);
    m_color_type_id_isSet = !json[QString("colorTypeId")].isNull() && m_color_type_id_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("dateCreated")]);
    m_date_created_isSet = !json[QString("dateCreated")].isNull() && m_date_created_isValid;

    m_date_modified_isValid = ::OpenAPI::fromJsonValue(m_date_modified, json[QString("dateModified")]);
    m_date_modified_isSet = !json[QString("dateModified")].isNull() && m_date_modified_isValid;

    m_fill_map_id_isValid = ::OpenAPI::fromJsonValue(m_fill_map_id, json[QString("fillMapId")]);
    m_fill_map_id_isSet = !json[QString("fillMapId")].isNull() && m_fill_map_id_isValid;

    m_hex_value_isValid = ::OpenAPI::fromJsonValue(m_hex_value, json[QString("hexValue")]);
    m_hex_value_isSet = !json[QString("hexValue")].isNull() && m_hex_value_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_user_color_isValid = ::OpenAPI::fromJsonValue(m_is_user_color, json[QString("isUserColor")]);
    m_is_user_color_isSet = !json[QString("isUserColor")].isNull() && m_is_user_color_isValid;

    m_parent_fill_map_isValid = ::OpenAPI::fromJsonValue(m_parent_fill_map, json[QString("parentFillMap")]);
    m_parent_fill_map_isSet = !json[QString("parentFillMap")].isNull() && m_parent_fill_map_isValid;

    m_parent_gradient_stop_isValid = ::OpenAPI::fromJsonValue(m_parent_gradient_stop, json[QString("parentGradientStop")]);
    m_parent_gradient_stop_isSet = !json[QString("parentGradientStop")].isNull() && m_parent_gradient_stop_isValid;

    m_parent_gradient_stop_id_isValid = ::OpenAPI::fromJsonValue(m_parent_gradient_stop_id, json[QString("parentGradientStopId")]);
    m_parent_gradient_stop_id_isSet = !json[QString("parentGradientStopId")].isNull() && m_parent_gradient_stop_id_isValid;

    m_parent_line_isValid = ::OpenAPI::fromJsonValue(m_parent_line, json[QString("parentLine")]);
    m_parent_line_isSet = !json[QString("parentLine")].isNull() && m_parent_line_isValid;

    m_parent_line_id_isValid = ::OpenAPI::fromJsonValue(m_parent_line_id, json[QString("parentLineId")]);
    m_parent_line_id_isSet = !json[QString("parentLineId")].isNull() && m_parent_line_id_isValid;

    m_parent_text_isValid = ::OpenAPI::fromJsonValue(m_parent_text, json[QString("parentText")]);
    m_parent_text_isSet = !json[QString("parentText")].isNull() && m_parent_text_isValid;

    m_parent_text_id_isValid = ::OpenAPI::fromJsonValue(m_parent_text_id, json[QString("parentTextId")]);
    m_parent_text_id_isSet = !json[QString("parentTextId")].isNull() && m_parent_text_id_isValid;

    m_user_created_isValid = ::OpenAPI::fromJsonValue(m_user_created, json[QString("userCreated")]);
    m_user_created_isSet = !json[QString("userCreated")].isNull() && m_user_created_isValid;

    m_user_modified_isValid = ::OpenAPI::fromJsonValue(m_user_modified, json[QString("userModified")]);
    m_user_modified_isSet = !json[QString("userModified")].isNull() && m_user_modified_isValid;
}

QString OAIShared_SolidFills_Details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShared_SolidFills_Details::asJsonObject() const {
    QJsonObject obj;
    if (m_color_transformations.isSet()) {
        obj.insert(QString("colorTransformations"), ::OpenAPI::toJsonValue(m_color_transformations));
    }
    if (m_color_type_id_isSet) {
        obj.insert(QString("colorTypeId"), ::OpenAPI::toJsonValue(m_color_type_id));
    }
    if (m_date_created_isSet) {
        obj.insert(QString("dateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_date_modified_isSet) {
        obj.insert(QString("dateModified"), ::OpenAPI::toJsonValue(m_date_modified));
    }
    if (m_fill_map_id_isSet) {
        obj.insert(QString("fillMapId"), ::OpenAPI::toJsonValue(m_fill_map_id));
    }
    if (m_hex_value_isSet) {
        obj.insert(QString("hexValue"), ::OpenAPI::toJsonValue(m_hex_value));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_user_color_isSet) {
        obj.insert(QString("isUserColor"), ::OpenAPI::toJsonValue(m_is_user_color));
    }
    if (m_parent_fill_map.isSet()) {
        obj.insert(QString("parentFillMap"), ::OpenAPI::toJsonValue(m_parent_fill_map));
    }
    if (m_parent_gradient_stop.isSet()) {
        obj.insert(QString("parentGradientStop"), ::OpenAPI::toJsonValue(m_parent_gradient_stop));
    }
    if (m_parent_gradient_stop_id_isSet) {
        obj.insert(QString("parentGradientStopId"), ::OpenAPI::toJsonValue(m_parent_gradient_stop_id));
    }
    if (m_parent_line.isSet()) {
        obj.insert(QString("parentLine"), ::OpenAPI::toJsonValue(m_parent_line));
    }
    if (m_parent_line_id_isSet) {
        obj.insert(QString("parentLineId"), ::OpenAPI::toJsonValue(m_parent_line_id));
    }
    if (m_parent_text.isSet()) {
        obj.insert(QString("parentText"), ::OpenAPI::toJsonValue(m_parent_text));
    }
    if (m_parent_text_id_isSet) {
        obj.insert(QString("parentTextId"), ::OpenAPI::toJsonValue(m_parent_text_id));
    }
    if (m_user_created_isSet) {
        obj.insert(QString("userCreated"), ::OpenAPI::toJsonValue(m_user_created));
    }
    if (m_user_modified_isSet) {
        obj.insert(QString("userModified"), ::OpenAPI::toJsonValue(m_user_modified));
    }
    return obj;
}

OAIShared_ColorTransformations_Details OAIShared_SolidFills_Details::getColorTransformations() const {
    return m_color_transformations;
}
void OAIShared_SolidFills_Details::setColorTransformations(const OAIShared_ColorTransformations_Details &color_transformations) {
    m_color_transformations = color_transformations;
    m_color_transformations_isSet = true;
}

bool OAIShared_SolidFills_Details::is_color_transformations_Set() const{
    return m_color_transformations_isSet;
}

bool OAIShared_SolidFills_Details::is_color_transformations_Valid() const{
    return m_color_transformations_isValid;
}

qint32 OAIShared_SolidFills_Details::getColorTypeId() const {
    return m_color_type_id;
}
void OAIShared_SolidFills_Details::setColorTypeId(const qint32 &color_type_id) {
    m_color_type_id = color_type_id;
    m_color_type_id_isSet = true;
}

bool OAIShared_SolidFills_Details::is_color_type_id_Set() const{
    return m_color_type_id_isSet;
}

bool OAIShared_SolidFills_Details::is_color_type_id_Valid() const{
    return m_color_type_id_isValid;
}

QDateTime OAIShared_SolidFills_Details::getDateCreated() const {
    return m_date_created;
}
void OAIShared_SolidFills_Details::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAIShared_SolidFills_Details::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAIShared_SolidFills_Details::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAIShared_SolidFills_Details::getDateModified() const {
    return m_date_modified;
}
void OAIShared_SolidFills_Details::setDateModified(const QDateTime &date_modified) {
    m_date_modified = date_modified;
    m_date_modified_isSet = true;
}

bool OAIShared_SolidFills_Details::is_date_modified_Set() const{
    return m_date_modified_isSet;
}

bool OAIShared_SolidFills_Details::is_date_modified_Valid() const{
    return m_date_modified_isValid;
}

QString OAIShared_SolidFills_Details::getFillMapId() const {
    return m_fill_map_id;
}
void OAIShared_SolidFills_Details::setFillMapId(const QString &fill_map_id) {
    m_fill_map_id = fill_map_id;
    m_fill_map_id_isSet = true;
}

bool OAIShared_SolidFills_Details::is_fill_map_id_Set() const{
    return m_fill_map_id_isSet;
}

bool OAIShared_SolidFills_Details::is_fill_map_id_Valid() const{
    return m_fill_map_id_isValid;
}

QString OAIShared_SolidFills_Details::getHexValue() const {
    return m_hex_value;
}
void OAIShared_SolidFills_Details::setHexValue(const QString &hex_value) {
    m_hex_value = hex_value;
    m_hex_value_isSet = true;
}

bool OAIShared_SolidFills_Details::is_hex_value_Set() const{
    return m_hex_value_isSet;
}

bool OAIShared_SolidFills_Details::is_hex_value_Valid() const{
    return m_hex_value_isValid;
}

QString OAIShared_SolidFills_Details::getId() const {
    return m_id;
}
void OAIShared_SolidFills_Details::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIShared_SolidFills_Details::is_id_Set() const{
    return m_id_isSet;
}

bool OAIShared_SolidFills_Details::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIShared_SolidFills_Details::isIsUserColor() const {
    return m_is_user_color;
}
void OAIShared_SolidFills_Details::setIsUserColor(const bool &is_user_color) {
    m_is_user_color = is_user_color;
    m_is_user_color_isSet = true;
}

bool OAIShared_SolidFills_Details::is_is_user_color_Set() const{
    return m_is_user_color_isSet;
}

bool OAIShared_SolidFills_Details::is_is_user_color_Valid() const{
    return m_is_user_color_isValid;
}

OAIShared_FillMap_Details OAIShared_SolidFills_Details::getParentFillMap() const {
    return m_parent_fill_map;
}
void OAIShared_SolidFills_Details::setParentFillMap(const OAIShared_FillMap_Details &parent_fill_map) {
    m_parent_fill_map = parent_fill_map;
    m_parent_fill_map_isSet = true;
}

bool OAIShared_SolidFills_Details::is_parent_fill_map_Set() const{
    return m_parent_fill_map_isSet;
}

bool OAIShared_SolidFills_Details::is_parent_fill_map_Valid() const{
    return m_parent_fill_map_isValid;
}

OAIShared_GradientStops_Details OAIShared_SolidFills_Details::getParentGradientStop() const {
    return m_parent_gradient_stop;
}
void OAIShared_SolidFills_Details::setParentGradientStop(const OAIShared_GradientStops_Details &parent_gradient_stop) {
    m_parent_gradient_stop = parent_gradient_stop;
    m_parent_gradient_stop_isSet = true;
}

bool OAIShared_SolidFills_Details::is_parent_gradient_stop_Set() const{
    return m_parent_gradient_stop_isSet;
}

bool OAIShared_SolidFills_Details::is_parent_gradient_stop_Valid() const{
    return m_parent_gradient_stop_isValid;
}

QString OAIShared_SolidFills_Details::getParentGradientStopId() const {
    return m_parent_gradient_stop_id;
}
void OAIShared_SolidFills_Details::setParentGradientStopId(const QString &parent_gradient_stop_id) {
    m_parent_gradient_stop_id = parent_gradient_stop_id;
    m_parent_gradient_stop_id_isSet = true;
}

bool OAIShared_SolidFills_Details::is_parent_gradient_stop_id_Set() const{
    return m_parent_gradient_stop_id_isSet;
}

bool OAIShared_SolidFills_Details::is_parent_gradient_stop_id_Valid() const{
    return m_parent_gradient_stop_id_isValid;
}

OAIShared_Lines_Details OAIShared_SolidFills_Details::getParentLine() const {
    return m_parent_line;
}
void OAIShared_SolidFills_Details::setParentLine(const OAIShared_Lines_Details &parent_line) {
    m_parent_line = parent_line;
    m_parent_line_isSet = true;
}

bool OAIShared_SolidFills_Details::is_parent_line_Set() const{
    return m_parent_line_isSet;
}

bool OAIShared_SolidFills_Details::is_parent_line_Valid() const{
    return m_parent_line_isValid;
}

QString OAIShared_SolidFills_Details::getParentLineId() const {
    return m_parent_line_id;
}
void OAIShared_SolidFills_Details::setParentLineId(const QString &parent_line_id) {
    m_parent_line_id = parent_line_id;
    m_parent_line_id_isSet = true;
}

bool OAIShared_SolidFills_Details::is_parent_line_id_Set() const{
    return m_parent_line_id_isSet;
}

bool OAIShared_SolidFills_Details::is_parent_line_id_Valid() const{
    return m_parent_line_id_isValid;
}

OAIShared_Text_Details OAIShared_SolidFills_Details::getParentText() const {
    return m_parent_text;
}
void OAIShared_SolidFills_Details::setParentText(const OAIShared_Text_Details &parent_text) {
    m_parent_text = parent_text;
    m_parent_text_isSet = true;
}

bool OAIShared_SolidFills_Details::is_parent_text_Set() const{
    return m_parent_text_isSet;
}

bool OAIShared_SolidFills_Details::is_parent_text_Valid() const{
    return m_parent_text_isValid;
}

QString OAIShared_SolidFills_Details::getParentTextId() const {
    return m_parent_text_id;
}
void OAIShared_SolidFills_Details::setParentTextId(const QString &parent_text_id) {
    m_parent_text_id = parent_text_id;
    m_parent_text_id_isSet = true;
}

bool OAIShared_SolidFills_Details::is_parent_text_id_Set() const{
    return m_parent_text_id_isSet;
}

bool OAIShared_SolidFills_Details::is_parent_text_id_Valid() const{
    return m_parent_text_id_isValid;
}

QString OAIShared_SolidFills_Details::getUserCreated() const {
    return m_user_created;
}
void OAIShared_SolidFills_Details::setUserCreated(const QString &user_created) {
    m_user_created = user_created;
    m_user_created_isSet = true;
}

bool OAIShared_SolidFills_Details::is_user_created_Set() const{
    return m_user_created_isSet;
}

bool OAIShared_SolidFills_Details::is_user_created_Valid() const{
    return m_user_created_isValid;
}

QString OAIShared_SolidFills_Details::getUserModified() const {
    return m_user_modified;
}
void OAIShared_SolidFills_Details::setUserModified(const QString &user_modified) {
    m_user_modified = user_modified;
    m_user_modified_isSet = true;
}

bool OAIShared_SolidFills_Details::is_user_modified_Set() const{
    return m_user_modified_isSet;
}

bool OAIShared_SolidFills_Details::is_user_modified_Valid() const{
    return m_user_modified_isValid;
}

bool OAIShared_SolidFills_Details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_color_transformations.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_color_type_id_isSet) {
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

        if (m_fill_map_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hex_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_user_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_fill_map.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_gradient_stop.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_gradient_stop_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_line.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_line_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_text.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_text_id_isSet) {
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

bool OAIShared_SolidFills_Details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
