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

#include "OAITable_Tables_Details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITable_Tables_Details::OAITable_Tables_Details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITable_Tables_Details::OAITable_Tables_Details() {
    this->initializeModel();
}

OAITable_Tables_Details::~OAITable_Tables_Details() {}

void OAITable_Tables_Details::initializeModel() {

    m_base_element_blob_url_isSet = false;
    m_base_element_blob_url_isValid = false;

    m_cells_isSet = false;
    m_cells_isValid = false;

    m_changed_base_element_blob_url_isSet = false;
    m_changed_base_element_blob_url_isValid = false;

    m_columns_isSet = false;
    m_columns_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_modified_isSet = false;
    m_date_modified_isValid = false;

    m_has_style_part_isSet = false;
    m_has_style_part_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_package_uri_isSet = false;
    m_package_uri_isValid = false;

    m_parent_graphic_isSet = false;
    m_parent_graphic_isValid = false;

    m_parent_graphic_id_isSet = false;
    m_parent_graphic_id_isValid = false;

    m_rows_isSet = false;
    m_rows_isValid = false;

    m_style_part_outer_xml_isSet = false;
    m_style_part_outer_xml_isValid = false;

    m_svg_blob_url_isSet = false;
    m_svg_blob_url_isValid = false;

    m_user_created_isSet = false;
    m_user_created_isValid = false;

    m_user_modified_isSet = false;
    m_user_modified_isValid = false;
}

void OAITable_Tables_Details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITable_Tables_Details::fromJsonObject(QJsonObject json) {

    m_base_element_blob_url_isValid = ::OpenAPI::fromJsonValue(m_base_element_blob_url, json[QString("baseElementBlobUrl")]);
    m_base_element_blob_url_isSet = !json[QString("baseElementBlobUrl")].isNull() && m_base_element_blob_url_isValid;

    m_cells_isValid = ::OpenAPI::fromJsonValue(m_cells, json[QString("cells")]);
    m_cells_isSet = !json[QString("cells")].isNull() && m_cells_isValid;

    m_changed_base_element_blob_url_isValid = ::OpenAPI::fromJsonValue(m_changed_base_element_blob_url, json[QString("changedBaseElementBlobUrl")]);
    m_changed_base_element_blob_url_isSet = !json[QString("changedBaseElementBlobUrl")].isNull() && m_changed_base_element_blob_url_isValid;

    m_columns_isValid = ::OpenAPI::fromJsonValue(m_columns, json[QString("columns")]);
    m_columns_isSet = !json[QString("columns")].isNull() && m_columns_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("dateCreated")]);
    m_date_created_isSet = !json[QString("dateCreated")].isNull() && m_date_created_isValid;

    m_date_modified_isValid = ::OpenAPI::fromJsonValue(m_date_modified, json[QString("dateModified")]);
    m_date_modified_isSet = !json[QString("dateModified")].isNull() && m_date_modified_isValid;

    m_has_style_part_isValid = ::OpenAPI::fromJsonValue(m_has_style_part, json[QString("hasStylePart")]);
    m_has_style_part_isSet = !json[QString("hasStylePart")].isNull() && m_has_style_part_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_package_uri_isValid = ::OpenAPI::fromJsonValue(m_package_uri, json[QString("packageUri")]);
    m_package_uri_isSet = !json[QString("packageUri")].isNull() && m_package_uri_isValid;

    m_parent_graphic_isValid = ::OpenAPI::fromJsonValue(m_parent_graphic, json[QString("parentGraphic")]);
    m_parent_graphic_isSet = !json[QString("parentGraphic")].isNull() && m_parent_graphic_isValid;

    m_parent_graphic_id_isValid = ::OpenAPI::fromJsonValue(m_parent_graphic_id, json[QString("parentGraphicId")]);
    m_parent_graphic_id_isSet = !json[QString("parentGraphicId")].isNull() && m_parent_graphic_id_isValid;

    m_rows_isValid = ::OpenAPI::fromJsonValue(m_rows, json[QString("rows")]);
    m_rows_isSet = !json[QString("rows")].isNull() && m_rows_isValid;

    m_style_part_outer_xml_isValid = ::OpenAPI::fromJsonValue(m_style_part_outer_xml, json[QString("stylePartOuterXml")]);
    m_style_part_outer_xml_isSet = !json[QString("stylePartOuterXml")].isNull() && m_style_part_outer_xml_isValid;

    m_svg_blob_url_isValid = ::OpenAPI::fromJsonValue(m_svg_blob_url, json[QString("svgBlobUrl")]);
    m_svg_blob_url_isSet = !json[QString("svgBlobUrl")].isNull() && m_svg_blob_url_isValid;

    m_user_created_isValid = ::OpenAPI::fromJsonValue(m_user_created, json[QString("userCreated")]);
    m_user_created_isSet = !json[QString("userCreated")].isNull() && m_user_created_isValid;

    m_user_modified_isValid = ::OpenAPI::fromJsonValue(m_user_modified, json[QString("userModified")]);
    m_user_modified_isSet = !json[QString("userModified")].isNull() && m_user_modified_isValid;
}

QString OAITable_Tables_Details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITable_Tables_Details::asJsonObject() const {
    QJsonObject obj;
    if (m_base_element_blob_url_isSet) {
        obj.insert(QString("baseElementBlobUrl"), ::OpenAPI::toJsonValue(m_base_element_blob_url));
    }
    if (m_cells.size() > 0) {
        obj.insert(QString("cells"), ::OpenAPI::toJsonValue(m_cells));
    }
    if (m_changed_base_element_blob_url_isSet) {
        obj.insert(QString("changedBaseElementBlobUrl"), ::OpenAPI::toJsonValue(m_changed_base_element_blob_url));
    }
    if (m_columns.size() > 0) {
        obj.insert(QString("columns"), ::OpenAPI::toJsonValue(m_columns));
    }
    if (m_date_created_isSet) {
        obj.insert(QString("dateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_date_modified_isSet) {
        obj.insert(QString("dateModified"), ::OpenAPI::toJsonValue(m_date_modified));
    }
    if (m_has_style_part_isSet) {
        obj.insert(QString("hasStylePart"), ::OpenAPI::toJsonValue(m_has_style_part));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_package_uri_isSet) {
        obj.insert(QString("packageUri"), ::OpenAPI::toJsonValue(m_package_uri));
    }
    if (m_parent_graphic.isSet()) {
        obj.insert(QString("parentGraphic"), ::OpenAPI::toJsonValue(m_parent_graphic));
    }
    if (m_parent_graphic_id_isSet) {
        obj.insert(QString("parentGraphicId"), ::OpenAPI::toJsonValue(m_parent_graphic_id));
    }
    if (m_rows.size() > 0) {
        obj.insert(QString("rows"), ::OpenAPI::toJsonValue(m_rows));
    }
    if (m_style_part_outer_xml_isSet) {
        obj.insert(QString("stylePartOuterXml"), ::OpenAPI::toJsonValue(m_style_part_outer_xml));
    }
    if (m_svg_blob_url_isSet) {
        obj.insert(QString("svgBlobUrl"), ::OpenAPI::toJsonValue(m_svg_blob_url));
    }
    if (m_user_created_isSet) {
        obj.insert(QString("userCreated"), ::OpenAPI::toJsonValue(m_user_created));
    }
    if (m_user_modified_isSet) {
        obj.insert(QString("userModified"), ::OpenAPI::toJsonValue(m_user_modified));
    }
    return obj;
}

QString OAITable_Tables_Details::getBaseElementBlobUrl() const {
    return m_base_element_blob_url;
}
void OAITable_Tables_Details::setBaseElementBlobUrl(const QString &base_element_blob_url) {
    m_base_element_blob_url = base_element_blob_url;
    m_base_element_blob_url_isSet = true;
}

bool OAITable_Tables_Details::is_base_element_blob_url_Set() const{
    return m_base_element_blob_url_isSet;
}

bool OAITable_Tables_Details::is_base_element_blob_url_Valid() const{
    return m_base_element_blob_url_isValid;
}

QList<OAITable_Cells_Details> OAITable_Tables_Details::getCells() const {
    return m_cells;
}
void OAITable_Tables_Details::setCells(const QList<OAITable_Cells_Details> &cells) {
    m_cells = cells;
    m_cells_isSet = true;
}

bool OAITable_Tables_Details::is_cells_Set() const{
    return m_cells_isSet;
}

bool OAITable_Tables_Details::is_cells_Valid() const{
    return m_cells_isValid;
}

QString OAITable_Tables_Details::getChangedBaseElementBlobUrl() const {
    return m_changed_base_element_blob_url;
}
void OAITable_Tables_Details::setChangedBaseElementBlobUrl(const QString &changed_base_element_blob_url) {
    m_changed_base_element_blob_url = changed_base_element_blob_url;
    m_changed_base_element_blob_url_isSet = true;
}

bool OAITable_Tables_Details::is_changed_base_element_blob_url_Set() const{
    return m_changed_base_element_blob_url_isSet;
}

bool OAITable_Tables_Details::is_changed_base_element_blob_url_Valid() const{
    return m_changed_base_element_blob_url_isValid;
}

QList<OAITable_Columns_Details> OAITable_Tables_Details::getColumns() const {
    return m_columns;
}
void OAITable_Tables_Details::setColumns(const QList<OAITable_Columns_Details> &columns) {
    m_columns = columns;
    m_columns_isSet = true;
}

bool OAITable_Tables_Details::is_columns_Set() const{
    return m_columns_isSet;
}

bool OAITable_Tables_Details::is_columns_Valid() const{
    return m_columns_isValid;
}

QDateTime OAITable_Tables_Details::getDateCreated() const {
    return m_date_created;
}
void OAITable_Tables_Details::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAITable_Tables_Details::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAITable_Tables_Details::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAITable_Tables_Details::getDateModified() const {
    return m_date_modified;
}
void OAITable_Tables_Details::setDateModified(const QDateTime &date_modified) {
    m_date_modified = date_modified;
    m_date_modified_isSet = true;
}

bool OAITable_Tables_Details::is_date_modified_Set() const{
    return m_date_modified_isSet;
}

bool OAITable_Tables_Details::is_date_modified_Valid() const{
    return m_date_modified_isValid;
}

bool OAITable_Tables_Details::isHasStylePart() const {
    return m_has_style_part;
}
void OAITable_Tables_Details::setHasStylePart(const bool &has_style_part) {
    m_has_style_part = has_style_part;
    m_has_style_part_isSet = true;
}

bool OAITable_Tables_Details::is_has_style_part_Set() const{
    return m_has_style_part_isSet;
}

bool OAITable_Tables_Details::is_has_style_part_Valid() const{
    return m_has_style_part_isValid;
}

QString OAITable_Tables_Details::getId() const {
    return m_id;
}
void OAITable_Tables_Details::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITable_Tables_Details::is_id_Set() const{
    return m_id_isSet;
}

bool OAITable_Tables_Details::is_id_Valid() const{
    return m_id_isValid;
}

QString OAITable_Tables_Details::getName() const {
    return m_name;
}
void OAITable_Tables_Details::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITable_Tables_Details::is_name_Set() const{
    return m_name_isSet;
}

bool OAITable_Tables_Details::is_name_Valid() const{
    return m_name_isValid;
}

QString OAITable_Tables_Details::getPackageUri() const {
    return m_package_uri;
}
void OAITable_Tables_Details::setPackageUri(const QString &package_uri) {
    m_package_uri = package_uri;
    m_package_uri_isSet = true;
}

bool OAITable_Tables_Details::is_package_uri_Set() const{
    return m_package_uri_isSet;
}

bool OAITable_Tables_Details::is_package_uri_Valid() const{
    return m_package_uri_isValid;
}

OAISlide_Graphics_Details OAITable_Tables_Details::getParentGraphic() const {
    return m_parent_graphic;
}
void OAITable_Tables_Details::setParentGraphic(const OAISlide_Graphics_Details &parent_graphic) {
    m_parent_graphic = parent_graphic;
    m_parent_graphic_isSet = true;
}

bool OAITable_Tables_Details::is_parent_graphic_Set() const{
    return m_parent_graphic_isSet;
}

bool OAITable_Tables_Details::is_parent_graphic_Valid() const{
    return m_parent_graphic_isValid;
}

QString OAITable_Tables_Details::getParentGraphicId() const {
    return m_parent_graphic_id;
}
void OAITable_Tables_Details::setParentGraphicId(const QString &parent_graphic_id) {
    m_parent_graphic_id = parent_graphic_id;
    m_parent_graphic_id_isSet = true;
}

bool OAITable_Tables_Details::is_parent_graphic_id_Set() const{
    return m_parent_graphic_id_isSet;
}

bool OAITable_Tables_Details::is_parent_graphic_id_Valid() const{
    return m_parent_graphic_id_isValid;
}

QList<OAITable_Rows_Details> OAITable_Tables_Details::getRows() const {
    return m_rows;
}
void OAITable_Tables_Details::setRows(const QList<OAITable_Rows_Details> &rows) {
    m_rows = rows;
    m_rows_isSet = true;
}

bool OAITable_Tables_Details::is_rows_Set() const{
    return m_rows_isSet;
}

bool OAITable_Tables_Details::is_rows_Valid() const{
    return m_rows_isValid;
}

QString OAITable_Tables_Details::getStylePartOuterXml() const {
    return m_style_part_outer_xml;
}
void OAITable_Tables_Details::setStylePartOuterXml(const QString &style_part_outer_xml) {
    m_style_part_outer_xml = style_part_outer_xml;
    m_style_part_outer_xml_isSet = true;
}

bool OAITable_Tables_Details::is_style_part_outer_xml_Set() const{
    return m_style_part_outer_xml_isSet;
}

bool OAITable_Tables_Details::is_style_part_outer_xml_Valid() const{
    return m_style_part_outer_xml_isValid;
}

QString OAITable_Tables_Details::getSvgBlobUrl() const {
    return m_svg_blob_url;
}
void OAITable_Tables_Details::setSvgBlobUrl(const QString &svg_blob_url) {
    m_svg_blob_url = svg_blob_url;
    m_svg_blob_url_isSet = true;
}

bool OAITable_Tables_Details::is_svg_blob_url_Set() const{
    return m_svg_blob_url_isSet;
}

bool OAITable_Tables_Details::is_svg_blob_url_Valid() const{
    return m_svg_blob_url_isValid;
}

QString OAITable_Tables_Details::getUserCreated() const {
    return m_user_created;
}
void OAITable_Tables_Details::setUserCreated(const QString &user_created) {
    m_user_created = user_created;
    m_user_created_isSet = true;
}

bool OAITable_Tables_Details::is_user_created_Set() const{
    return m_user_created_isSet;
}

bool OAITable_Tables_Details::is_user_created_Valid() const{
    return m_user_created_isValid;
}

QString OAITable_Tables_Details::getUserModified() const {
    return m_user_modified;
}
void OAITable_Tables_Details::setUserModified(const QString &user_modified) {
    m_user_modified = user_modified;
    m_user_modified_isSet = true;
}

bool OAITable_Tables_Details::is_user_modified_Set() const{
    return m_user_modified_isSet;
}

bool OAITable_Tables_Details::is_user_modified_Valid() const{
    return m_user_modified_isValid;
}

bool OAITable_Tables_Details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base_element_blob_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cells.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_changed_base_element_blob_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_columns.size() > 0) {
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

        if (m_has_style_part_isSet) {
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

        if (m_package_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_graphic.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_graphic_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rows.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_style_part_outer_xml_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_svg_blob_url_isSet) {
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

bool OAITable_Tables_Details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
