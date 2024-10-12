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

#include "OAISlide_Slides_Details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISlide_Slides_Details::OAISlide_Slides_Details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISlide_Slides_Details::OAISlide_Slides_Details() {
    this->initializeModel();
}

OAISlide_Slides_Details::~OAISlide_Slides_Details() {}

void OAISlide_Slides_Details::initializeModel() {

    m_base_element_blob_url_isSet = false;
    m_base_element_blob_url_isValid = false;

    m_changed_base_element_blob_url_isSet = false;
    m_changed_base_element_blob_url_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_modified_isSet = false;
    m_date_modified_isValid = false;

    m_document_isSet = false;
    m_document_isValid = false;

    m_document_id_isSet = false;
    m_document_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_ooxml_id_isSet = false;
    m_ooxml_id_isValid = false;

    m_package_uri_isSet = false;
    m_package_uri_isValid = false;

    m_shape_tree_isSet = false;
    m_shape_tree_isValid = false;

    m_slide_document_url_isSet = false;
    m_slide_document_url_isValid = false;

    m_slide_master_isSet = false;
    m_slide_master_isValid = false;

    m_svg_blob_url_isSet = false;
    m_svg_blob_url_isValid = false;

    m_theme_isSet = false;
    m_theme_isValid = false;

    m_user_created_isSet = false;
    m_user_created_isValid = false;

    m_user_modified_isSet = false;
    m_user_modified_isValid = false;
}

void OAISlide_Slides_Details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISlide_Slides_Details::fromJsonObject(QJsonObject json) {

    m_base_element_blob_url_isValid = ::OpenAPI::fromJsonValue(m_base_element_blob_url, json[QString("baseElementBlobUrl")]);
    m_base_element_blob_url_isSet = !json[QString("baseElementBlobUrl")].isNull() && m_base_element_blob_url_isValid;

    m_changed_base_element_blob_url_isValid = ::OpenAPI::fromJsonValue(m_changed_base_element_blob_url, json[QString("changedBaseElementBlobUrl")]);
    m_changed_base_element_blob_url_isSet = !json[QString("changedBaseElementBlobUrl")].isNull() && m_changed_base_element_blob_url_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("dateCreated")]);
    m_date_created_isSet = !json[QString("dateCreated")].isNull() && m_date_created_isValid;

    m_date_modified_isValid = ::OpenAPI::fromJsonValue(m_date_modified, json[QString("dateModified")]);
    m_date_modified_isSet = !json[QString("dateModified")].isNull() && m_date_modified_isValid;

    m_document_isValid = ::OpenAPI::fromJsonValue(m_document, json[QString("document")]);
    m_document_isSet = !json[QString("document")].isNull() && m_document_isValid;

    m_document_id_isValid = ::OpenAPI::fromJsonValue(m_document_id, json[QString("documentId")]);
    m_document_id_isSet = !json[QString("documentId")].isNull() && m_document_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;

    m_ooxml_id_isValid = ::OpenAPI::fromJsonValue(m_ooxml_id, json[QString("ooxmlId")]);
    m_ooxml_id_isSet = !json[QString("ooxmlId")].isNull() && m_ooxml_id_isValid;

    m_package_uri_isValid = ::OpenAPI::fromJsonValue(m_package_uri, json[QString("packageUri")]);
    m_package_uri_isSet = !json[QString("packageUri")].isNull() && m_package_uri_isValid;

    m_shape_tree_isValid = ::OpenAPI::fromJsonValue(m_shape_tree, json[QString("shapeTree")]);
    m_shape_tree_isSet = !json[QString("shapeTree")].isNull() && m_shape_tree_isValid;

    m_slide_document_url_isValid = ::OpenAPI::fromJsonValue(m_slide_document_url, json[QString("slideDocumentUrl")]);
    m_slide_document_url_isSet = !json[QString("slideDocumentUrl")].isNull() && m_slide_document_url_isValid;

    m_slide_master_isValid = ::OpenAPI::fromJsonValue(m_slide_master, json[QString("slideMaster")]);
    m_slide_master_isSet = !json[QString("slideMaster")].isNull() && m_slide_master_isValid;

    m_svg_blob_url_isValid = ::OpenAPI::fromJsonValue(m_svg_blob_url, json[QString("svgBlobUrl")]);
    m_svg_blob_url_isSet = !json[QString("svgBlobUrl")].isNull() && m_svg_blob_url_isValid;

    m_theme_isValid = ::OpenAPI::fromJsonValue(m_theme, json[QString("theme")]);
    m_theme_isSet = !json[QString("theme")].isNull() && m_theme_isValid;

    m_user_created_isValid = ::OpenAPI::fromJsonValue(m_user_created, json[QString("userCreated")]);
    m_user_created_isSet = !json[QString("userCreated")].isNull() && m_user_created_isValid;

    m_user_modified_isValid = ::OpenAPI::fromJsonValue(m_user_modified, json[QString("userModified")]);
    m_user_modified_isSet = !json[QString("userModified")].isNull() && m_user_modified_isValid;
}

QString OAISlide_Slides_Details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISlide_Slides_Details::asJsonObject() const {
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
    if (m_document.isSet()) {
        obj.insert(QString("document"), ::OpenAPI::toJsonValue(m_document));
    }
    if (m_document_id_isSet) {
        obj.insert(QString("documentId"), ::OpenAPI::toJsonValue(m_document_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_ooxml_id_isSet) {
        obj.insert(QString("ooxmlId"), ::OpenAPI::toJsonValue(m_ooxml_id));
    }
    if (m_package_uri_isSet) {
        obj.insert(QString("packageUri"), ::OpenAPI::toJsonValue(m_package_uri));
    }
    if (m_shape_tree.isSet()) {
        obj.insert(QString("shapeTree"), ::OpenAPI::toJsonValue(m_shape_tree));
    }
    if (m_slide_document_url_isSet) {
        obj.insert(QString("slideDocumentUrl"), ::OpenAPI::toJsonValue(m_slide_document_url));
    }
    if (m_slide_master.isSet()) {
        obj.insert(QString("slideMaster"), ::OpenAPI::toJsonValue(m_slide_master));
    }
    if (m_svg_blob_url_isSet) {
        obj.insert(QString("svgBlobUrl"), ::OpenAPI::toJsonValue(m_svg_blob_url));
    }
    if (m_theme.isSet()) {
        obj.insert(QString("theme"), ::OpenAPI::toJsonValue(m_theme));
    }
    if (m_user_created_isSet) {
        obj.insert(QString("userCreated"), ::OpenAPI::toJsonValue(m_user_created));
    }
    if (m_user_modified_isSet) {
        obj.insert(QString("userModified"), ::OpenAPI::toJsonValue(m_user_modified));
    }
    return obj;
}

QString OAISlide_Slides_Details::getBaseElementBlobUrl() const {
    return m_base_element_blob_url;
}
void OAISlide_Slides_Details::setBaseElementBlobUrl(const QString &base_element_blob_url) {
    m_base_element_blob_url = base_element_blob_url;
    m_base_element_blob_url_isSet = true;
}

bool OAISlide_Slides_Details::is_base_element_blob_url_Set() const{
    return m_base_element_blob_url_isSet;
}

bool OAISlide_Slides_Details::is_base_element_blob_url_Valid() const{
    return m_base_element_blob_url_isValid;
}

QString OAISlide_Slides_Details::getChangedBaseElementBlobUrl() const {
    return m_changed_base_element_blob_url;
}
void OAISlide_Slides_Details::setChangedBaseElementBlobUrl(const QString &changed_base_element_blob_url) {
    m_changed_base_element_blob_url = changed_base_element_blob_url;
    m_changed_base_element_blob_url_isSet = true;
}

bool OAISlide_Slides_Details::is_changed_base_element_blob_url_Set() const{
    return m_changed_base_element_blob_url_isSet;
}

bool OAISlide_Slides_Details::is_changed_base_element_blob_url_Valid() const{
    return m_changed_base_element_blob_url_isValid;
}

QDateTime OAISlide_Slides_Details::getDateCreated() const {
    return m_date_created;
}
void OAISlide_Slides_Details::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAISlide_Slides_Details::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAISlide_Slides_Details::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAISlide_Slides_Details::getDateModified() const {
    return m_date_modified;
}
void OAISlide_Slides_Details::setDateModified(const QDateTime &date_modified) {
    m_date_modified = date_modified;
    m_date_modified_isSet = true;
}

bool OAISlide_Slides_Details::is_date_modified_Set() const{
    return m_date_modified_isSet;
}

bool OAISlide_Slides_Details::is_date_modified_Valid() const{
    return m_date_modified_isValid;
}

OAIDocument_Details OAISlide_Slides_Details::getDocument() const {
    return m_document;
}
void OAISlide_Slides_Details::setDocument(const OAIDocument_Details &document) {
    m_document = document;
    m_document_isSet = true;
}

bool OAISlide_Slides_Details::is_document_Set() const{
    return m_document_isSet;
}

bool OAISlide_Slides_Details::is_document_Valid() const{
    return m_document_isValid;
}

QString OAISlide_Slides_Details::getDocumentId() const {
    return m_document_id;
}
void OAISlide_Slides_Details::setDocumentId(const QString &document_id) {
    m_document_id = document_id;
    m_document_id_isSet = true;
}

bool OAISlide_Slides_Details::is_document_id_Set() const{
    return m_document_id_isSet;
}

bool OAISlide_Slides_Details::is_document_id_Valid() const{
    return m_document_id_isValid;
}

QString OAISlide_Slides_Details::getId() const {
    return m_id;
}
void OAISlide_Slides_Details::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISlide_Slides_Details::is_id_Set() const{
    return m_id_isSet;
}

bool OAISlide_Slides_Details::is_id_Valid() const{
    return m_id_isValid;
}

QString OAISlide_Slides_Details::getName() const {
    return m_name;
}
void OAISlide_Slides_Details::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISlide_Slides_Details::is_name_Set() const{
    return m_name_isSet;
}

bool OAISlide_Slides_Details::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAISlide_Slides_Details::getNumber() const {
    return m_number;
}
void OAISlide_Slides_Details::setNumber(const qint32 &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAISlide_Slides_Details::is_number_Set() const{
    return m_number_isSet;
}

bool OAISlide_Slides_Details::is_number_Valid() const{
    return m_number_isValid;
}

qint32 OAISlide_Slides_Details::getOoxmlId() const {
    return m_ooxml_id;
}
void OAISlide_Slides_Details::setOoxmlId(const qint32 &ooxml_id) {
    m_ooxml_id = ooxml_id;
    m_ooxml_id_isSet = true;
}

bool OAISlide_Slides_Details::is_ooxml_id_Set() const{
    return m_ooxml_id_isSet;
}

bool OAISlide_Slides_Details::is_ooxml_id_Valid() const{
    return m_ooxml_id_isValid;
}

QString OAISlide_Slides_Details::getPackageUri() const {
    return m_package_uri;
}
void OAISlide_Slides_Details::setPackageUri(const QString &package_uri) {
    m_package_uri = package_uri;
    m_package_uri_isSet = true;
}

bool OAISlide_Slides_Details::is_package_uri_Set() const{
    return m_package_uri_isSet;
}

bool OAISlide_Slides_Details::is_package_uri_Valid() const{
    return m_package_uri_isValid;
}

OAISlide_ShapeTrees_Details OAISlide_Slides_Details::getShapeTree() const {
    return m_shape_tree;
}
void OAISlide_Slides_Details::setShapeTree(const OAISlide_ShapeTrees_Details &shape_tree) {
    m_shape_tree = shape_tree;
    m_shape_tree_isSet = true;
}

bool OAISlide_Slides_Details::is_shape_tree_Set() const{
    return m_shape_tree_isSet;
}

bool OAISlide_Slides_Details::is_shape_tree_Valid() const{
    return m_shape_tree_isValid;
}

QString OAISlide_Slides_Details::getSlideDocumentUrl() const {
    return m_slide_document_url;
}
void OAISlide_Slides_Details::setSlideDocumentUrl(const QString &slide_document_url) {
    m_slide_document_url = slide_document_url;
    m_slide_document_url_isSet = true;
}

bool OAISlide_Slides_Details::is_slide_document_url_Set() const{
    return m_slide_document_url_isSet;
}

bool OAISlide_Slides_Details::is_slide_document_url_Valid() const{
    return m_slide_document_url_isValid;
}

OAISlide_SlideMasters_Details OAISlide_Slides_Details::getSlideMaster() const {
    return m_slide_master;
}
void OAISlide_Slides_Details::setSlideMaster(const OAISlide_SlideMasters_Details &slide_master) {
    m_slide_master = slide_master;
    m_slide_master_isSet = true;
}

bool OAISlide_Slides_Details::is_slide_master_Set() const{
    return m_slide_master_isSet;
}

bool OAISlide_Slides_Details::is_slide_master_Valid() const{
    return m_slide_master_isValid;
}

QString OAISlide_Slides_Details::getSvgBlobUrl() const {
    return m_svg_blob_url;
}
void OAISlide_Slides_Details::setSvgBlobUrl(const QString &svg_blob_url) {
    m_svg_blob_url = svg_blob_url;
    m_svg_blob_url_isSet = true;
}

bool OAISlide_Slides_Details::is_svg_blob_url_Set() const{
    return m_svg_blob_url_isSet;
}

bool OAISlide_Slides_Details::is_svg_blob_url_Valid() const{
    return m_svg_blob_url_isValid;
}

OAITheme_Themes_Details OAISlide_Slides_Details::getTheme() const {
    return m_theme;
}
void OAISlide_Slides_Details::setTheme(const OAITheme_Themes_Details &theme) {
    m_theme = theme;
    m_theme_isSet = true;
}

bool OAISlide_Slides_Details::is_theme_Set() const{
    return m_theme_isSet;
}

bool OAISlide_Slides_Details::is_theme_Valid() const{
    return m_theme_isValid;
}

QString OAISlide_Slides_Details::getUserCreated() const {
    return m_user_created;
}
void OAISlide_Slides_Details::setUserCreated(const QString &user_created) {
    m_user_created = user_created;
    m_user_created_isSet = true;
}

bool OAISlide_Slides_Details::is_user_created_Set() const{
    return m_user_created_isSet;
}

bool OAISlide_Slides_Details::is_user_created_Valid() const{
    return m_user_created_isValid;
}

QString OAISlide_Slides_Details::getUserModified() const {
    return m_user_modified;
}
void OAISlide_Slides_Details::setUserModified(const QString &user_modified) {
    m_user_modified = user_modified;
    m_user_modified_isSet = true;
}

bool OAISlide_Slides_Details::is_user_modified_Set() const{
    return m_user_modified_isSet;
}

bool OAISlide_Slides_Details::is_user_modified_Valid() const{
    return m_user_modified_isValid;
}

bool OAISlide_Slides_Details::isSet() const {
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

        if (m_document.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_id_isSet) {
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

        if (m_number_isSet) {
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

        if (m_shape_tree.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_slide_document_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slide_master.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_svg_blob_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_theme.isSet()) {
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

bool OAISlide_Slides_Details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
