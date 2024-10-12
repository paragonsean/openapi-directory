/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICustomer_data_attribute_metadata_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomer_data_attribute_metadata_interface::OAICustomer_data_attribute_metadata_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomer_data_attribute_metadata_interface::OAICustomer_data_attribute_metadata_interface() {
    this->initializeModel();
}

OAICustomer_data_attribute_metadata_interface::~OAICustomer_data_attribute_metadata_interface() {}

void OAICustomer_data_attribute_metadata_interface::initializeModel() {

    m_attribute_code_isSet = false;
    m_attribute_code_isValid = false;

    m_backend_type_isSet = false;
    m_backend_type_isValid = false;

    m_data_model_isSet = false;
    m_data_model_isValid = false;

    m_frontend_class_isSet = false;
    m_frontend_class_isValid = false;

    m_frontend_input_isSet = false;
    m_frontend_input_isValid = false;

    m_frontend_label_isSet = false;
    m_frontend_label_isValid = false;

    m_input_filter_isSet = false;
    m_input_filter_isValid = false;

    m_is_filterable_in_grid_isSet = false;
    m_is_filterable_in_grid_isValid = false;

    m_is_searchable_in_grid_isSet = false;
    m_is_searchable_in_grid_isValid = false;

    m_is_used_in_grid_isSet = false;
    m_is_used_in_grid_isValid = false;

    m_is_visible_in_grid_isSet = false;
    m_is_visible_in_grid_isValid = false;

    m_multiline_count_isSet = false;
    m_multiline_count_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_options_isSet = false;
    m_options_isValid = false;

    m_required_isSet = false;
    m_required_isValid = false;

    m_sort_order_isSet = false;
    m_sort_order_isValid = false;

    m_store_label_isSet = false;
    m_store_label_isValid = false;

    m_system_isSet = false;
    m_system_isValid = false;

    m_user_defined_isSet = false;
    m_user_defined_isValid = false;

    m_validation_rules_isSet = false;
    m_validation_rules_isValid = false;

    m_visible_isSet = false;
    m_visible_isValid = false;
}

void OAICustomer_data_attribute_metadata_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomer_data_attribute_metadata_interface::fromJsonObject(QJsonObject json) {

    m_attribute_code_isValid = ::OpenAPI::fromJsonValue(m_attribute_code, json[QString("attribute_code")]);
    m_attribute_code_isSet = !json[QString("attribute_code")].isNull() && m_attribute_code_isValid;

    m_backend_type_isValid = ::OpenAPI::fromJsonValue(m_backend_type, json[QString("backend_type")]);
    m_backend_type_isSet = !json[QString("backend_type")].isNull() && m_backend_type_isValid;

    m_data_model_isValid = ::OpenAPI::fromJsonValue(m_data_model, json[QString("data_model")]);
    m_data_model_isSet = !json[QString("data_model")].isNull() && m_data_model_isValid;

    m_frontend_class_isValid = ::OpenAPI::fromJsonValue(m_frontend_class, json[QString("frontend_class")]);
    m_frontend_class_isSet = !json[QString("frontend_class")].isNull() && m_frontend_class_isValid;

    m_frontend_input_isValid = ::OpenAPI::fromJsonValue(m_frontend_input, json[QString("frontend_input")]);
    m_frontend_input_isSet = !json[QString("frontend_input")].isNull() && m_frontend_input_isValid;

    m_frontend_label_isValid = ::OpenAPI::fromJsonValue(m_frontend_label, json[QString("frontend_label")]);
    m_frontend_label_isSet = !json[QString("frontend_label")].isNull() && m_frontend_label_isValid;

    m_input_filter_isValid = ::OpenAPI::fromJsonValue(m_input_filter, json[QString("input_filter")]);
    m_input_filter_isSet = !json[QString("input_filter")].isNull() && m_input_filter_isValid;

    m_is_filterable_in_grid_isValid = ::OpenAPI::fromJsonValue(m_is_filterable_in_grid, json[QString("is_filterable_in_grid")]);
    m_is_filterable_in_grid_isSet = !json[QString("is_filterable_in_grid")].isNull() && m_is_filterable_in_grid_isValid;

    m_is_searchable_in_grid_isValid = ::OpenAPI::fromJsonValue(m_is_searchable_in_grid, json[QString("is_searchable_in_grid")]);
    m_is_searchable_in_grid_isSet = !json[QString("is_searchable_in_grid")].isNull() && m_is_searchable_in_grid_isValid;

    m_is_used_in_grid_isValid = ::OpenAPI::fromJsonValue(m_is_used_in_grid, json[QString("is_used_in_grid")]);
    m_is_used_in_grid_isSet = !json[QString("is_used_in_grid")].isNull() && m_is_used_in_grid_isValid;

    m_is_visible_in_grid_isValid = ::OpenAPI::fromJsonValue(m_is_visible_in_grid, json[QString("is_visible_in_grid")]);
    m_is_visible_in_grid_isSet = !json[QString("is_visible_in_grid")].isNull() && m_is_visible_in_grid_isValid;

    m_multiline_count_isValid = ::OpenAPI::fromJsonValue(m_multiline_count, json[QString("multiline_count")]);
    m_multiline_count_isSet = !json[QString("multiline_count")].isNull() && m_multiline_count_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_options_isValid = ::OpenAPI::fromJsonValue(m_options, json[QString("options")]);
    m_options_isSet = !json[QString("options")].isNull() && m_options_isValid;

    m_required_isValid = ::OpenAPI::fromJsonValue(m_required, json[QString("required")]);
    m_required_isSet = !json[QString("required")].isNull() && m_required_isValid;

    m_sort_order_isValid = ::OpenAPI::fromJsonValue(m_sort_order, json[QString("sort_order")]);
    m_sort_order_isSet = !json[QString("sort_order")].isNull() && m_sort_order_isValid;

    m_store_label_isValid = ::OpenAPI::fromJsonValue(m_store_label, json[QString("store_label")]);
    m_store_label_isSet = !json[QString("store_label")].isNull() && m_store_label_isValid;

    m_system_isValid = ::OpenAPI::fromJsonValue(m_system, json[QString("system")]);
    m_system_isSet = !json[QString("system")].isNull() && m_system_isValid;

    m_user_defined_isValid = ::OpenAPI::fromJsonValue(m_user_defined, json[QString("user_defined")]);
    m_user_defined_isSet = !json[QString("user_defined")].isNull() && m_user_defined_isValid;

    m_validation_rules_isValid = ::OpenAPI::fromJsonValue(m_validation_rules, json[QString("validation_rules")]);
    m_validation_rules_isSet = !json[QString("validation_rules")].isNull() && m_validation_rules_isValid;

    m_visible_isValid = ::OpenAPI::fromJsonValue(m_visible, json[QString("visible")]);
    m_visible_isSet = !json[QString("visible")].isNull() && m_visible_isValid;
}

QString OAICustomer_data_attribute_metadata_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomer_data_attribute_metadata_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_attribute_code_isSet) {
        obj.insert(QString("attribute_code"), ::OpenAPI::toJsonValue(m_attribute_code));
    }
    if (m_backend_type_isSet) {
        obj.insert(QString("backend_type"), ::OpenAPI::toJsonValue(m_backend_type));
    }
    if (m_data_model_isSet) {
        obj.insert(QString("data_model"), ::OpenAPI::toJsonValue(m_data_model));
    }
    if (m_frontend_class_isSet) {
        obj.insert(QString("frontend_class"), ::OpenAPI::toJsonValue(m_frontend_class));
    }
    if (m_frontend_input_isSet) {
        obj.insert(QString("frontend_input"), ::OpenAPI::toJsonValue(m_frontend_input));
    }
    if (m_frontend_label_isSet) {
        obj.insert(QString("frontend_label"), ::OpenAPI::toJsonValue(m_frontend_label));
    }
    if (m_input_filter_isSet) {
        obj.insert(QString("input_filter"), ::OpenAPI::toJsonValue(m_input_filter));
    }
    if (m_is_filterable_in_grid_isSet) {
        obj.insert(QString("is_filterable_in_grid"), ::OpenAPI::toJsonValue(m_is_filterable_in_grid));
    }
    if (m_is_searchable_in_grid_isSet) {
        obj.insert(QString("is_searchable_in_grid"), ::OpenAPI::toJsonValue(m_is_searchable_in_grid));
    }
    if (m_is_used_in_grid_isSet) {
        obj.insert(QString("is_used_in_grid"), ::OpenAPI::toJsonValue(m_is_used_in_grid));
    }
    if (m_is_visible_in_grid_isSet) {
        obj.insert(QString("is_visible_in_grid"), ::OpenAPI::toJsonValue(m_is_visible_in_grid));
    }
    if (m_multiline_count_isSet) {
        obj.insert(QString("multiline_count"), ::OpenAPI::toJsonValue(m_multiline_count));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_options.size() > 0) {
        obj.insert(QString("options"), ::OpenAPI::toJsonValue(m_options));
    }
    if (m_required_isSet) {
        obj.insert(QString("required"), ::OpenAPI::toJsonValue(m_required));
    }
    if (m_sort_order_isSet) {
        obj.insert(QString("sort_order"), ::OpenAPI::toJsonValue(m_sort_order));
    }
    if (m_store_label_isSet) {
        obj.insert(QString("store_label"), ::OpenAPI::toJsonValue(m_store_label));
    }
    if (m_system_isSet) {
        obj.insert(QString("system"), ::OpenAPI::toJsonValue(m_system));
    }
    if (m_user_defined_isSet) {
        obj.insert(QString("user_defined"), ::OpenAPI::toJsonValue(m_user_defined));
    }
    if (m_validation_rules.size() > 0) {
        obj.insert(QString("validation_rules"), ::OpenAPI::toJsonValue(m_validation_rules));
    }
    if (m_visible_isSet) {
        obj.insert(QString("visible"), ::OpenAPI::toJsonValue(m_visible));
    }
    return obj;
}

QString OAICustomer_data_attribute_metadata_interface::getAttributeCode() const {
    return m_attribute_code;
}
void OAICustomer_data_attribute_metadata_interface::setAttributeCode(const QString &attribute_code) {
    m_attribute_code = attribute_code;
    m_attribute_code_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_attribute_code_Set() const{
    return m_attribute_code_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_attribute_code_Valid() const{
    return m_attribute_code_isValid;
}

QString OAICustomer_data_attribute_metadata_interface::getBackendType() const {
    return m_backend_type;
}
void OAICustomer_data_attribute_metadata_interface::setBackendType(const QString &backend_type) {
    m_backend_type = backend_type;
    m_backend_type_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_backend_type_Set() const{
    return m_backend_type_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_backend_type_Valid() const{
    return m_backend_type_isValid;
}

QString OAICustomer_data_attribute_metadata_interface::getDataModel() const {
    return m_data_model;
}
void OAICustomer_data_attribute_metadata_interface::setDataModel(const QString &data_model) {
    m_data_model = data_model;
    m_data_model_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_data_model_Set() const{
    return m_data_model_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_data_model_Valid() const{
    return m_data_model_isValid;
}

QString OAICustomer_data_attribute_metadata_interface::getFrontendClass() const {
    return m_frontend_class;
}
void OAICustomer_data_attribute_metadata_interface::setFrontendClass(const QString &frontend_class) {
    m_frontend_class = frontend_class;
    m_frontend_class_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_frontend_class_Set() const{
    return m_frontend_class_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_frontend_class_Valid() const{
    return m_frontend_class_isValid;
}

QString OAICustomer_data_attribute_metadata_interface::getFrontendInput() const {
    return m_frontend_input;
}
void OAICustomer_data_attribute_metadata_interface::setFrontendInput(const QString &frontend_input) {
    m_frontend_input = frontend_input;
    m_frontend_input_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_frontend_input_Set() const{
    return m_frontend_input_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_frontend_input_Valid() const{
    return m_frontend_input_isValid;
}

QString OAICustomer_data_attribute_metadata_interface::getFrontendLabel() const {
    return m_frontend_label;
}
void OAICustomer_data_attribute_metadata_interface::setFrontendLabel(const QString &frontend_label) {
    m_frontend_label = frontend_label;
    m_frontend_label_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_frontend_label_Set() const{
    return m_frontend_label_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_frontend_label_Valid() const{
    return m_frontend_label_isValid;
}

QString OAICustomer_data_attribute_metadata_interface::getInputFilter() const {
    return m_input_filter;
}
void OAICustomer_data_attribute_metadata_interface::setInputFilter(const QString &input_filter) {
    m_input_filter = input_filter;
    m_input_filter_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_input_filter_Set() const{
    return m_input_filter_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_input_filter_Valid() const{
    return m_input_filter_isValid;
}

bool OAICustomer_data_attribute_metadata_interface::isIsFilterableInGrid() const {
    return m_is_filterable_in_grid;
}
void OAICustomer_data_attribute_metadata_interface::setIsFilterableInGrid(const bool &is_filterable_in_grid) {
    m_is_filterable_in_grid = is_filterable_in_grid;
    m_is_filterable_in_grid_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_is_filterable_in_grid_Set() const{
    return m_is_filterable_in_grid_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_is_filterable_in_grid_Valid() const{
    return m_is_filterable_in_grid_isValid;
}

bool OAICustomer_data_attribute_metadata_interface::isIsSearchableInGrid() const {
    return m_is_searchable_in_grid;
}
void OAICustomer_data_attribute_metadata_interface::setIsSearchableInGrid(const bool &is_searchable_in_grid) {
    m_is_searchable_in_grid = is_searchable_in_grid;
    m_is_searchable_in_grid_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_is_searchable_in_grid_Set() const{
    return m_is_searchable_in_grid_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_is_searchable_in_grid_Valid() const{
    return m_is_searchable_in_grid_isValid;
}

bool OAICustomer_data_attribute_metadata_interface::isIsUsedInGrid() const {
    return m_is_used_in_grid;
}
void OAICustomer_data_attribute_metadata_interface::setIsUsedInGrid(const bool &is_used_in_grid) {
    m_is_used_in_grid = is_used_in_grid;
    m_is_used_in_grid_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_is_used_in_grid_Set() const{
    return m_is_used_in_grid_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_is_used_in_grid_Valid() const{
    return m_is_used_in_grid_isValid;
}

bool OAICustomer_data_attribute_metadata_interface::isIsVisibleInGrid() const {
    return m_is_visible_in_grid;
}
void OAICustomer_data_attribute_metadata_interface::setIsVisibleInGrid(const bool &is_visible_in_grid) {
    m_is_visible_in_grid = is_visible_in_grid;
    m_is_visible_in_grid_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_is_visible_in_grid_Set() const{
    return m_is_visible_in_grid_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_is_visible_in_grid_Valid() const{
    return m_is_visible_in_grid_isValid;
}

qint32 OAICustomer_data_attribute_metadata_interface::getMultilineCount() const {
    return m_multiline_count;
}
void OAICustomer_data_attribute_metadata_interface::setMultilineCount(const qint32 &multiline_count) {
    m_multiline_count = multiline_count;
    m_multiline_count_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_multiline_count_Set() const{
    return m_multiline_count_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_multiline_count_Valid() const{
    return m_multiline_count_isValid;
}

QString OAICustomer_data_attribute_metadata_interface::getNote() const {
    return m_note;
}
void OAICustomer_data_attribute_metadata_interface::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_note_Set() const{
    return m_note_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_note_Valid() const{
    return m_note_isValid;
}

QList<OAICustomer_data_option_interface> OAICustomer_data_attribute_metadata_interface::getOptions() const {
    return m_options;
}
void OAICustomer_data_attribute_metadata_interface::setOptions(const QList<OAICustomer_data_option_interface> &options) {
    m_options = options;
    m_options_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_options_Set() const{
    return m_options_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_options_Valid() const{
    return m_options_isValid;
}

bool OAICustomer_data_attribute_metadata_interface::isRequired() const {
    return m_required;
}
void OAICustomer_data_attribute_metadata_interface::setRequired(const bool &required) {
    m_required = required;
    m_required_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_required_Set() const{
    return m_required_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_required_Valid() const{
    return m_required_isValid;
}

qint32 OAICustomer_data_attribute_metadata_interface::getSortOrder() const {
    return m_sort_order;
}
void OAICustomer_data_attribute_metadata_interface::setSortOrder(const qint32 &sort_order) {
    m_sort_order = sort_order;
    m_sort_order_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_sort_order_Set() const{
    return m_sort_order_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_sort_order_Valid() const{
    return m_sort_order_isValid;
}

QString OAICustomer_data_attribute_metadata_interface::getStoreLabel() const {
    return m_store_label;
}
void OAICustomer_data_attribute_metadata_interface::setStoreLabel(const QString &store_label) {
    m_store_label = store_label;
    m_store_label_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_store_label_Set() const{
    return m_store_label_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_store_label_Valid() const{
    return m_store_label_isValid;
}

bool OAICustomer_data_attribute_metadata_interface::isSystem() const {
    return m_system;
}
void OAICustomer_data_attribute_metadata_interface::setSystem(const bool &system) {
    m_system = system;
    m_system_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_system_Set() const{
    return m_system_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_system_Valid() const{
    return m_system_isValid;
}

bool OAICustomer_data_attribute_metadata_interface::isUserDefined() const {
    return m_user_defined;
}
void OAICustomer_data_attribute_metadata_interface::setUserDefined(const bool &user_defined) {
    m_user_defined = user_defined;
    m_user_defined_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_user_defined_Set() const{
    return m_user_defined_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_user_defined_Valid() const{
    return m_user_defined_isValid;
}

QList<OAICustomer_data_validation_rule_interface> OAICustomer_data_attribute_metadata_interface::getValidationRules() const {
    return m_validation_rules;
}
void OAICustomer_data_attribute_metadata_interface::setValidationRules(const QList<OAICustomer_data_validation_rule_interface> &validation_rules) {
    m_validation_rules = validation_rules;
    m_validation_rules_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_validation_rules_Set() const{
    return m_validation_rules_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_validation_rules_Valid() const{
    return m_validation_rules_isValid;
}

bool OAICustomer_data_attribute_metadata_interface::isVisible() const {
    return m_visible;
}
void OAICustomer_data_attribute_metadata_interface::setVisible(const bool &visible) {
    m_visible = visible;
    m_visible_isSet = true;
}

bool OAICustomer_data_attribute_metadata_interface::is_visible_Set() const{
    return m_visible_isSet;
}

bool OAICustomer_data_attribute_metadata_interface::is_visible_Valid() const{
    return m_visible_isValid;
}

bool OAICustomer_data_attribute_metadata_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_attribute_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_backend_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_model_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_frontend_class_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_frontend_input_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_frontend_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_input_filter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_filterable_in_grid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_searchable_in_grid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_used_in_grid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_visible_in_grid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_multiline_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_required_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sort_order_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_system_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_defined_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_validation_rules.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_visible_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomer_data_attribute_metadata_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_attribute_code_isValid && m_backend_type_isValid && m_data_model_isValid && m_frontend_class_isValid && m_frontend_input_isValid && m_frontend_label_isValid && m_input_filter_isValid && m_multiline_count_isValid && m_note_isValid && m_options_isValid && m_required_isValid && m_sort_order_isValid && m_store_label_isValid && m_system_isValid && m_user_defined_isValid && m_validation_rules_isValid && m_visible_isValid && true;
}

} // namespace OpenAPI
