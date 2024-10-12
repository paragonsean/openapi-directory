/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArticleUpdate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArticleUpdate::OAIArticleUpdate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArticleUpdate::OAIArticleUpdate() {
    this->initializeModel();
}

OAIArticleUpdate::~OAIArticleUpdate() {}

void OAIArticleUpdate::initializeModel() {

    m_authors_isSet = false;
    m_authors_isValid = false;

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_categories_by_source_id_isSet = false;
    m_categories_by_source_id_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_custom_fields_list_isSet = false;
    m_custom_fields_list_isValid = false;

    m_defined_type_isSet = false;
    m_defined_type_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_doi_isSet = false;
    m_doi_isValid = false;

    m_funding_isSet = false;
    m_funding_isValid = false;

    m_funding_list_isSet = false;
    m_funding_list_isValid = false;

    m_group_id_isSet = false;
    m_group_id_isValid = false;

    m_handle_isSet = false;
    m_handle_isValid = false;

    m_is_metadata_record_isSet = false;
    m_is_metadata_record_isValid = false;

    m_keywords_isSet = false;
    m_keywords_isValid = false;

    m_license_isSet = false;
    m_license_isValid = false;

    m_metadata_reason_isSet = false;
    m_metadata_reason_isValid = false;

    m_references_isSet = false;
    m_references_isValid = false;

    m_resource_doi_isSet = false;
    m_resource_doi_isValid = false;

    m_resource_title_isSet = false;
    m_resource_title_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_timeline_isSet = false;
    m_timeline_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIArticleUpdate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArticleUpdate::fromJsonObject(QJsonObject json) {

    m_authors_isValid = ::OpenAPI::fromJsonValue(m_authors, json[QString("authors")]);
    m_authors_isSet = !json[QString("authors")].isNull() && m_authors_isValid;

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("categories")]);
    m_categories_isSet = !json[QString("categories")].isNull() && m_categories_isValid;

    m_categories_by_source_id_isValid = ::OpenAPI::fromJsonValue(m_categories_by_source_id, json[QString("categories_by_source_id")]);
    m_categories_by_source_id_isSet = !json[QString("categories_by_source_id")].isNull() && m_categories_by_source_id_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_custom_fields_list_isValid = ::OpenAPI::fromJsonValue(m_custom_fields_list, json[QString("custom_fields_list")]);
    m_custom_fields_list_isSet = !json[QString("custom_fields_list")].isNull() && m_custom_fields_list_isValid;

    m_defined_type_isValid = ::OpenAPI::fromJsonValue(m_defined_type, json[QString("defined_type")]);
    m_defined_type_isSet = !json[QString("defined_type")].isNull() && m_defined_type_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_doi_isValid = ::OpenAPI::fromJsonValue(m_doi, json[QString("doi")]);
    m_doi_isSet = !json[QString("doi")].isNull() && m_doi_isValid;

    m_funding_isValid = ::OpenAPI::fromJsonValue(m_funding, json[QString("funding")]);
    m_funding_isSet = !json[QString("funding")].isNull() && m_funding_isValid;

    m_funding_list_isValid = ::OpenAPI::fromJsonValue(m_funding_list, json[QString("funding_list")]);
    m_funding_list_isSet = !json[QString("funding_list")].isNull() && m_funding_list_isValid;

    m_group_id_isValid = ::OpenAPI::fromJsonValue(m_group_id, json[QString("group_id")]);
    m_group_id_isSet = !json[QString("group_id")].isNull() && m_group_id_isValid;

    m_handle_isValid = ::OpenAPI::fromJsonValue(m_handle, json[QString("handle")]);
    m_handle_isSet = !json[QString("handle")].isNull() && m_handle_isValid;

    m_is_metadata_record_isValid = ::OpenAPI::fromJsonValue(m_is_metadata_record, json[QString("is_metadata_record")]);
    m_is_metadata_record_isSet = !json[QString("is_metadata_record")].isNull() && m_is_metadata_record_isValid;

    m_keywords_isValid = ::OpenAPI::fromJsonValue(m_keywords, json[QString("keywords")]);
    m_keywords_isSet = !json[QString("keywords")].isNull() && m_keywords_isValid;

    m_license_isValid = ::OpenAPI::fromJsonValue(m_license, json[QString("license")]);
    m_license_isSet = !json[QString("license")].isNull() && m_license_isValid;

    m_metadata_reason_isValid = ::OpenAPI::fromJsonValue(m_metadata_reason, json[QString("metadata_reason")]);
    m_metadata_reason_isSet = !json[QString("metadata_reason")].isNull() && m_metadata_reason_isValid;

    m_references_isValid = ::OpenAPI::fromJsonValue(m_references, json[QString("references")]);
    m_references_isSet = !json[QString("references")].isNull() && m_references_isValid;

    m_resource_doi_isValid = ::OpenAPI::fromJsonValue(m_resource_doi, json[QString("resource_doi")]);
    m_resource_doi_isSet = !json[QString("resource_doi")].isNull() && m_resource_doi_isValid;

    m_resource_title_isValid = ::OpenAPI::fromJsonValue(m_resource_title, json[QString("resource_title")]);
    m_resource_title_isSet = !json[QString("resource_title")].isNull() && m_resource_title_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_timeline_isValid = ::OpenAPI::fromJsonValue(m_timeline, json[QString("timeline")]);
    m_timeline_isSet = !json[QString("timeline")].isNull() && m_timeline_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIArticleUpdate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArticleUpdate::asJsonObject() const {
    QJsonObject obj;
    if (m_authors.size() > 0) {
        obj.insert(QString("authors"), ::OpenAPI::toJsonValue(m_authors));
    }
    if (m_categories.size() > 0) {
        obj.insert(QString("categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_categories_by_source_id.size() > 0) {
        obj.insert(QString("categories_by_source_id"), ::OpenAPI::toJsonValue(m_categories_by_source_id));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_custom_fields_list.size() > 0) {
        obj.insert(QString("custom_fields_list"), ::OpenAPI::toJsonValue(m_custom_fields_list));
    }
    if (m_defined_type_isSet) {
        obj.insert(QString("defined_type"), ::OpenAPI::toJsonValue(m_defined_type));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_doi_isSet) {
        obj.insert(QString("doi"), ::OpenAPI::toJsonValue(m_doi));
    }
    if (m_funding_isSet) {
        obj.insert(QString("funding"), ::OpenAPI::toJsonValue(m_funding));
    }
    if (m_funding_list.size() > 0) {
        obj.insert(QString("funding_list"), ::OpenAPI::toJsonValue(m_funding_list));
    }
    if (m_group_id_isSet) {
        obj.insert(QString("group_id"), ::OpenAPI::toJsonValue(m_group_id));
    }
    if (m_handle_isSet) {
        obj.insert(QString("handle"), ::OpenAPI::toJsonValue(m_handle));
    }
    if (m_is_metadata_record_isSet) {
        obj.insert(QString("is_metadata_record"), ::OpenAPI::toJsonValue(m_is_metadata_record));
    }
    if (m_keywords.size() > 0) {
        obj.insert(QString("keywords"), ::OpenAPI::toJsonValue(m_keywords));
    }
    if (m_license_isSet) {
        obj.insert(QString("license"), ::OpenAPI::toJsonValue(m_license));
    }
    if (m_metadata_reason_isSet) {
        obj.insert(QString("metadata_reason"), ::OpenAPI::toJsonValue(m_metadata_reason));
    }
    if (m_references.size() > 0) {
        obj.insert(QString("references"), ::OpenAPI::toJsonValue(m_references));
    }
    if (m_resource_doi_isSet) {
        obj.insert(QString("resource_doi"), ::OpenAPI::toJsonValue(m_resource_doi));
    }
    if (m_resource_title_isSet) {
        obj.insert(QString("resource_title"), ::OpenAPI::toJsonValue(m_resource_title));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_timeline.isSet()) {
        obj.insert(QString("timeline"), ::OpenAPI::toJsonValue(m_timeline));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QList<OAIObject> OAIArticleUpdate::getAuthors() const {
    return m_authors;
}
void OAIArticleUpdate::setAuthors(const QList<OAIObject> &authors) {
    m_authors = authors;
    m_authors_isSet = true;
}

bool OAIArticleUpdate::is_authors_Set() const{
    return m_authors_isSet;
}

bool OAIArticleUpdate::is_authors_Valid() const{
    return m_authors_isValid;
}

QList<qint64> OAIArticleUpdate::getCategories() const {
    return m_categories;
}
void OAIArticleUpdate::setCategories(const QList<qint64> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIArticleUpdate::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIArticleUpdate::is_categories_Valid() const{
    return m_categories_isValid;
}

QList<QString> OAIArticleUpdate::getCategoriesBySourceId() const {
    return m_categories_by_source_id;
}
void OAIArticleUpdate::setCategoriesBySourceId(const QList<QString> &categories_by_source_id) {
    m_categories_by_source_id = categories_by_source_id;
    m_categories_by_source_id_isSet = true;
}

bool OAIArticleUpdate::is_categories_by_source_id_Set() const{
    return m_categories_by_source_id_isSet;
}

bool OAIArticleUpdate::is_categories_by_source_id_Valid() const{
    return m_categories_by_source_id_isValid;
}

OAIObject OAIArticleUpdate::getCustomFields() const {
    return m_custom_fields;
}
void OAIArticleUpdate::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIArticleUpdate::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIArticleUpdate::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QList<OAICustomArticleFieldAdd> OAIArticleUpdate::getCustomFieldsList() const {
    return m_custom_fields_list;
}
void OAIArticleUpdate::setCustomFieldsList(const QList<OAICustomArticleFieldAdd> &custom_fields_list) {
    m_custom_fields_list = custom_fields_list;
    m_custom_fields_list_isSet = true;
}

bool OAIArticleUpdate::is_custom_fields_list_Set() const{
    return m_custom_fields_list_isSet;
}

bool OAIArticleUpdate::is_custom_fields_list_Valid() const{
    return m_custom_fields_list_isValid;
}

QString OAIArticleUpdate::getDefinedType() const {
    return m_defined_type;
}
void OAIArticleUpdate::setDefinedType(const QString &defined_type) {
    m_defined_type = defined_type;
    m_defined_type_isSet = true;
}

bool OAIArticleUpdate::is_defined_type_Set() const{
    return m_defined_type_isSet;
}

bool OAIArticleUpdate::is_defined_type_Valid() const{
    return m_defined_type_isValid;
}

QString OAIArticleUpdate::getDescription() const {
    return m_description;
}
void OAIArticleUpdate::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIArticleUpdate::is_description_Set() const{
    return m_description_isSet;
}

bool OAIArticleUpdate::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIArticleUpdate::getDoi() const {
    return m_doi;
}
void OAIArticleUpdate::setDoi(const QString &doi) {
    m_doi = doi;
    m_doi_isSet = true;
}

bool OAIArticleUpdate::is_doi_Set() const{
    return m_doi_isSet;
}

bool OAIArticleUpdate::is_doi_Valid() const{
    return m_doi_isValid;
}

QString OAIArticleUpdate::getFunding() const {
    return m_funding;
}
void OAIArticleUpdate::setFunding(const QString &funding) {
    m_funding = funding;
    m_funding_isSet = true;
}

bool OAIArticleUpdate::is_funding_Set() const{
    return m_funding_isSet;
}

bool OAIArticleUpdate::is_funding_Valid() const{
    return m_funding_isValid;
}

QList<OAIFundingCreate> OAIArticleUpdate::getFundingList() const {
    return m_funding_list;
}
void OAIArticleUpdate::setFundingList(const QList<OAIFundingCreate> &funding_list) {
    m_funding_list = funding_list;
    m_funding_list_isSet = true;
}

bool OAIArticleUpdate::is_funding_list_Set() const{
    return m_funding_list_isSet;
}

bool OAIArticleUpdate::is_funding_list_Valid() const{
    return m_funding_list_isValid;
}

qint64 OAIArticleUpdate::getGroupId() const {
    return m_group_id;
}
void OAIArticleUpdate::setGroupId(const qint64 &group_id) {
    m_group_id = group_id;
    m_group_id_isSet = true;
}

bool OAIArticleUpdate::is_group_id_Set() const{
    return m_group_id_isSet;
}

bool OAIArticleUpdate::is_group_id_Valid() const{
    return m_group_id_isValid;
}

QString OAIArticleUpdate::getHandle() const {
    return m_handle;
}
void OAIArticleUpdate::setHandle(const QString &handle) {
    m_handle = handle;
    m_handle_isSet = true;
}

bool OAIArticleUpdate::is_handle_Set() const{
    return m_handle_isSet;
}

bool OAIArticleUpdate::is_handle_Valid() const{
    return m_handle_isValid;
}

bool OAIArticleUpdate::isIsMetadataRecord() const {
    return m_is_metadata_record;
}
void OAIArticleUpdate::setIsMetadataRecord(const bool &is_metadata_record) {
    m_is_metadata_record = is_metadata_record;
    m_is_metadata_record_isSet = true;
}

bool OAIArticleUpdate::is_is_metadata_record_Set() const{
    return m_is_metadata_record_isSet;
}

bool OAIArticleUpdate::is_is_metadata_record_Valid() const{
    return m_is_metadata_record_isValid;
}

QList<QString> OAIArticleUpdate::getKeywords() const {
    return m_keywords;
}
void OAIArticleUpdate::setKeywords(const QList<QString> &keywords) {
    m_keywords = keywords;
    m_keywords_isSet = true;
}

bool OAIArticleUpdate::is_keywords_Set() const{
    return m_keywords_isSet;
}

bool OAIArticleUpdate::is_keywords_Valid() const{
    return m_keywords_isValid;
}

qint64 OAIArticleUpdate::getLicense() const {
    return m_license;
}
void OAIArticleUpdate::setLicense(const qint64 &license) {
    m_license = license;
    m_license_isSet = true;
}

bool OAIArticleUpdate::is_license_Set() const{
    return m_license_isSet;
}

bool OAIArticleUpdate::is_license_Valid() const{
    return m_license_isValid;
}

QString OAIArticleUpdate::getMetadataReason() const {
    return m_metadata_reason;
}
void OAIArticleUpdate::setMetadataReason(const QString &metadata_reason) {
    m_metadata_reason = metadata_reason;
    m_metadata_reason_isSet = true;
}

bool OAIArticleUpdate::is_metadata_reason_Set() const{
    return m_metadata_reason_isSet;
}

bool OAIArticleUpdate::is_metadata_reason_Valid() const{
    return m_metadata_reason_isValid;
}

QList<QString> OAIArticleUpdate::getReferences() const {
    return m_references;
}
void OAIArticleUpdate::setReferences(const QList<QString> &references) {
    m_references = references;
    m_references_isSet = true;
}

bool OAIArticleUpdate::is_references_Set() const{
    return m_references_isSet;
}

bool OAIArticleUpdate::is_references_Valid() const{
    return m_references_isValid;
}

QString OAIArticleUpdate::getResourceDoi() const {
    return m_resource_doi;
}
void OAIArticleUpdate::setResourceDoi(const QString &resource_doi) {
    m_resource_doi = resource_doi;
    m_resource_doi_isSet = true;
}

bool OAIArticleUpdate::is_resource_doi_Set() const{
    return m_resource_doi_isSet;
}

bool OAIArticleUpdate::is_resource_doi_Valid() const{
    return m_resource_doi_isValid;
}

QString OAIArticleUpdate::getResourceTitle() const {
    return m_resource_title;
}
void OAIArticleUpdate::setResourceTitle(const QString &resource_title) {
    m_resource_title = resource_title;
    m_resource_title_isSet = true;
}

bool OAIArticleUpdate::is_resource_title_Set() const{
    return m_resource_title_isSet;
}

bool OAIArticleUpdate::is_resource_title_Valid() const{
    return m_resource_title_isValid;
}

QList<QString> OAIArticleUpdate::getTags() const {
    return m_tags;
}
void OAIArticleUpdate::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIArticleUpdate::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIArticleUpdate::is_tags_Valid() const{
    return m_tags_isValid;
}

OAITimelineUpdate OAIArticleUpdate::getTimeline() const {
    return m_timeline;
}
void OAIArticleUpdate::setTimeline(const OAITimelineUpdate &timeline) {
    m_timeline = timeline;
    m_timeline_isSet = true;
}

bool OAIArticleUpdate::is_timeline_Set() const{
    return m_timeline_isSet;
}

bool OAIArticleUpdate::is_timeline_Valid() const{
    return m_timeline_isValid;
}

QString OAIArticleUpdate::getTitle() const {
    return m_title;
}
void OAIArticleUpdate::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIArticleUpdate::is_title_Set() const{
    return m_title_isSet;
}

bool OAIArticleUpdate::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIArticleUpdate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_authors.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories_by_source_id.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_defined_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_doi_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_funding_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_funding_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_handle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_metadata_record_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_keywords.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_license_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_metadata_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_references.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_doi_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_timeline.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArticleUpdate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
