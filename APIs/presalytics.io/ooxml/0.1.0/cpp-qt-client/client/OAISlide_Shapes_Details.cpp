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

#include "OAISlide_Shapes_Details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISlide_Shapes_Details::OAISlide_Shapes_Details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISlide_Shapes_Details::OAISlide_Shapes_Details() {
    this->initializeModel();
}

OAISlide_Shapes_Details::~OAISlide_Shapes_Details() {}

void OAISlide_Shapes_Details::initializeModel() {

    m_base_element_blob_url_isSet = false;
    m_base_element_blob_url_isValid = false;

    m_changed_base_element_blob_url_isSet = false;
    m_changed_base_element_blob_url_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_modified_isSet = false;
    m_date_modified_isValid = false;

    m_effect_isSet = false;
    m_effect_isValid = false;

    m_fill_map_isSet = false;
    m_fill_map_isValid = false;

    m_flip_horizontal_isSet = false;
    m_flip_horizontal_isValid = false;

    m_flip_vertical_isSet = false;
    m_flip_vertical_isValid = false;

    m_free_form_path_xml_isSet = false;
    m_free_form_path_xml_isValid = false;

    m_group_element_isSet = false;
    m_group_element_isValid = false;

    m_group_elements_id_isSet = false;
    m_group_elements_id_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_hidden_isSet = false;
    m_hidden_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_theme_effect_isSet = false;
    m_is_theme_effect_isValid = false;

    m_is_theme_fill_isSet = false;
    m_is_theme_fill_isValid = false;

    m_is_theme_line_isSet = false;
    m_is_theme_line_isValid = false;

    m_line_isSet = false;
    m_line_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_ooxml_id_isSet = false;
    m_ooxml_id_isValid = false;

    m_package_uri_isSet = false;
    m_package_uri_isValid = false;

    m_preset_type_id_isSet = false;
    m_preset_type_id_isValid = false;

    m_rotation_isSet = false;
    m_rotation_isValid = false;

    m_svg_blob_url_isSet = false;
    m_svg_blob_url_isValid = false;

    m_text_container_isSet = false;
    m_text_container_isValid = false;

    m_user_created_isSet = false;
    m_user_created_isValid = false;

    m_user_modified_isSet = false;
    m_user_modified_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;

    m_x_offset_isSet = false;
    m_x_offset_isValid = false;

    m_y_offset_isSet = false;
    m_y_offset_isValid = false;
}

void OAISlide_Shapes_Details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISlide_Shapes_Details::fromJsonObject(QJsonObject json) {

    m_base_element_blob_url_isValid = ::OpenAPI::fromJsonValue(m_base_element_blob_url, json[QString("baseElementBlobUrl")]);
    m_base_element_blob_url_isSet = !json[QString("baseElementBlobUrl")].isNull() && m_base_element_blob_url_isValid;

    m_changed_base_element_blob_url_isValid = ::OpenAPI::fromJsonValue(m_changed_base_element_blob_url, json[QString("changedBaseElementBlobUrl")]);
    m_changed_base_element_blob_url_isSet = !json[QString("changedBaseElementBlobUrl")].isNull() && m_changed_base_element_blob_url_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("dateCreated")]);
    m_date_created_isSet = !json[QString("dateCreated")].isNull() && m_date_created_isValid;

    m_date_modified_isValid = ::OpenAPI::fromJsonValue(m_date_modified, json[QString("dateModified")]);
    m_date_modified_isSet = !json[QString("dateModified")].isNull() && m_date_modified_isValid;

    m_effect_isValid = ::OpenAPI::fromJsonValue(m_effect, json[QString("effect")]);
    m_effect_isSet = !json[QString("effect")].isNull() && m_effect_isValid;

    m_fill_map_isValid = ::OpenAPI::fromJsonValue(m_fill_map, json[QString("fillMap")]);
    m_fill_map_isSet = !json[QString("fillMap")].isNull() && m_fill_map_isValid;

    m_flip_horizontal_isValid = ::OpenAPI::fromJsonValue(m_flip_horizontal, json[QString("flipHorizontal")]);
    m_flip_horizontal_isSet = !json[QString("flipHorizontal")].isNull() && m_flip_horizontal_isValid;

    m_flip_vertical_isValid = ::OpenAPI::fromJsonValue(m_flip_vertical, json[QString("flipVertical")]);
    m_flip_vertical_isSet = !json[QString("flipVertical")].isNull() && m_flip_vertical_isValid;

    m_free_form_path_xml_isValid = ::OpenAPI::fromJsonValue(m_free_form_path_xml, json[QString("freeFormPathXml")]);
    m_free_form_path_xml_isSet = !json[QString("freeFormPathXml")].isNull() && m_free_form_path_xml_isValid;

    m_group_element_isValid = ::OpenAPI::fromJsonValue(m_group_element, json[QString("groupElement")]);
    m_group_element_isSet = !json[QString("groupElement")].isNull() && m_group_element_isValid;

    m_group_elements_id_isValid = ::OpenAPI::fromJsonValue(m_group_elements_id, json[QString("groupElementsId")]);
    m_group_elements_id_isSet = !json[QString("groupElementsId")].isNull() && m_group_elements_id_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_hidden_isValid = ::OpenAPI::fromJsonValue(m_hidden, json[QString("hidden")]);
    m_hidden_isSet = !json[QString("hidden")].isNull() && m_hidden_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_theme_effect_isValid = ::OpenAPI::fromJsonValue(m_is_theme_effect, json[QString("isThemeEffect")]);
    m_is_theme_effect_isSet = !json[QString("isThemeEffect")].isNull() && m_is_theme_effect_isValid;

    m_is_theme_fill_isValid = ::OpenAPI::fromJsonValue(m_is_theme_fill, json[QString("isThemeFill")]);
    m_is_theme_fill_isSet = !json[QString("isThemeFill")].isNull() && m_is_theme_fill_isValid;

    m_is_theme_line_isValid = ::OpenAPI::fromJsonValue(m_is_theme_line, json[QString("isThemeLine")]);
    m_is_theme_line_isSet = !json[QString("isThemeLine")].isNull() && m_is_theme_line_isValid;

    m_line_isValid = ::OpenAPI::fromJsonValue(m_line, json[QString("line")]);
    m_line_isSet = !json[QString("line")].isNull() && m_line_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_ooxml_id_isValid = ::OpenAPI::fromJsonValue(m_ooxml_id, json[QString("ooxmlId")]);
    m_ooxml_id_isSet = !json[QString("ooxmlId")].isNull() && m_ooxml_id_isValid;

    m_package_uri_isValid = ::OpenAPI::fromJsonValue(m_package_uri, json[QString("packageUri")]);
    m_package_uri_isSet = !json[QString("packageUri")].isNull() && m_package_uri_isValid;

    m_preset_type_id_isValid = ::OpenAPI::fromJsonValue(m_preset_type_id, json[QString("presetTypeId")]);
    m_preset_type_id_isSet = !json[QString("presetTypeId")].isNull() && m_preset_type_id_isValid;

    m_rotation_isValid = ::OpenAPI::fromJsonValue(m_rotation, json[QString("rotation")]);
    m_rotation_isSet = !json[QString("rotation")].isNull() && m_rotation_isValid;

    m_svg_blob_url_isValid = ::OpenAPI::fromJsonValue(m_svg_blob_url, json[QString("svgBlobUrl")]);
    m_svg_blob_url_isSet = !json[QString("svgBlobUrl")].isNull() && m_svg_blob_url_isValid;

    m_text_container_isValid = ::OpenAPI::fromJsonValue(m_text_container, json[QString("textContainer")]);
    m_text_container_isSet = !json[QString("textContainer")].isNull() && m_text_container_isValid;

    m_user_created_isValid = ::OpenAPI::fromJsonValue(m_user_created, json[QString("userCreated")]);
    m_user_created_isSet = !json[QString("userCreated")].isNull() && m_user_created_isValid;

    m_user_modified_isValid = ::OpenAPI::fromJsonValue(m_user_modified, json[QString("userModified")]);
    m_user_modified_isSet = !json[QString("userModified")].isNull() && m_user_modified_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;

    m_x_offset_isValid = ::OpenAPI::fromJsonValue(m_x_offset, json[QString("xOffset")]);
    m_x_offset_isSet = !json[QString("xOffset")].isNull() && m_x_offset_isValid;

    m_y_offset_isValid = ::OpenAPI::fromJsonValue(m_y_offset, json[QString("yOffset")]);
    m_y_offset_isSet = !json[QString("yOffset")].isNull() && m_y_offset_isValid;
}

QString OAISlide_Shapes_Details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISlide_Shapes_Details::asJsonObject() const {
    QJsonObject obj;
    if (m_base_element_blob_url_isSet) {
        obj.insert(QString("baseElementBlobUrl"), ::OpenAPI::toJsonValue(m_base_element_blob_url));
    }
    if (m_changed_base_element_blob_url_isSet) {
        obj.insert(QString("changedBaseElementBlobUrl"), ::OpenAPI::toJsonValue(m_changed_base_element_blob_url));
    }
    if (m_date_created_isSet) {
        obj.insert(QString("dateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_date_modified_isSet) {
        obj.insert(QString("dateModified"), ::OpenAPI::toJsonValue(m_date_modified));
    }
    if (m_effect.isSet()) {
        obj.insert(QString("effect"), ::OpenAPI::toJsonValue(m_effect));
    }
    if (m_fill_map.isSet()) {
        obj.insert(QString("fillMap"), ::OpenAPI::toJsonValue(m_fill_map));
    }
    if (m_flip_horizontal_isSet) {
        obj.insert(QString("flipHorizontal"), ::OpenAPI::toJsonValue(m_flip_horizontal));
    }
    if (m_flip_vertical_isSet) {
        obj.insert(QString("flipVertical"), ::OpenAPI::toJsonValue(m_flip_vertical));
    }
    if (m_free_form_path_xml_isSet) {
        obj.insert(QString("freeFormPathXml"), ::OpenAPI::toJsonValue(m_free_form_path_xml));
    }
    if (m_group_element.isSet()) {
        obj.insert(QString("groupElement"), ::OpenAPI::toJsonValue(m_group_element));
    }
    if (m_group_elements_id_isSet) {
        obj.insert(QString("groupElementsId"), ::OpenAPI::toJsonValue(m_group_elements_id));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_hidden_isSet) {
        obj.insert(QString("hidden"), ::OpenAPI::toJsonValue(m_hidden));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_theme_effect_isSet) {
        obj.insert(QString("isThemeEffect"), ::OpenAPI::toJsonValue(m_is_theme_effect));
    }
    if (m_is_theme_fill_isSet) {
        obj.insert(QString("isThemeFill"), ::OpenAPI::toJsonValue(m_is_theme_fill));
    }
    if (m_is_theme_line_isSet) {
        obj.insert(QString("isThemeLine"), ::OpenAPI::toJsonValue(m_is_theme_line));
    }
    if (m_line.isSet()) {
        obj.insert(QString("line"), ::OpenAPI::toJsonValue(m_line));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_ooxml_id_isSet) {
        obj.insert(QString("ooxmlId"), ::OpenAPI::toJsonValue(m_ooxml_id));
    }
    if (m_package_uri_isSet) {
        obj.insert(QString("packageUri"), ::OpenAPI::toJsonValue(m_package_uri));
    }
    if (m_preset_type_id_isSet) {
        obj.insert(QString("presetTypeId"), ::OpenAPI::toJsonValue(m_preset_type_id));
    }
    if (m_rotation_isSet) {
        obj.insert(QString("rotation"), ::OpenAPI::toJsonValue(m_rotation));
    }
    if (m_svg_blob_url_isSet) {
        obj.insert(QString("svgBlobUrl"), ::OpenAPI::toJsonValue(m_svg_blob_url));
    }
    if (m_text_container.isSet()) {
        obj.insert(QString("textContainer"), ::OpenAPI::toJsonValue(m_text_container));
    }
    if (m_user_created_isSet) {
        obj.insert(QString("userCreated"), ::OpenAPI::toJsonValue(m_user_created));
    }
    if (m_user_modified_isSet) {
        obj.insert(QString("userModified"), ::OpenAPI::toJsonValue(m_user_modified));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    if (m_x_offset_isSet) {
        obj.insert(QString("xOffset"), ::OpenAPI::toJsonValue(m_x_offset));
    }
    if (m_y_offset_isSet) {
        obj.insert(QString("yOffset"), ::OpenAPI::toJsonValue(m_y_offset));
    }
    return obj;
}

QString OAISlide_Shapes_Details::getBaseElementBlobUrl() const {
    return m_base_element_blob_url;
}
void OAISlide_Shapes_Details::setBaseElementBlobUrl(const QString &base_element_blob_url) {
    m_base_element_blob_url = base_element_blob_url;
    m_base_element_blob_url_isSet = true;
}

bool OAISlide_Shapes_Details::is_base_element_blob_url_Set() const{
    return m_base_element_blob_url_isSet;
}

bool OAISlide_Shapes_Details::is_base_element_blob_url_Valid() const{
    return m_base_element_blob_url_isValid;
}

QString OAISlide_Shapes_Details::getChangedBaseElementBlobUrl() const {
    return m_changed_base_element_blob_url;
}
void OAISlide_Shapes_Details::setChangedBaseElementBlobUrl(const QString &changed_base_element_blob_url) {
    m_changed_base_element_blob_url = changed_base_element_blob_url;
    m_changed_base_element_blob_url_isSet = true;
}

bool OAISlide_Shapes_Details::is_changed_base_element_blob_url_Set() const{
    return m_changed_base_element_blob_url_isSet;
}

bool OAISlide_Shapes_Details::is_changed_base_element_blob_url_Valid() const{
    return m_changed_base_element_blob_url_isValid;
}

QDateTime OAISlide_Shapes_Details::getDateCreated() const {
    return m_date_created;
}
void OAISlide_Shapes_Details::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAISlide_Shapes_Details::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAISlide_Shapes_Details::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAISlide_Shapes_Details::getDateModified() const {
    return m_date_modified;
}
void OAISlide_Shapes_Details::setDateModified(const QDateTime &date_modified) {
    m_date_modified = date_modified;
    m_date_modified_isSet = true;
}

bool OAISlide_Shapes_Details::is_date_modified_Set() const{
    return m_date_modified_isSet;
}

bool OAISlide_Shapes_Details::is_date_modified_Valid() const{
    return m_date_modified_isValid;
}

OAIShared_Effects_Details OAISlide_Shapes_Details::getEffect() const {
    return m_effect;
}
void OAISlide_Shapes_Details::setEffect(const OAIShared_Effects_Details &effect) {
    m_effect = effect;
    m_effect_isSet = true;
}

bool OAISlide_Shapes_Details::is_effect_Set() const{
    return m_effect_isSet;
}

bool OAISlide_Shapes_Details::is_effect_Valid() const{
    return m_effect_isValid;
}

OAIShared_FillMap_Details OAISlide_Shapes_Details::getFillMap() const {
    return m_fill_map;
}
void OAISlide_Shapes_Details::setFillMap(const OAIShared_FillMap_Details &fill_map) {
    m_fill_map = fill_map;
    m_fill_map_isSet = true;
}

bool OAISlide_Shapes_Details::is_fill_map_Set() const{
    return m_fill_map_isSet;
}

bool OAISlide_Shapes_Details::is_fill_map_Valid() const{
    return m_fill_map_isValid;
}

bool OAISlide_Shapes_Details::isFlipHorizontal() const {
    return m_flip_horizontal;
}
void OAISlide_Shapes_Details::setFlipHorizontal(const bool &flip_horizontal) {
    m_flip_horizontal = flip_horizontal;
    m_flip_horizontal_isSet = true;
}

bool OAISlide_Shapes_Details::is_flip_horizontal_Set() const{
    return m_flip_horizontal_isSet;
}

bool OAISlide_Shapes_Details::is_flip_horizontal_Valid() const{
    return m_flip_horizontal_isValid;
}

bool OAISlide_Shapes_Details::isFlipVertical() const {
    return m_flip_vertical;
}
void OAISlide_Shapes_Details::setFlipVertical(const bool &flip_vertical) {
    m_flip_vertical = flip_vertical;
    m_flip_vertical_isSet = true;
}

bool OAISlide_Shapes_Details::is_flip_vertical_Set() const{
    return m_flip_vertical_isSet;
}

bool OAISlide_Shapes_Details::is_flip_vertical_Valid() const{
    return m_flip_vertical_isValid;
}

QString OAISlide_Shapes_Details::getFreeFormPathXml() const {
    return m_free_form_path_xml;
}
void OAISlide_Shapes_Details::setFreeFormPathXml(const QString &free_form_path_xml) {
    m_free_form_path_xml = free_form_path_xml;
    m_free_form_path_xml_isSet = true;
}

bool OAISlide_Shapes_Details::is_free_form_path_xml_Set() const{
    return m_free_form_path_xml_isSet;
}

bool OAISlide_Shapes_Details::is_free_form_path_xml_Valid() const{
    return m_free_form_path_xml_isValid;
}

OAISlide_GroupElements_Details OAISlide_Shapes_Details::getGroupElement() const {
    return m_group_element;
}
void OAISlide_Shapes_Details::setGroupElement(const OAISlide_GroupElements_Details &group_element) {
    m_group_element = group_element;
    m_group_element_isSet = true;
}

bool OAISlide_Shapes_Details::is_group_element_Set() const{
    return m_group_element_isSet;
}

bool OAISlide_Shapes_Details::is_group_element_Valid() const{
    return m_group_element_isValid;
}

QString OAISlide_Shapes_Details::getGroupElementsId() const {
    return m_group_elements_id;
}
void OAISlide_Shapes_Details::setGroupElementsId(const QString &group_elements_id) {
    m_group_elements_id = group_elements_id;
    m_group_elements_id_isSet = true;
}

bool OAISlide_Shapes_Details::is_group_elements_id_Set() const{
    return m_group_elements_id_isSet;
}

bool OAISlide_Shapes_Details::is_group_elements_id_Valid() const{
    return m_group_elements_id_isValid;
}

qint32 OAISlide_Shapes_Details::getHeight() const {
    return m_height;
}
void OAISlide_Shapes_Details::setHeight(const qint32 &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAISlide_Shapes_Details::is_height_Set() const{
    return m_height_isSet;
}

bool OAISlide_Shapes_Details::is_height_Valid() const{
    return m_height_isValid;
}

bool OAISlide_Shapes_Details::isHidden() const {
    return m_hidden;
}
void OAISlide_Shapes_Details::setHidden(const bool &hidden) {
    m_hidden = hidden;
    m_hidden_isSet = true;
}

bool OAISlide_Shapes_Details::is_hidden_Set() const{
    return m_hidden_isSet;
}

bool OAISlide_Shapes_Details::is_hidden_Valid() const{
    return m_hidden_isValid;
}

QString OAISlide_Shapes_Details::getId() const {
    return m_id;
}
void OAISlide_Shapes_Details::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISlide_Shapes_Details::is_id_Set() const{
    return m_id_isSet;
}

bool OAISlide_Shapes_Details::is_id_Valid() const{
    return m_id_isValid;
}

bool OAISlide_Shapes_Details::isIsThemeEffect() const {
    return m_is_theme_effect;
}
void OAISlide_Shapes_Details::setIsThemeEffect(const bool &is_theme_effect) {
    m_is_theme_effect = is_theme_effect;
    m_is_theme_effect_isSet = true;
}

bool OAISlide_Shapes_Details::is_is_theme_effect_Set() const{
    return m_is_theme_effect_isSet;
}

bool OAISlide_Shapes_Details::is_is_theme_effect_Valid() const{
    return m_is_theme_effect_isValid;
}

bool OAISlide_Shapes_Details::isIsThemeFill() const {
    return m_is_theme_fill;
}
void OAISlide_Shapes_Details::setIsThemeFill(const bool &is_theme_fill) {
    m_is_theme_fill = is_theme_fill;
    m_is_theme_fill_isSet = true;
}

bool OAISlide_Shapes_Details::is_is_theme_fill_Set() const{
    return m_is_theme_fill_isSet;
}

bool OAISlide_Shapes_Details::is_is_theme_fill_Valid() const{
    return m_is_theme_fill_isValid;
}

bool OAISlide_Shapes_Details::isIsThemeLine() const {
    return m_is_theme_line;
}
void OAISlide_Shapes_Details::setIsThemeLine(const bool &is_theme_line) {
    m_is_theme_line = is_theme_line;
    m_is_theme_line_isSet = true;
}

bool OAISlide_Shapes_Details::is_is_theme_line_Set() const{
    return m_is_theme_line_isSet;
}

bool OAISlide_Shapes_Details::is_is_theme_line_Valid() const{
    return m_is_theme_line_isValid;
}

OAIShared_Lines_Details OAISlide_Shapes_Details::getLine() const {
    return m_line;
}
void OAISlide_Shapes_Details::setLine(const OAIShared_Lines_Details &line) {
    m_line = line;
    m_line_isSet = true;
}

bool OAISlide_Shapes_Details::is_line_Set() const{
    return m_line_isSet;
}

bool OAISlide_Shapes_Details::is_line_Valid() const{
    return m_line_isValid;
}

QString OAISlide_Shapes_Details::getName() const {
    return m_name;
}
void OAISlide_Shapes_Details::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISlide_Shapes_Details::is_name_Set() const{
    return m_name_isSet;
}

bool OAISlide_Shapes_Details::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAISlide_Shapes_Details::getOoxmlId() const {
    return m_ooxml_id;
}
void OAISlide_Shapes_Details::setOoxmlId(const qint32 &ooxml_id) {
    m_ooxml_id = ooxml_id;
    m_ooxml_id_isSet = true;
}

bool OAISlide_Shapes_Details::is_ooxml_id_Set() const{
    return m_ooxml_id_isSet;
}

bool OAISlide_Shapes_Details::is_ooxml_id_Valid() const{
    return m_ooxml_id_isValid;
}

QString OAISlide_Shapes_Details::getPackageUri() const {
    return m_package_uri;
}
void OAISlide_Shapes_Details::setPackageUri(const QString &package_uri) {
    m_package_uri = package_uri;
    m_package_uri_isSet = true;
}

bool OAISlide_Shapes_Details::is_package_uri_Set() const{
    return m_package_uri_isSet;
}

bool OAISlide_Shapes_Details::is_package_uri_Valid() const{
    return m_package_uri_isValid;
}

QString OAISlide_Shapes_Details::getPresetTypeId() const {
    return m_preset_type_id;
}
void OAISlide_Shapes_Details::setPresetTypeId(const QString &preset_type_id) {
    m_preset_type_id = preset_type_id;
    m_preset_type_id_isSet = true;
}

bool OAISlide_Shapes_Details::is_preset_type_id_Set() const{
    return m_preset_type_id_isSet;
}

bool OAISlide_Shapes_Details::is_preset_type_id_Valid() const{
    return m_preset_type_id_isValid;
}

qint32 OAISlide_Shapes_Details::getRotation() const {
    return m_rotation;
}
void OAISlide_Shapes_Details::setRotation(const qint32 &rotation) {
    m_rotation = rotation;
    m_rotation_isSet = true;
}

bool OAISlide_Shapes_Details::is_rotation_Set() const{
    return m_rotation_isSet;
}

bool OAISlide_Shapes_Details::is_rotation_Valid() const{
    return m_rotation_isValid;
}

QString OAISlide_Shapes_Details::getSvgBlobUrl() const {
    return m_svg_blob_url;
}
void OAISlide_Shapes_Details::setSvgBlobUrl(const QString &svg_blob_url) {
    m_svg_blob_url = svg_blob_url;
    m_svg_blob_url_isSet = true;
}

bool OAISlide_Shapes_Details::is_svg_blob_url_Set() const{
    return m_svg_blob_url_isSet;
}

bool OAISlide_Shapes_Details::is_svg_blob_url_Valid() const{
    return m_svg_blob_url_isValid;
}

OAIShared_TextContainer_Details OAISlide_Shapes_Details::getTextContainer() const {
    return m_text_container;
}
void OAISlide_Shapes_Details::setTextContainer(const OAIShared_TextContainer_Details &text_container) {
    m_text_container = text_container;
    m_text_container_isSet = true;
}

bool OAISlide_Shapes_Details::is_text_container_Set() const{
    return m_text_container_isSet;
}

bool OAISlide_Shapes_Details::is_text_container_Valid() const{
    return m_text_container_isValid;
}

QString OAISlide_Shapes_Details::getUserCreated() const {
    return m_user_created;
}
void OAISlide_Shapes_Details::setUserCreated(const QString &user_created) {
    m_user_created = user_created;
    m_user_created_isSet = true;
}

bool OAISlide_Shapes_Details::is_user_created_Set() const{
    return m_user_created_isSet;
}

bool OAISlide_Shapes_Details::is_user_created_Valid() const{
    return m_user_created_isValid;
}

QString OAISlide_Shapes_Details::getUserModified() const {
    return m_user_modified;
}
void OAISlide_Shapes_Details::setUserModified(const QString &user_modified) {
    m_user_modified = user_modified;
    m_user_modified_isSet = true;
}

bool OAISlide_Shapes_Details::is_user_modified_Set() const{
    return m_user_modified_isSet;
}

bool OAISlide_Shapes_Details::is_user_modified_Valid() const{
    return m_user_modified_isValid;
}

qint32 OAISlide_Shapes_Details::getWidth() const {
    return m_width;
}
void OAISlide_Shapes_Details::setWidth(const qint32 &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAISlide_Shapes_Details::is_width_Set() const{
    return m_width_isSet;
}

bool OAISlide_Shapes_Details::is_width_Valid() const{
    return m_width_isValid;
}

qint32 OAISlide_Shapes_Details::getXOffset() const {
    return m_x_offset;
}
void OAISlide_Shapes_Details::setXOffset(const qint32 &x_offset) {
    m_x_offset = x_offset;
    m_x_offset_isSet = true;
}

bool OAISlide_Shapes_Details::is_x_offset_Set() const{
    return m_x_offset_isSet;
}

bool OAISlide_Shapes_Details::is_x_offset_Valid() const{
    return m_x_offset_isValid;
}

qint32 OAISlide_Shapes_Details::getYOffset() const {
    return m_y_offset;
}
void OAISlide_Shapes_Details::setYOffset(const qint32 &y_offset) {
    m_y_offset = y_offset;
    m_y_offset_isSet = true;
}

bool OAISlide_Shapes_Details::is_y_offset_Set() const{
    return m_y_offset_isSet;
}

bool OAISlide_Shapes_Details::is_y_offset_Valid() const{
    return m_y_offset_isValid;
}

bool OAISlide_Shapes_Details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base_element_blob_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_changed_base_element_blob_url_isSet) {
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

        if (m_effect.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_fill_map.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_flip_horizontal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_flip_vertical_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_free_form_path_xml_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_element.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_elements_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hidden_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_theme_effect_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_theme_fill_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_theme_line_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ooxml_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_package_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preset_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rotation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_svg_blob_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_container.isSet()) {
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

        if (m_width_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_x_offset_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_y_offset_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISlide_Shapes_Details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
