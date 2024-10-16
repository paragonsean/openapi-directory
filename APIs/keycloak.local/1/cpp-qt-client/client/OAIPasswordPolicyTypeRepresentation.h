/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPasswordPolicyTypeRepresentation.h
 *
 * 
 */

#ifndef OAIPasswordPolicyTypeRepresentation_H
#define OAIPasswordPolicyTypeRepresentation_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPasswordPolicyTypeRepresentation : public OAIObject {
public:
    OAIPasswordPolicyTypeRepresentation();
    OAIPasswordPolicyTypeRepresentation(QString json);
    ~OAIPasswordPolicyTypeRepresentation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getConfigType() const;
    void setConfigType(const QString &config_type);
    bool is_config_type_Set() const;
    bool is_config_type_Valid() const;

    QString getDefaultValue() const;
    void setDefaultValue(const QString &default_value);
    bool is_default_value_Set() const;
    bool is_default_value_Valid() const;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isMultipleSupported() const;
    void setMultipleSupported(const bool &multiple_supported);
    bool is_multiple_supported_Set() const;
    bool is_multiple_supported_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_config_type;
    bool m_config_type_isSet;
    bool m_config_type_isValid;

    QString m_default_value;
    bool m_default_value_isSet;
    bool m_default_value_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_multiple_supported;
    bool m_multiple_supported_isSet;
    bool m_multiple_supported_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPasswordPolicyTypeRepresentation)

#endif // OAIPasswordPolicyTypeRepresentation_H
